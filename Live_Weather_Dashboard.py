import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import numpy as np

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Weather Dashboard"

# Open-Meteo API with corrected parameters
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&hourly=temperature_2m,relative_humidity_2m,windspeed_10m&timezone=auto"


# Layout update with corrected style for the slider
app.layout = html.Div([
    html.H1("Live Weather Dashboard", style={'textAlign': 'center', 'color': '#004466'}),
    dcc.Interval(id='interval-component', interval=60000, n_intervals=0),
    
    # Display current weather values
    html.Div(id='current-weather', style={'textAlign': 'center', 'margin': '20px', 'fontSize': '18px'}),
    
    html.Div(id='weather-summary', style={'textAlign': 'center', 'margin': '20px', 'fontSize': '18px'}),
    
    # Dropdown for metrics selection
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Temperature (°C)', 'value': 'Temperature (°C)'},
            {'label': 'Humidity (%)', 'value': 'Humidity (%)'},
            {'label': 'Wind Speed (m/s)', 'value': 'Wind Speed (m/s)'}
        ],
        value='Temperature (°C)',  # Default value
        style={'width': '50%', 'margin': 'auto', 'padding': '10px'}
    ),
    
    # Div container for slider with style applied to the container
    html.Div(
        dcc.Slider(
            id='hour-slider',
            min=1,
            max=168,
            step=1,
            value=12,
            marks={i: f'{i}h' for i in range(1, 168, 12)},
            tooltip={"placement": "bottom", "always_visible": True}
        ),
        style={'width': '50%', 'margin': 'auto', 'padding': '20px'}
    ),
    
    # Weather graphs
    dcc.Graph(id='weather-bar-chart'),
    dcc.Graph(id='weather-line-chart'),
    dcc.Graph(id='weather-pie-chart'),
    
    # Correlation matrix plot
    dcc.Graph(id='correlation-matrix')
], style={'fontFamily': 'Arial', 'backgroundColor': '#f2f2f2', 'padding': '20px'})

# Fetch Weather data
def fetch_weather():
    response = requests.get(API_URL).json()
    timestamps = response["hourly"]["time"][-168:]  # Last 48 hours
    data = {
        "Temperature (°C)": response["hourly"]["temperature_2m"][-168:],
        "Humidity (%)": response["hourly"]["relative_humidity_2m"][-168:],
        "Wind Speed (m/s)": response["hourly"]["windspeed_10m"][-168:]
    }
    df = pd.DataFrame(data, index=pd.to_datetime(timestamps))
    return df

# Callback to update dashboard
@app.callback(
    [Output('current-weather', 'children'),
     Output('weather-summary', 'children'),
     Output('weather-bar-chart', 'figure'),
     Output('weather-line-chart', 'figure'),
     Output('weather-pie-chart', 'figure'),
     Output('correlation-matrix', 'figure')],
    [Input('interval-component', 'n_intervals'),
     Input('metric-dropdown', 'value'),
     Input('hour-slider', 'value')]
)
def update_dashboard(n, selected_metric, hours_range):
    df = fetch_weather()
    
    # Adjust data to user-selected hours range
    df_range = df.iloc[-hours_range:]
    
    latest_values = df_range.iloc[-1]
    
    # Current weather values (Temperature, Humidity, Wind Speed)
    current_weather = [
        f"Temperature: {latest_values['Temperature (°C)']}°C",
        f"Humidity: {latest_values['Humidity (%)']}%",
        f"Wind Speed: {latest_values['Wind Speed (m/s)']} m/s"
    ]
    
    # Summary
    summary = f"Latest Weather - {selected_metric}: {latest_values[selected_metric]} {selected_metric.split('(')[-1].strip(')')}"
    
    # Bar Chart (Selected Metric) with color change
    bar_colors = {
        'Temperature (°C)': 'royalblue',
        'Humidity (%)': 'lightcoral',
        'Wind Speed (m/s)': 'yellowgreen'
    }
    
    bar_fig = go.Figure([go.Bar(x=[selected_metric], y=[latest_values[selected_metric]], marker_color=bar_colors[selected_metric])])
    bar_fig.update_layout(title=f'Current {selected_metric}', xaxis_title='Metric', yaxis_title='Value')
    
    # Line Chart (Weather Trends Over Time)
    line_colors = {
        'Temperature (°C)': 'royalblue',
        'Humidity (%)': 'lightcoral',
        'Wind Speed (m/s)': 'yellowgreen'
    }
    
    line_fig = go.Figure()
    line_fig.add_trace(go.Scatter(x=df_range.index, y=df_range[selected_metric], mode='lines+markers', name=selected_metric, line=dict(color=line_colors[selected_metric])))
    line_fig.update_layout(title=f'{selected_metric} Trends Over Time', xaxis_title='Time', yaxis_title='Value')
    
    # Pie Chart (Proportions of Selected Metrics)
    pie_colors = ['green', 'yellow', 'red']
    pie_fig = go.Figure([go.Pie(labels=df_range.columns, values=df_range.iloc[-1], marker=dict(colors=pie_colors))])
    pie_fig.update_layout(title=f'{selected_metric} Proportions')
    
    # Correlation Matrix with annotated values
    corr_matrix = df.corr()
    corr_matrix_fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='Viridis',
        colorbar=dict(title="Correlation"),
        showscale=True,
        zmin=-1, zmax=1
    ))
    
    # Adding annotations (values) to the heatmap
    for i in range(len(corr_matrix.columns)):
        for j in range(len(corr_matrix.columns)):
            corr_matrix_fig.add_annotation(
                x=corr_matrix.columns[j],
                y=corr_matrix.columns[i],
                text=f'{corr_matrix.iloc[i, j]:.2f}',
                showarrow=False,
                font=dict(size=12, color='white'),
                align='center'
            )

    corr_matrix_fig.update_layout(title='Correlation Matrix of Weather Features', xaxis_title='Features', yaxis_title='Features')

    return current_weather, summary, bar_fig, line_fig, pie_fig, corr_matrix_fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
