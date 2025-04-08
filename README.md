# Natural Disaster Prediction Using Machine Learning

![Image](https://github.com/user-attachments/assets/6b77c463-1acc-4f63-943e-67d3f41cc2fd)

## 📋 Overview

This project develops AI-based prediction models to enhance early warning systems and disaster preparedness for natural disasters including floods, tornadoes, earthquakes, and forest fires. By leveraging machine learning capabilities, we forecast the likelihood, intensity, and location of natural disasters, allowing authorities to plan and respond more effectively.

## 🎯 Project Goals

- Develop robust ML models for predicting various natural disasters
- Enhance early warning systems to save lives
- Enable better disaster preparedness and response
- Reduce economic losses due to natural disasters

## 📊 Results

Our machine learning models have achieved promising results:

| Disaster Type | Accuracy |
|---------------|----------|
| Flood Prediction | 71.95% |
| Wildfire Detection | 84% |
| Tornado Prediction | 83% |
| Earthquake Detection | 78.53% |

## 💻 Technologies Used

- Python
- Machine Learning Libraries:
  - Scikit-learn
  - TensorFlow/Keras
  - Pandas
  - NumPy
- Support Vector Machines
- Decision Trees
- Random Forests
- Convolutional Neural Networks
- Logistic Regression
- K-Nearest Neighbors

## 📁 File Structure

```
└── Natural-Disaster-Prediction/
    ├── Earth-quake Detection/         # Earthquake detection model
    ├── Fire Detection/                # Wildfire detection model
    ├── Flood detection/               # Flood prediction model
    ├── Tornado Detection/             # Tornado prediction model
    ├── docs/
    │   ├── Report_dc_2.pdf            # Detailed project report
    │   └── Project_Presentation.pptx  # Project presentation slides
    ├── Live_Weather_Dashboard.py      # Python script for dashboard
    ├── Live_Weather_Dashboard.mp4     # Video demo of the dashboard
    ├── LICENSE                        # Apache-2.0 license
    └── README.md                      # Project documentation
```

## 🎬 Video Demo

A video demonstration of the project's live weather dashboard is available in the repository. The `Live_Weather_Dashboard.mp4` file shows the real-time operation of our prediction system and how it integrates data from various sources to provide accurate disaster predictions.

https://github.com/user-attachments/assets/c8cb67f8-4516-4329-bbaa-e9072a3faac1

## 🔍 Models Overview

### Flood Prediction
Uses Support Vector Regressor (SVR) and Decision Tree Regressor to process rainfall, river flow, and other hydrological data.

### Tornado Prediction
Employs Logistic Regression, Decision Tree, Random Forest, and K-Nearest Neighbors to classify atmospheric conditions that may lead to tornado formation.

### Earthquake Detection
Utilizes SVM, Multiple Linear Regression, Naive Bayes, and Random Forest to analyze seismic waveform and geolocation data for early detection.

### Wildfire Detection
Implements Convolutional Neural Networks (CNNs) to process satellite imagery, identifying heat signatures, dryness indexes, and vegetation patterns for hotspot detection.

## 🌊 Real-world Impact

Our models address disasters with significant social and economic impacts:

- **Floods**: Account for 43% of all disaster events with $40 billion in annual global losses
- **Tornadoes**: Cost the U.S. alone an average of $10 billion annually
- **Earthquakes**: Global losses averaging over $14 billion annually
- **Forest Fires**: In 2020, U.S. wildfire damages surpassed $16.5 billion

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Required libraries (see requirements.txt)
- Access to weather/climate data sources

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/Natural-Disaster-Prediction.git

# Navigate to the project directory
cd Natural-Disaster-Prediction

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
python Live_Weather_Dashboard.py
```

## 📄 Documentation

For more detailed information about the project, please refer to:
- `Report_dc_2.pdf`: Comprehensive project report with methodology and findings
- `Project_Presentation.pptx`: Presentation slides with visual explanations

## 👨‍💻 Contributors

- Ronak Gadhiya (B22AI052)
- Anuj Chincholikar (B22ES018)
- Vishesh Sachdeva (B22AI050)
- Dilip Gampala (B22CH011)

## 📃 License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.
