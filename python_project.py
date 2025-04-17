import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df=pd.read_csv("airline.csv")
print(df)
print("Information of Dataset: \n")
print(df.info())
print("Description of Dataset: \n")
print(df.describe())

#finding missing values
print("Missing value or not?? \n")
print(df.isnull().sum())

#filling missing values with 112
df['Arrival Delay']=df['Arrival Delay'].fillna(112)
print("1st 10 rows of datset: \n")
print(df.head(10))
print("last 10 rows of datset: \n")
print(df.tail(10))

#print rows and column numbers
print("Shape of DataSet:  \n",df.shape)
print("Columns of DataSet:  \n",df.columns)
print("Datatype of DataSet: \n ",df.dtypes)

# Fill missing values in all columns with the mode
#filling missing values with mode and locating at 1st index
df = df.fillna(df.mode().iloc[0])

#handling only numeric colums and then checking iff all values are numeric. If not filling
#them with mode
numeric_cols = ['Age', 'Flight Distance', 'Check-in Service', 'Online Boarding',
                'Departure Delay', 'Arrival Delay', 'Seat Comfort']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].fillna(df[col].mode()[0])

# Set plot style
#rc params is a dict storing all changeble aspects rc stands for runtime configuration
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1) Overall Satisfaction Levels
sns.countplot(data=df, x='Satisfaction')
plt.title('Overall Satisfaction Levels')
plt.show()

# Pie Chart
counts = df['Satisfaction'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
plt.title('Satisfaction Distribution (Pie Chart)')
plt.show()

# Donut Chart
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90,
        colors=sns.color_palette("pastel"), wedgeprops=dict(width=0.4))
plt.title('Satisfaction Distribution (Donut Chart)')
plt.show()

# 2) Satisfaction by Travel Class
sns.countplot(data=df, x='Class', hue='Satisfaction', palette='muted')
plt.title('Satisfaction by Travel Class')
plt.show()

# 3) Impact of Customer Type
sns.countplot(data=df, x='Customer Type', hue='Satisfaction', palette='Set2')
plt.title('Satisfaction by Customer Type')
plt.show()

# 4) Check-in and Boarding Experience
sns.boxplot(data=df, x='Satisfaction', y='Check-in Service', hue='Satisfaction', palette='coolwarm', legend=False)
plt.title('Check-in Service by Satisfaction')
plt.show()

sns.boxplot(data=df, x='Satisfaction', y='Online Boarding', hue='Satisfaction', palette='coolwarm', legend=False)
plt.title('Online Boarding by Satisfaction')
plt.show()

#using kde to show smooth transition of data
5) Satisfaction Based on Flight Distance or Duration
sns.histplot(data=df, x='Flight Distance', hue='Satisfaction', bins=30, kde=True, palette='Set1')
plt.title('Flight Distance and Satisfaction')
plt.show()

# KDE Plot
sns.kdeplot(data=df, x='Flight Distance', hue='Satisfaction', fill=True)
plt.title('KDE of Flight Distance by Satisfaction')
plt.show()

# Heatmap
corr = df.select_dtypes(include=['int64', 'float64']).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# Scatter Plot
sns.scatterplot(data=df, x='Flight Distance', y='Age', hue='Satisfaction', palette='cool')
plt.title('Flight Distance vs Age Colored by Satisfaction')
plt.show()

# Bar Chart
rating_cols = ['Check-in Service', 'Online Boarding', 'Seat Comfort']
df.groupby('Satisfaction')[rating_cols].mean().T.plot(kind='bar', colormap='viridis')
plt.title('Average Ratings by Satisfaction')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
#fixing the layout
plt.tight_layout()
plt.show()

# Horizontal Bar Chart
df.groupby('Satisfaction')[['Departure Delay', 'Arrival Delay']].mean().plot(kind='barh', colormap='plasma')
plt.title('Average Delays by Satisfaction')
plt.xlabel('Delay (minutes)')
plt.tight_layout()
plt.show()


# Histogram: Age
sns.histplot(df['Age'], bins=30, kde=True, color='teal')
plt.title('Distribution of Passenger Age')
plt.show()

# Count Plot: Type of Travel
sns.countplot(data=df, x='Type of Travel')
plt.title('Count of Travel Types')
plt.show()
