import streamlit as st
import pickle
import requests

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="MovieFlix",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background:#141414;
}

h1,h2,h3,h4,p{
    color:white;
}

.stButton>button{
    background:#E50914;
    color:white;
    border:none;
    border-radius:8px;
    font-weight:bold;
    height:50px;
    width:100%;
}

.stButton>button:hover{
    background:#ff1f1f;
}

section[data-testid="stSidebar"]{
    background:#0d0d0d;
}

img{
    border-radius:10px;
}

</style>
""",unsafe_allow_html=True)

# ---------------- LOAD DATA ---------------- #

movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

movies_list = movies["title"].values

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🎬 MovieFlix")

st.sidebar.write("Movie Recommendation System")

st.sidebar.markdown("---")

st.sidebar.write("Developer")
st.sidebar.success("Anuj Sharma")

st.sidebar.markdown("---")

st.sidebar.write("Built With")

st.sidebar.write("🐍 Python")
st.sidebar.write("⚡ Streamlit")
st.sidebar.write("🤖 Scikit Learn")
st.sidebar.write("🎬 TMDB API")

# ---------------- HEADER ---------------- #

st.markdown(
"""
<h1 style='text-align:center;color:#E50914;'>
🎬 MOVIEFLIX
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<h4 style='text-align:center;'>
Discover Your Next Favourite Movie
</h4>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- RECOMMEND FUNCTION ---------------- #

def recommend(movie):

    movie_index = movies[movies['title']==movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:6]

    recommended_movies=[]
    recommended_movie_ids=[]

    for i in movie_list:

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        recommended_movie_ids.append(
            movies.iloc[i[0]].movie_id
        )

    return recommended_movies,recommended_movie_ids

# ---------------- SELECT MOVIE ---------------- #

selected_movie = st.selectbox(
    "🍿 Select a Movie",
    movies_list
)

recommend_button = st.button("🔥 Recommend")


# ---------part 2----------------------

api_key = st.secrets["7c3354a1ed24ccce2b06814df86b9569"]

# ----------------part 3------------
# ---------------- POSTER FUNCTION ---------------- #

def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    data = requests.get(url).json()

    poster_path = data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path

    return "https://via.placeholder.com/500x750?text=No+Poster"


# ---------------- RECOMMENDATIONS ---------------- #

if recommend_button:

    with st.spinner("Finding Similar Movies... 🍿"):

        movie_names, movie_ids = recommend(selected_movie)

        posters = []

        for i in range(5):
         posters.append(fetch_poster(movie_ids[i]))

    st.markdown("## 🍿 Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0], use_container_width=True)
        st.markdown(f"**{movie_names[0]}**")

    with col2:
        st.image(posters[1], use_container_width=True)
        st.markdown(f"**{movie_names[1]}**")

    with col3:
        st.image(posters[2], use_container_width=True)
        st.markdown(f"**{movie_names[2]}**")

    with col4:
        st.image(posters[3], use_container_width=True)
        st.markdown(f"**{movie_names[3]}**")

    with col5:
        st.image(posters[4], use_container_width=True)
        st.markdown(f"**{movie_names[4]}**")


# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;color:gray;padding:10px;">
Made with ❤️ by <b>Anuj Sharma</b><br>
Python • Streamlit • Scikit-Learn • TMDB API
</div>
""",
unsafe_allow_html=True
)
