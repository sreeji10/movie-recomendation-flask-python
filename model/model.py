import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title.str.lower() == title.lower()]["index"].values[0]

def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print ("Error:", row	)

def check_movie(title):
    if title in all_movies:
        return True
    return False

def get_recommendations(title, n):
    names = []
    movie_user_likes = title
    movie_index = get_index_from_title(movie_user_likes)
    similar_movies =  list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

    for element in sorted_similar_movies[1:n+1]:
        names.append(get_title_from_index(element[0]))
    return names


df = pd.read_csv("./data/movie_dataset.csv")
features = ['keywords','cast','genres','director']
all_movies = df.original_title.str.lower().tolist()

for feature in features:
	df[feature] = df[feature].fillna('')

df["combined_features"] = df.apply(combine_features,axis=1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix) 

