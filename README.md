
# Movie Recommender System 🎬

This project is a **Movie Recommender System** built using Python and the TMDb dataset. It leverages content-based filtering to suggest similar movies based on features like genre, overview, cast, crew, and keywords.
## Live demo: https://movie-recommendation-system-sourav.streamlit.app/
## 📌 Features

- ✅ Content-Based Filtering using cosine similarity
- ✅ Text feature engineering using TF-IDF and CountVectorizer
- ✅ Movie metadata analysis (cast, crew, genre, etc.)
- ✅ Cleaned and preprocessed TMDb dataset
- ✅ Streamlit Web App
- ✅ Recommends top 5 similar movies based on selected movie

## 🛠️ Tech Stack

- **Python**
- **Pandas**, **NumPy** – Data manipulation
- **Scikit-learn** – TF-IDF, CountVectorizer, Cosine Similarity
- **NLTK** – Text preprocessing
- **TMDb 5000 Movie Dataset** – Movie metadata
- **streamlit** – Movie metadata


## 🚀 How It Works

1. **Data Cleaning:** Combine relevant features (overview, keywords, cast, crew, genres) into a single "tags" column.
2. **Text Vectorization:** Convert tags into numerical vectors using CountVectorizer or TF-IDF.
3. **Similarity Calculation:** Compute cosine similarity between movie vectors.
4. **Recommendation Function:** Given a movie, find the top 5 most similar movies.

## 🧠 Example

If you input the movie **"Iron Man"**, the system might recommend:
- Iron Man 2  
- Iron Man 3  
- Avengers: Age of Ultron  
- Captain America: Civil War  
- The Avengers  

