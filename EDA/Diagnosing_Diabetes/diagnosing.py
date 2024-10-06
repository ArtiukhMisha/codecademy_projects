import pandas as pd
import numpy as np

diabetes_data = pd.read_csv('../Diagnosing_Diabetes/diabetes.csv')
#print(diabetes_data)

print(diabetes_data.info())
print(diabetes_data.describe())
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)
print(diabetes_data.info())
print(diabetes_data[diabetes_data.isnull().any(axis=1)])
diabetes_data['Outcome'].unique()
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O',0).astype('int')
diabetes_data[diabetes_data['Insulin']>500]
diabetes_data['Insulin'] = diabetes_data['Insulin'].replace(np.nan,diabetes_data['Insulin'].median())