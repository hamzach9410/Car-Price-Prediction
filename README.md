# 🚗 Car Price Prediction Model

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modern, interactive web application built with Streamlit that predicts used car prices using machine learning. The application features a clean, responsive UI with real-time predictions based on car specifications.

## 🌟 Features

- **Interactive Form Interface**: User-friendly car selection with dynamic dropdowns
- **Real-time Predictions**: Instant price estimates without page reloads
- **Modern UI Design**: Responsive layout with gradient backgrounds and smooth animations
- **Smart Filtering**: Model options update dynamically based on selected company
- **Input Validation**: Comprehensive error handling and user feedback
- **Session Management**: Maintains prediction state across interactions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd car-price-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📖 Usage Guide

1. **Select Car Company**: Choose from available car manufacturers
2. **Pick Model**: Select specific car model (filtered by company)
3. **Choose Year**: Select manufacturing year
4. **Select Fuel Type**: Pick fuel type (Petrol, Diesel, CNG, etc.)
5. **Enter Kilometers**: Input total distance driven
6. **Get Prediction**: Click "Predict Price" for instant estimate

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **ML Model** | Linear Regression (scikit-learn) |
| **Data Processing** | pandas, numpy |
| **Styling** | Custom CSS |

## 📁 Project Structure

```
car-price-predictor/
├── streamlit_app.py          # Main application file
├── LinearRegressionModel.pkl # Pre-trained ML model
├── Cleaned_car_data.csv      # Dataset for predictions
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## 🔧 Model Information

- **Algorithm**: Linear Regression
- **Training Data**: Cleaned car dataset with features like company, model, year, fuel type, and kilometers
- **Accuracy Enhancement**: 3.5x multiplier applied for improved price estimates
- **Input Features**: Car company, model, manufacturing year, fuel type, kilometers driven

## 📊 Dependencies

```txt
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.21.0
scikit-learn>=1.1.0
pickle-mixin>=1.0.2
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨💻 Author

**Ali Hamza**
- Email: [ihamzaali06@gmail.com](mailto:ihamzaali06@gmail.com)
- GitHub: [@alihamza](https://github.com/alihamza)

---

<div align="center">
  <strong>Made with ❤️ by Ali Hamza</strong>
</div>