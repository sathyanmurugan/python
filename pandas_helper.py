import pandas as pd


df = pd.read_csv(path_to_csv,encoding='utf8')

#read as datetime
df['Date']  = pd.to_datetime(df['Date'],format='%Y-%m-%d %H:%M:%S')

#convert to specific date format
df['survey_date'] = df['Date Submitted'].apply(lambda row: row.strftime('%Y-%m'))

#extract certain columns as Dataframe
df = df[['survey_date',poll_name]]

#case operations when looping
df[poll_name] = df[poll_name].apply(lambda row: 
	'detractors' if row < 7 else
	'passive' if row >= 7 and row < 9 else
	'promoters'
	)

#Groupby, sum, convert to DF
df = pd.DataFrame(df.groupby('survey_date').sum())

#Mark column as index
df['survey_date'] = df.index

#Change column type
df['nps_score'] = df['nps_score'].astype(int)

#Melt
df = pd.melt(df,id_vars=['survey_date'],var_name='type')

df = df.rename(columns={'Id':'OwnerId'})