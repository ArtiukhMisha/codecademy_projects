import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
print(census.dtypes)

print(census.head(10))

census['birth_year'] = census['birth_year'].replace(['missing'], 1967)
census['birth_year'] = census['birth_year'].astype('int')
census['higher_tax'] = pd.Categorical(census['higher_tax'],['strongly disagree','disagree','neutral','agree','strongly agree'])
census['encode_tax'] = census['higher_tax'].cat.codes

census =pd.get_dummies(data=census,columns=['marital_status'])
print(census.head())
print(census.encode_tax.median())