import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#load datasets
df = pd.read_csv("../data/netflix_titles.csv")

print("DataSet Shape",df.shape)
print(df.head())

#data cleaning

df['date_added'] = pd.to_datetime(df['date_added'],errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['country'].fillna("Unknown" ,inplace=True)


#graph Movies and tv

plt.figure()
sns.countplot(x="type",data=df)
plt.title("Movies Vs Tv shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()


# -----------------------------

# GRAPH 2: Top 10 Countries

# -----------------------------

 

plt.figure()

 

top_country = df['country'].value_counts().head(10)

 

top_country.plot(kind='bar')

 

plt.title("Top 10 Countries Producing Netflix Content")

plt.xlabel("Country")

plt.ylabel("Count")

plt.xticks(rotation=45)

 

plt.show()




# -----------------------------

# GRAPH 3: Content Added Per Year

# -----------------------------

 

plt.figure()

 

sns.countplot(x='year_added', data=df)

 

plt.title("Netflix Content Added Per Year")

 

plt.xticks(rotation=90)

 

plt.show()



# -----------------------------

# GRAPH 4: Ratings Distribution

# -----------------------------

 

plt.figure()

 

sns.countplot(y='rating', data=df,

order=df['rating'].value_counts().index)

 

plt.title("Distribution of Ratings")

 

plt.show()




# -----------------------------

# GRAPH 5: Top Genres

# -----------------------------

 

plt.figure()

 

genres = df['listed_in'].str.split(',', expand=True).stack()

 

genres.value_counts().head(10).plot(kind='bar')

 

plt.title("Top 10 Genres on Netflix")

 

plt.xlabel("Genre")

 

plt.ylabel("Count")

 

plt.xticks(rotation=45)

 

plt.show()





