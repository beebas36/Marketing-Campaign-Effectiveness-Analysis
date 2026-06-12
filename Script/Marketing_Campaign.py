#importing libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
df = pd.read_csv(r'c:\Users\User\OneDrive\Desktop\Marketing Campaign Effectiveness Analysis\digital_marketing_campaign_dataset.csv')
print(df.head())

#initial exploration
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe)
print(df.describe(include=["object",'string']))
print(df.info)
print(df.isnull().sum())

#remove non-useful columns
df.drop(columns=['AdvertisingPlatform','AdvertisingTool'],inplace=True)

#check duplicates
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

#missing value treatment for numerical columns
num_cols = df.select_dtypes(include=["number"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

#missing value treatment for categorical columns
cat_cols = df.select_dtypes(include=['object', 'string']).columns
for cols in cat_cols:
    df[cols] = df[cols].fillna(df[cols].mode()[0])

#detecting outlier using boxplot
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    plt.figure(figsize=(8,5))
    sns.boxplot(x = df[col])
    plt.title(f"Box plot of {col}")
    plt.show()
    

#removing outlier
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower,upper)

#checking outlier after removing
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    count = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
    print(f"{col}: {count} Remaining outliers")

#feature engineering
#conversion percentage
df['ConversionPercentage'] = df['ConversionRate'] * 100

#CTR percentage
df['ClickThroughRatePercentage'] = df['ClickThroughRate'] * 100

#Email Engagement
df['EmailEngagement'] = df['EmailClicks'] + (df['EmailOpens'] + 1)

#visit quality score
df["VisitQualityScore"] = df['PagesPerVisit'] * df['TimeOnSite']

#Marketing efficiency
df["MarketingEfficiency"] = df['ConversionRate'] * df["ClickThroughRate"]

#Social engagement
df["socialEngagement"] = df['SocialShares'] + df['EmailClicks'] + df["WebsiteVisits"]

#EDA
#conversion Rate by campaign channel
plt.figure(figsize=(8,5))
ax = sns.barplot(x='CampaignChannel',y='ConversionRate',data=df)
for container in ax.containers:
    ax.bar_label(container)
plt.title('Conversion Rate by Campaign Channel')
plt.show()

#campaign channel distribution
plt.figure(figsize=(8,5))
sns.countplot(x='CampaignChannel', data = df)
plt.title("Campaign Channel Distribution")
plt.show()

#campaign type performance
plt.figure(figsize=(8,5))
sns.barplot(x ='CampaignType', y='ConversionRate', data=df)
plt.title("Conversion Rate by Campaign Type")
plt.show()

#Adspend distribution
plt.figure(figsize=(8,5))
sns.histplot(x='AdSpend', data=df, bins=30, kde=True)
plt.title("Distribution of Adspend")
plt.show()

#Gender based conversion
plt.figure(figsize=(8,5))
sns.barplot(x='Gender', y='ConversionRate', data = df)
plt.title("Gender based Conversion Rate")
plt.show()

#Adspend vs Conversion Rate
plt.figure(figsize=(8,5))
sns.scatterplot(x='AdSpend', y='ConversionRate', data=df)
plt.title("Adspend vs Conversion Rate")
plt.show()

#correlation Heatmap
corr = df.corr(numeric_only = True)
plt.figure(figsize=(8,5))
sns.heatmap(corr, annot = True, cmap = "coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

#marketing funnel analysis
stages = ['Visited Website', 'Opened Email', 'Clicked Email', 'Converted']
counts = df[['WebsiteVisits', 'EmailOpens', 'EmailClicks', 'Conversion']].sum()
plt.figure(figsize=(8,5))
plt.bar(stages,counts)
plt.title("Marketing Funnel Analysis")
plt.xlabel('Stages')
plt.ylabel("Number of users")
plt.show()

#saved cleaned dataset
df.to_csv("cleaned_Marketing_Dataset.csv", index=False)