import pandas as pd
df = pd.read_csv("sample.csv")
df['SSN'] = df['SSN'].astype(str)
df['DOB'] = df['DOB'].astype(str)
df['Weight'] = df['Weight'].astype(str)
df['Height'] = df['Height'].astype(str)
df['Age'] = df['Age'].astype(str)
df['HeightFt'] = df['HeightFt'].astype(str)
df['HtIn'] = df['HtIn'].astype(str)
df['BMI'] = df['BMI'].astype(str)
s=df.groupby(['NameF', 'NameL']).agg({'SSN':lambda x : ' | '.join(set(x)),'Weight':lambda x : ' | '.join(set(x)),'Height':lambda x : ' | '.join(set(x)),'DOB':lambda x : ' | '.join(set(x)),'Hometown':lambda x : ' | '.join(set(x)),'Prov':lambda x : ' | '.join(set(x)),'Pos':lambda x : ' | '.join(set(x)),'Age':lambda x : ' | '.join(set(x)),'HeightFt':lambda x : ' | '.join(set(x)),'HtIn':lambda x : ' | '.join(set(x)),'BMI':lambda x : ' | '.join(set(x))})
s.to_csv('full.csv')
df = pd.read_csv('merged.csv')
print(df)