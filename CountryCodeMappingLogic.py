import pandas
data = pandas.read_csv("disaster.csv")
first = data[['Entity','Code']].drop_duplicates(subset=['Entity'])
first.to_csv('countryMapping.csv',index=False)