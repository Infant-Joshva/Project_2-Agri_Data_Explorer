# 🌾 Agri Data Explorer

A Mini Project to analyze Indian agricultural datasets using **Python**, **Pandas**, **SciPy**, **Plotly**, **Streamlit**, and **Power BI**.  
It provides statistical insights and interactive dashboards for understanding trends in crop production, yield, and cultivated area.

---

## 🚀 Key Features

- 🔍 Exploratory Data Analysis via Streamlit  
- 📈 Interactive visualizations using Plotly  
- 📊 Power BI Dashboard for state/district level insights  
- 🧪 Statistical computations with SciPy
- 💾 CSV & PostgreSQL support via SQLAlchemy  
- ☁️ Google Colab notebooks for EDA and preprocessing

---

## 🛠️ Tech Stack

| Tool/Library   | Purpose                            |
|----------------|-------------------------------------|
| Python         | Core scripting                     |
| Pandas         | Data manipulation                  |
| SciPy          | Statistical analysis               |
| Streamlit      | Interactive web app                |
| Plotly         | Advanced visualizations            |
| Power BI       | Business-level dashboards          |
| SQLAlchemy     | Database connection (PostgreSQL)   |
| Google Colab   | Notebook-based EDA                 |

---

## 📁 Project Structure

```
Agri-Data-Explorer/
├── app/                # Streamlit app code
│   └── main.py
├── data/               # Raw and cleaned datasets
├── scripts/            # ETL scripts
├── dashboards/         # Power BI .pbix files
├── notebooks/          # Google Colab notebooks
├── images/videos             # Visuals for dashboard & # Project demonstration video
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── LICENSE             # Open-source license
└── .gitignore          # Files to be ignored by Git
```

---

### 📊 Streamlit Dashboard Preview

#### 📌 Rice vs Wheat Production Over the Last 50 Years

![Rice vs Wheat Production](https://github.com/user-attachments/assets/1ff28d88-7cfc-4105-aef6-3dc78ecd3c5a)

---

#### 📌 Impact of Area Cultivated on Rice, Wheat, and Maize Production

![Impact of Area Cultivated](https://github.com/user-attachments/assets/08ef3d7a-1845-4aa3-b101-d8f3be5a045c)

---

## 📊 Power BI Dashboard

📁 Located in the `dashboards/` folder  

#### 📌 Power BI Dashboard Preview

![Power BI Preview](https://github.com/user-attachments/assets/8e994d9c-1fac-402d-835f-33cce18a4df9)
--
![Power BI Preview](https://github.com/user-attachments/assets/1a3c0e4c-9370-4963-a720-ac60245163e9)
--
![Power BI Preview](https://github.com/user-attachments/assets/8b459b52-be8f-4f45-a854-308b75991f0b)

---

## 🧪 Sample Insights

- 📈 Year‑wise trend of rice production across top 3 states  
- 🌾 Districts with highest wheat yield in last 5 years  
- 🛢️ Top oilseed producing states and their growth  
- 🌽 Area vs. production correlation for major crops  
- 🧵 Cotton production trends and groundnut yield by district

---

## 🔧 Installation & Running

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Agri-Data-Explorer.git
cd Agri-Data-Explorer
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

## 📝 Requirements

The following Python libraries are required:

- pandas  
- scipy  
- plotly  
- streamlit  
- sqlalchemy  
- psycopg2-binary 

### 4. Run the Streamlit app
```bash
streamlit run app/main.py
```

---

## 📚 Data Sources

- India agricultural datasets 
- Custom CSV/Excel files based on domain data

---

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full text.

---

## 👤 Author

Project developed by **Infant Joshva A**

📧 infantjoshva46@gmail.com  
🐙 [GitHub](https://github.com/Infant-Joshva)  
🔗 [LinkedIn](https://www.linkedin.com/in/infant-joshva)

## ⭐ Give a Star!

If you liked this project, please give it a ⭐ on GitHub!
