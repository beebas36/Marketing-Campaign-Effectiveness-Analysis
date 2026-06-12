# Marketing Campaign Effectiveness Analysis

## Project Overview
This project analyzes digital marketing campaign performance using Python-based data analytics techniques.
The goal is to evaluate campaign effectiveness, identify key factors influencing customer conversion, and generate actionable business insights for future marketing optimization.

## Objectives
- Analyze campaign performance across channels.
- Identify factors affecting customer conversion.
- Detect and handle missing values and outliers.
- Create new business metrics using feature engineering.
- Visualize marketing performance trends.
- Generate insights for strategic decision-making.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- GitHub

## Dataset Information
The dataset contains customer demographics, campaign details, engagement metrics, and conversion outcomes.

### Features
- Customer Demographics
- Campaign Information
- Website Engagement
- Email Engagement
- Social Engagement
- Conversion Metrics

## Project Workflow
### 1. Data Collection

- Load dataset using Pandas
- Explore dataset structure
- Check data types
- Generate summary statistics

### 2. Data Cleaning
- Remove irrelevant columns
- Handle missing values
- Remove duplicate records
- Detect and treat outliers

### 3. Feature Engineering
Created:

- ConversionPercentage
- ClickThroughRatePercentage
- EmailEngagement
- VisitQualityScore
- MarketingEfficiency
- SocialEngagement

### 4. Exploratory Data Analysis
Visualizations include:
- Campaign Channel Performance
- Campaign Type Performance
- Ad Spend Distribution
- Gender-Based Conversion Analysis
- Correlation Heatmap
- Marketing Funnel Analysis

### 5. Results
Key drivers of conversion:
- Email Engagement
- Website Visits
- Time On Site
- Pages Per Visit
- Previous Purchases
- Loyalty Points

## Project Structure
Marketing-Campaign-Effectiveness-Analysis/

├── data/
│   ├── digital_marketing_campaign_dataset.csv
│   └── cleaned_Marketing_Dataset.csv
│
├── notebooks/
│   └── Marketing_Campaign_Analysis.ipynb
│
├── scripts/
│   └── Marketing_Campaign.py
│
├── images/
│   └── visualizations
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/Marketing-Campaign-Effectiveness-Analysis.git
```

Navigate to project folder:
```bash
cd Marketing-Campaign-Effectiveness-Analysis
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the project:
```bash
python Marketing_Campaign.py
```
## Key Insights
- Customer engagement is a stronger predictor of conversion than advertising spend.
- Email marketing significantly influences campaign success.
- Website quality impacts customer decision-making.
- High-performing channels should receive larger budget allocations.
- Funnel analysis helps identify customer drop-off points.

## Future Improvements
- Build predictive machine learning models.
- Develop campaign recommendation systems.
- Deploy dashboard using Streamlit.
- Automate reporting pipelines.

## Author
Bibas Basnet
Data Analysis Project