# 🎧 Spotify Analytics Project

An end-to-end data analytics project focused on analyzing Spotify streaming behavior using Python, SQL, Spark, and BI tools.  
This project demonstrates real-world data workflows including ingestion, transformation, dimensional modeling, and insight generation.

---

## 📌 Project Overview

This project explores Spotify streaming data to uncover insights related to:
- User listening behavior
- Artist popularity and engagement
- Subscription-based usage patterns
- Geographic and demographic trends

The goal is to simulate a production-style analytics pipeline and showcase practical data analysis and analytics engineering skills.

---

## 🔄 Data Pipeline

1. **Data Ingestion**
   - Spotify API ingestion using Python
   - CSV-based mock streaming data

2. **Data Transformation**
   - Data cleaning and validation
   - Feature standardization
   - Transformations using SQL and PySpark

3. **Data Modeling**
   - Star schema design
   - Fact and dimension tables optimized for analytics

4. **Analysis & Reporting**
   - Aggregated metrics
   - BI-ready datasets for dashboards

---

## 🧱 Data Model

### Fact Table
- `fact_streams`  
  Contains individual streaming events with references to users, artists, countries, and subscription types.

### Dimension Tables
- `dim_artist` – Artist metadata  
- `dim_country` – Country information  
- `dim_age_group` – User age segmentation  
- `dim_subscription` – Subscription type details  

This dimensional model enables efficient analytical querying and reporting.

---

## ❓ Key Questions Answered

- Which artists generate the highest number of streams?
- How does streaming behavior vary by age group and country?
- Which subscription types drive the most engagement?
- Are there noticeable demographic trends in music consumption?

---

## 📊 Sample Insights

- Premium users contribute a significantly higher share of total streams.
- A small number of artists account for the majority of platform engagement.
- Younger age groups demonstrate higher streaming frequency.
- Streaming patterns vary considerably across different regions.

---

## 🛠️ Tools & Technologies

- **Python** – Data ingestion and preprocessing  
- **SQL** – Data transformation and analysis  
- **PySpark / Spark SQL** – Scalable data processing  
- **CSV / SQLite** – Data storage  
- **Power BI** – Data visualization and reporting  

---

## 📁 Project Structure

-├── spotify_api_ingestion.py # Spotify API data ingestion
-├── Spotify_ETL.ipynb # ETL and transformations
-├── spotify_streaming_data.csv # Raw streaming data
-├── fact_streams.csv # Fact table
-├── dim_artist.csv # Artist dimension
-├── dim_country.csv # Country dimension
-├── dim_age_group.csv # Age group dimension
-├── dim_subscription.csv # Subscription dimension
-├── spotify_extended.db # SQLite database
-└── README.md # Project documentation
---

## 🧠 Skills Demonstrated

- End-to-end data pipeline development  
- Data cleaning and transformation  
- Dimensional data modeling (star schema)  
- SQL-based analytics and aggregation  
- Business-focused data analysis  
- BI-ready data preparation  

---

## 🚀 Future Enhancements

- Automate ingestion with scheduled workflows
- Implement incremental data loading
- Build interactive dashboards
- Apply machine learning for user segmentation or recommendations

---

## 👤 Author

**Sarthak Bora**  
Data Analyst | Analytics Engineer  
SQL • Python • Spark • Power BI


