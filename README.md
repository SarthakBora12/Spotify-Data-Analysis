🎧 Spotify Analytics Project
A complete data analytics project that explores Spotify streaming behavior using Python, SQL, and BI tools.
This project focuses on transforming raw data into meaningful insights through structured data modeling and analysis.
📌 Overview
The purpose of this project is to analyze Spotify streaming data to understand:
User listening behavior
Artist popularity trends
Subscription-based usage patterns
Geographic and demographic insights
The project follows an end-to-end analytics workflow, similar to what is used in real-world data teams.
🔄 Data Pipeline
Data Collection
Mock Spotify streaming data
API-based ingestion using Python
Data Transformation
Cleaning and preprocessing
Feature standardization and validation
SQL-based transformations
Data Modeling
Fact and dimension tables
Star schema optimized for analytics
Analysis & Reporting
Aggregations and metrics
Dashboard-ready datasets
🧱 Data Model
Fact Table
fact_streams – Records individual streaming events
Dimension Tables
dim_artist – Artist details
dim_country – Country information
dim_age_group – User age segmentation
dim_subscription – Subscription types
This model enables efficient slicing of data across multiple business dimensions.
❓ Questions Answered
Which artists generate the highest streaming volume?
How does streaming behavior differ across age groups?
Which countries contribute most to total streams?
How do subscription types impact engagement?
📊 Sample Insights
Premium users show higher engagement compared to free users.
A small group of artists accounts for a large share of total streams.
Younger listeners tend to stream more frequently.
Streaming behavior varies significantly by region.
🛠️ Tools & Technologies
Python – Data ingestion and preprocessing
SQL – Data transformation and analysis
PySpark / Spark SQL – Scalable data processing
SQLite / CSV – Data storage
Power BI – Data visualization
