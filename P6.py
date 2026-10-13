import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
titanic_df = pd.read_csv(url)

print("--- Missing Values Before Preprocessing ---")
print(titanic_df.isnull().sum())

titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].median())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0])
if 'Cabin' in titanic_df.columns:
    titanic_df.drop('Cabin', axis=1, inplace=True)

le_sex = LabelEncoder()
titanic_df['Sex_Encoded'] = le_sex.fit_transform(titanic_df['Sex'])

le_embarked = LabelEncoder()
titanic_df['Embarked_Encoded'] = le_embarked.fit_transform(titanic_df['Embarked'])

scaler = MinMaxScaler()
num_cols = ['Age', 'Fare']
titanic_df[num_cols] = scaler.fit_transform(titanic_df[num_cols])

print("\n--- Missing Values After Preprocessing ---")
print(titanic_df.isnull().sum())

print("\n--- Preprocessed Dataset Sample ---")
display(titanic_df[['PassengerId', 'Survived', 'Pclass', 'Sex_Encoded', 'Age', 'Fare', 'Embarked_Encoded']].head())
