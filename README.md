# 🚗 Car Price Prediction

> A Python-based machine learning project for estimating car prices using real-world automotive listing data collected from Bama.ir.

<p align="center">
  <strong>Web Scraping • Data Processing • PostgreSQL • Machine Learning</strong>
</p>

---

## 📌 Overview

**Car Price Prediction** is an educational machine learning project that estimates the price of cars based on historical listing data collected from **Bama.ir**, an Iranian automotive classifieds platform.

The project follows a complete data pipeline:

```text
┌──────────────────┐
│    Bama.ir       │
│  Car Listings    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Web Scraping   │
│ crawler.py       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    PostgreSQL    │
│     Database     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Data Processing  │
│     Pandas       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Machine Learning │
│ Random Forest    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Price Prediction│
└──────────────────┘
```

The application collects car information, stores the dataset in PostgreSQL, processes the data, trains a `RandomForestRegressor` model, and uses the trained model to estimate the price of a car based on its characteristics.

---

## ✨ Features

- 🚙 **Automated Data Scraping**
  - Collects car advertisement data from Bama.ir.
  - Iterates through multiple pages to build a larger dataset.

- 🗄️ **PostgreSQL Database Integration**
  - Stores scraped car data in PostgreSQL.
  - Uses SQLAlchemy for database interaction.

- 🧹 **Data Preprocessing**
  - Processes scraped data before model training.
  - Handles categorical features such as:
    - Car name
    - Transmission
    - Fuel type
    - Body status

- 🤖 **Machine Learning**
  - Uses Scikit-learn's `RandomForestRegressor`.
  - Splits the available dataset into training and testing sets.
  - Trains a regression model to estimate car prices.

- 🔐 **Environment Configuration**
  - Uses `python-decouple` for configuration and database credentials.
  - Keeps sensitive configuration outside the source code.

- 💰 **Interactive Price Prediction**
  - Accepts car characteristics from the terminal.
  - Returns an estimated price based on the trained model.

---

## 🧠 Machine Learning Pipeline

The machine learning workflow can be summarized as:

```text
Raw Car Listings
       │
       ▼
Data Collection
       │
       ▼
Data Cleaning
       │
       ▼
Feature Processing
       │
       ▼
Categorical Encoding
       │
       ▼
Train / Test Split
       │
       ▼
RandomForestRegressor
       │
       ▼
Trained Model
       │
       ▼
User Input
       │
       ▼
Predicted Car Price
```

### Input Features

The model uses information such as:

| Feature | Description |
|---|---|
| `name` | Car model/name |
| `year` | Production year |
| `mileage` | Vehicle mileage |
| `transmission` | Manual or automatic transmission |
| `fuel` | Fuel type |
| `body_status` | Vehicle body/paint condition |

### Target

The target variable is the **car price**.

> ⚠️ Prediction quality depends heavily on the quality, quantity, freshness, and distribution of the collected data, as well as the preprocessing and model configuration.

---

## 🛠️ Tech Stack

### Core

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming language |
| 🐼 Pandas | Data processing and manipulation |
| 🤖 Scikit-learn | Machine learning |
| 🌐 Requests | HTTP requests |
| 🥣 Beautiful Soup 4 | Web scraping |
| 🗄️ SQLAlchemy | Database interaction |
| 🐘 PostgreSQL | Data storage |
| 🔌 Psycopg2 | PostgreSQL driver |
| 🔐 Python-Decouple | Environment/configuration management |
| 📦 Joblib | Python object/model serialization |

### Supporting Libraries

The project also uses supporting dependencies such as:

- NumPy
- Python-Dateutil
- Certifi
- Charset-Normalizer
- Greenlet
- IDNA
- Pytz
- Six
- Soupsieve
- Threadpoolctl
- Typing Extensions
- Tzdata
- Urllib3

---

## 📂 Project Structure

```text
car-price-prediction/
│
├── .env
│   └── Environment variables and database configuration
│
├── crawler.py
│   └── Scrapes car listings and stores them in PostgreSQL
│
├── car_ai.py
│   └── Data preprocessing, model training, and price prediction
│
├── price_prediction.py
│   └── Main entry point for the prediction workflow
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

- Python 3.9+
- pip
- Git
- PostgreSQL

---

### 1. Clone the Repository

```bash
git clone https://github.com/Mahdiwav/car-price-prediction.git
cd car-price-prediction
```

### 2. Create a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the project root.

Example:

```env
ENGINE=postgresql://USER:PASSWORD@HOST:PORT/DATABASE_NAME

DATABASE_NAME=your_db_name
HOST_NAME=your_db_host
USER=your_db_user
PASSWORD=your_db_password
PORT=your_db_port
```

Replace the placeholder values with your PostgreSQL configuration.

### ⚠️ Security

Never commit your `.env` file or database credentials to GitHub.

Make sure `.env` is included in `.gitignore`:

```gitignore
.env
```

---

# ▶️ Usage

The project contains three main Python scripts.

---

## 1. 🕷️ Run the Crawler

`crawler.py` is responsible for collecting car listings from Bama.ir and storing the data in PostgreSQL.

Run:

```bash
python crawler.py
```

The crawler iterates through multiple pages and collects car information for the dataset.

> The crawler also attempts to create the `car` database table when it does not already exist.

---

## 2. 🤖 Train the Machine Learning Model

`car_ai.py` contains the machine learning logic.

Its responsibilities include:

1. Reading car data from PostgreSQL
2. Preprocessing the dataset
3. Encoding categorical features
4. Splitting the dataset into training and testing sets
5. Creating a `RandomForestRegressor`
6. Training the model
7. Providing price prediction functionality

---

## 3. 💰 Run Price Prediction

`price_prediction.py` acts as the main entry point for the prediction workflow.

It coordinates the following process:

```text
Connect to Database
        ↓
Collect Car Data
        ↓
Prepare Dataset
        ↓
Train Model
        ↓
Collect User Input
        ↓
Predict Price
        ↓
Display Result
```

Run:

```bash
python price_prediction.py
```

---

# 💡 Example Prediction Workflow

After running the prediction script, the application asks for information about the car.

Typical inputs include:

```text
Car name
Production year
Mileage
Transmission type
Fuel type
Body condition
```

For example:

```text
Car name: Peugeot 206
Year: 1399
Mileage: 45000
Transmission: manual
Fuel: gasoline
Body status: no paint
```

The trained model then processes the provided features and returns an estimated car price.

---

## 🔎 Real-World Use Case

Imagine you are buying or selling a used car in Iran.

Instead of relying only on a subjective price estimate, this project can use historical marketplace data to provide an estimated value based on characteristics such as:

- Car model
- Production year
- Mileage
- Transmission
- Fuel type
- Body condition

The result can be used as an **estimated market value**, rather than a guaranteed selling price.

---

## ⚠️ Limitations

This project is primarily an educational machine learning project and should not be considered a production-grade pricing system.

Potential limitations include:

- Prediction quality depends on the collected dataset.
- Marketplace prices can change over time.
- Scraped data may contain noise or inconsistent values.
- Important market factors may not be represented in the available features.
- Categorical encoding can affect model behavior.
- A single Random Forest model may not be optimal for every dataset.
- Model performance should be evaluated using appropriate regression metrics before being used for real-world decisions.

---

## 📊 Model Evaluation

The project uses a train/test split during the machine learning workflow.

For a production-oriented version, the following metrics could be added to evaluate the regression model:

```text
MAE
MSE
RMSE
R²
```

This would make it possible to quantitatively compare model performance and evaluate whether the predictions are reliable enough for practical use.

---

## 🔮 Future Improvements

Possible improvements include:

- [ ] Add MAE, MSE, RMSE, and R² evaluation
- [ ] Add cross-validation
- [ ] Compare Random Forest with other regression algorithms
- [ ] Improve categorical feature encoding
- [ ] Add feature engineering
- [ ] Handle outliers and missing values more systematically
- [ ] Add automated data cleaning
- [ ] Save and load trained models with Joblib
- [ ] Create a REST API for predictions
- [ ] Build a web interface for price prediction
- [ ] Add Docker support
- [ ] Add automated tests
- [ ] Add GitHub Actions CI
- [ ] Add scheduled data collection
- [ ] Add model retraining workflow
- [ ] Add model versioning and experiment tracking

---

## 🤝 Contributing

Contributions and improvements are welcome.

### Contribution Workflow

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Implement your changes.
4. Add or update tests where appropriate.
5. Commit your changes:

```bash
git commit -m "Add AmazingFeature"
```

6. Push your branch:

```bash
git push origin feature/AmazingFeature
```

7. Open a Pull Request.

Please keep changes focused and document important modifications.

---

## 📄 License

No license is currently specified for this project.

If you plan to distribute or reuse the project publicly, consider adding an appropriate open-source license.

---

## ⚖️ Data Source & Responsible Scraping

This project uses publicly accessible automotive listing data from Bama.ir for educational and machine learning purposes.

When running or modifying the crawler, users should respect the website's terms of service, robots.txt directives, rate limits, and applicable laws.

The project is not affiliated with or endorsed by Bama.ir.

---

## 👨‍💻 Author

**Mahdi Faghani**

Python / Backend Developer

---

## ⭐ Support

If you find this project useful:

⭐ Star the repository  
🍴 Fork the project  
🐛 Report bugs through Issues  
💡 Suggest improvements

---

<p align="center">
  Built with ❤️ and Python
</p>
