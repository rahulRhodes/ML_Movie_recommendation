# ML_Movie_recommendation

🎬 Movie Recommendation System

A machine learning–based movie recommendation system that suggests similar movies based on content similarity. This project uses NLP techniques and cosine similarity to provide personalized recommendations through a simple web interface built with Streamlit.

🚀 Features

Content-based movie recommendations

Text vectorization using CountVectorizer

Cosine similarity for matching similar movies

Interactive UI built using Streamlit

Fast and accurate movie suggestions

🛠️ Tech Stack

Python

Pandas, NumPy

Scikit-learn

NLTK

Streamlit

📂 Project Structure
ML_Movie_recommendation/
│
├── app.py
├── movies_dict1.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
├── README.md

⚙️ How It Works

Movie data is cleaned and preprocessed

Important text features (overview, genres, keywords, cast, crew) are combined

Text is converted to vectors using CountVectorizer

Cosine similarity is calculated between all movies

Based on a selected movie, the system returns top 5 similar recommendations

▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/rahulRhodes/ML_Movie_recommendation.git
cd ML_Movie_recommendation

2. Create virtual environment
python3 -m venv movie_env
source movie_env/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run app.py


Then open the local URL shown in your terminal.

📊 Dataset

This project uses the TMDB 5000 Movies dataset.

⚠️ Dataset and trained model files are not included in the repository due to GitHub file size limits.
