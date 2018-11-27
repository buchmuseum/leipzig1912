import pandas as pd
import numpy as np

df = pd.read_csv("Leipzig-1912-komplett-flat.csv", delimiter=";", header=0)
print(df['PLZ_2018'].head())

df['PLZ_2018'] = '0' + df['PLZ_2018'].astype(str).str[:-2]
df['SBZ_NR_2018'] = df['SBZ_NR_2018'].astype(str).str[:-2]
df['OT_NR_2018'] = df['OT_NR_2018'].astype(str).str[:-2]
df['FirmenNr'] = df['FirmenNr'].astype(str).str[:-2]
df['HaeuserNr'] = df['HaeuserNr'].astype(str).str[:-2]

df.to_csv('Leipzig-1912-komplett-flat-clean.csv', sep=';', index=False)
