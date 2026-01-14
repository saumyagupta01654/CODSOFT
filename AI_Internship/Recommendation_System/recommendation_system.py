import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- SAMPLE DATASET ----------------
data = {
    'title': [
        'The Avengers',
        'Iron Man',
        'Captain America',
        'Thor',
        'Batman Begins',
        'The Dark Knight',
        'Man of Steel',
        'Interstellar',
        'Inception',
        'The Matrix'
    ],
    'description': [
        'superhero action team save world',
        'genius billionaire superhero suit',
        'soldier superhero patriot war',
        'god thunder superhero hammer',
        'dark superhero justice city',
        'dark knight joker chaos',
        'alien superhero earth power',
        'space time future science',
        'dream mind reality',
        'virtual reality future human'
    ]
}

df = pd.DataFrame(data)

# ---------------- TF-IDF VECTORIZATION ----------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['description'])

# ---------------- COSINE SIMILARITY ----------------
cosine_sim = cosine_similarity(tfidf_matrix)

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie_title):
    if movie_title not in df['title'].values:
        return "Movie not found in database."

    index = df[df['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(cosine_sim[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in similarity_scores[1:6]:
        recommendations.append(df.iloc[i[0]]['title'])

    return recommendations

# ---------------- USER INPUT ----------------
print("🎬 Movie Recommendation System")
movie = input("Enter a movie name: ")

results = recommend(movie)

print("\nRecommended Movies:")
if isinstance(results, list):
    for r in results:
        print("✔", r)
else:
    print(results)
