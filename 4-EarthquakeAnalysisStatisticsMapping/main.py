import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium 

df = pd.read_excel('earthquake.xlsx')

# # first 5 lines
# print('first 5 lines: ')
# print(df.head())

# # general information about the dataset
# print("\nData Set Information: ")
# print(df.info)

# # basic statistical summary
# print('basic statistical summary: ')
# print(df.describe())

# # are there any missing data?
# print("\nAre there any missing data? ")
# print(df.isnull().sum) # if false -> then no

# ! combining date and time columns
df['TarihSaat'] = pd.to_datetime(df['Tarih'].astype(str)+ " " + df['Saat'],format="%Y.%m.%d %H:%M:%S")
df.drop(['Tarih','Saat'],axis=1,inplace=True)

# # control the combining
# print('\nUpdated data: ')
# print(df.dtypes)

# !! Analyze and manipulate with ML 
df['ML'] = pd.to_numeric(df['ML'],errors='coerce')
print("\n Missing values in the 'ML' column:")
print(df['ML'].isnull().sum())
# Remove it if it exists. (empty data?)
df_clean = df.dropna(subset=['ML'])
print('Size of the cleaned dataset: ',df_clean.shape)

# # 1-Number of earthquakes by date
# plt.figure(figsize=(12,6))
# sns.countplot(data=df_clean,x=df_clean['TarihSaat'].dt.date,palette='viridis')
# plt.xticks(rotation=45)
# plt.title('Number of earthquakes by day')
# plt.xlabel('Date')
# plt.ylabel('Number of earthquakes')e
# plt.tight_layout()
# plt.show()

# # 2-Earthquake magnitude distribution
# plt.figure(figsize=(8,6))
# sns.histplot(df_clean['ML'],bins=20,kde=True,color='blue') 
# # bins:up -> details up
# plt.title('Earthquake magnitude distribution')
# plt.xlabel("Magnitude (ML)")
# plt.ylabel("Frequency")
# plt.show()

# # 3-Earthquake magnitudes according to depth
# plt.figure(figsize=(8,6))
# sns.scatterplot(data=df_clean,x='Derinlik(km)' ,y='ML' , hue='Yer', palette='deep')
# plt.title('Earthquake magnitudes according to depth.')
# plt.xlabel('Depth(KM)')
# plt.ylabel('Magnitude(ML)')
# plt.legend(bbox_to_anchor=(1.03,1),loc='upper left') #bbox_to_anchor=(weight,height)
# plt.tight_layout()
# plt.show()

# Determine the map center.
mapCenter = [38.0,35.0]
m = folium.Map(location=mapCenter,zoom_start=5)

# Her bir depremi haritaya ekle
for idx , row in df_clean.iterrows():
    folium.CircleMarker(
        location=[row['Enlem(N)'], row['Boylam(E)']],
        radius=row['ML']*2,
        popup=f"Yer:{row['Yer']}<br>Magnitude: {row['ML']}<br>Depth:{row['Derinlik(km)']}km ",
        color='blue',
        fill=True,
        fill_color='skyblue'
    ).add_to(m)

m.save('Earthquake_map.html')
print("Transaction complete.")