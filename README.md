# 🌾 Agri Data Explorer

A Mini Project to analyze Indian agricultural datasets using **Python**, **Pandas**, **NumPy**, **SciPy**, **Plotly**, **Streamlit**, and **Power BI**.  
It provides statistical insights and interactive dashboards for understanding trends in crop production, yield, and cultivated area.

---

## 🚀 Key Features

- 🔍 Exploratory Data Analysis via Streamlit  
- 📈 Interactive visualizations using Plotly  
- 📊 Power BI Dashboard for state/district level insights  
- 🧪 Statistical computations with SciPy and NumPy  
- 💾 CSV & PostgreSQL support via SQLAlchemy  
- ☁️ Google Colab notebooks for EDA and preprocessing

---

## 🛠️ Tech Stack

| Tool/Library   | Purpose                            |
|----------------|-------------------------------------|
| Python         | Core scripting                     |
| Pandas         | Data manipulation                  |
| NumPy          | Numerical computations             |
| SciPy          | Statistical analysis               |
| Streamlit      | Interactive web app                |
| Plotly         | Advanced visualizations            |
| Power BI       | Business-level dashboards          |
| SQLAlchemy     | Database connection (PostgreSQL)   |
| Google Colab   | Notebook-based EDA (optional)      |

---

## 📁 Project Structure

```
Agri-Data-Explorer/
├── app/                # Streamlit app code
│   └── main.py
├── data/               # Raw and cleaned datasets
├── scripts/            # Data preprocessing scripts
├── dashboards/         # Power BI .pbix files
├── notebooks/          # Google Colab notebooks
├── images/             # Visuals for README or dashboard
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── LICENSE             # Open-source license
└── .gitignore          # Files to be ignored by Git
```

---

## 📊 Power BI Dashboard

📁 Located in the `dashboards/` folder  
📷 *Insert your Power BI screenshot:*  
![Power BI Preview](images/powerbi-preview.png)

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

### 2. (Optional) Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app
```bash
streamlit run app/main.py
```

---

## 📚 Data Sources

- Government of India agricultural datasets  
- Open data portals (e.g. data.gov.in, UCI Machine Learning Repository)  
- Custom CSV/Excel files based on domain data

---

## 📝 Requirements

Include the following in your `requirements.txt`:
```
pandas
numpy
scipy
plotly
streamlit
sqlalchemy
psycopg2-binary
```

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full text.

---

## 👤 Author

Project developed by **[Your Name]**  
📧 your.email@example.com  
🔗 GitHub: [@your-username](https://github.com/your-username)  
🔗 LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
