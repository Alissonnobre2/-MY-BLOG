import streamlit as st

# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="Only English Time",
    page_icon="🌻",
    layout="wide",
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* ============================
   Esconde elementos Streamlit
===============================*/

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* ============================
   Página
===============================*/

.block-container{
    max-width:1200px;
    padding-top:2rem;
}

/* ============================
   Sidebar
===============================*/

section[data-testid="stSidebar"]{
    border-right:3px solid #262730;
}

section[data-testid="stSidebar"] img{
    border-radius:50%;
}

/* ============================
   Header
===============================*/

.title{
    text-align:center;
    font-size:60px;
    font-weight:900;
    letter-spacing:5px;
    color:#262730;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#555;
    margin-top:-15px;
    margin-bottom:30px;
}

/* ============================
   Menu
===============================*/

.menu{
    display:flex;
    justify-content:center;
    gap:15px;
    flex-wrap:wrap;
    margin-bottom:40px;
}

.menu-item{

    background:white;

    padding:10px 22px;

    border-radius:30px;

    border:2px solid #262730;

    font-weight:bold;

    transition:0.25s;

}

.menu-item:hover{

    background:#1E88E5;

    color:white;

}

/* ============================
   Cartão do Post
===============================*/

.post{

    background:white;

    padding:35px;

    border-radius:20px;

    box-shadow:0px 8px 20px rgba(0,0,0,.15);

}

.post h2{

    margin-top:0;

}

.word{

    margin-top:30px;

    background:#E3F2FD;

    border-left:8px solid #1E88E5;

    padding:18px;

    border-radius:10px;

}

.caption{

    text-align:center;

    color:gray;

    font-size:14px;

}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    try:
        st.image("student.jpg", use_container_width=True)
    except:
        st.info("📷 Add your image as student.jpg")

    st.markdown("## 👋 About Me")

    st.write("""
Hello!

I'm an English student.

Welcome to my blog.

Here I share:

- 📚 Daily Vocabulary
- ✍ Writing Practice
- 📖 Grammar
- 💡 English Tips
- 🎯 Learning Goals
""")

    st.button("Say Hello 👋", use_container_width=True)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    "<div class='title'>ONLY ENGLISH TIME</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>Blog for sharing my English learning experience</div>",
    unsafe_allow_html=True,
)

st.markdown("""
<div class="menu">

<div class="menu-item">HOME</div>

<div class="menu-item">VOCABULARY</div>

<div class="menu-item">GRAMMAR</div>

<div class="menu-item">WRITING</div>

<div class="menu-item">ABOUT</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# POST
# =========================================================

left,right = st.columns([2.2,1])

with left:

    st.markdown("""

<div class="post">

<h2>📖 My First Day Writing in English</h2>

<p><i>Published Today</i></p>

Welcome to my first blog!

I created this page to practice English every day and share my learning journey.

<h4>Today's Goals</h4>

<ul>

<li>Write in English.</li>

<li>Learn three new words.</li>

<li>Practice grammar.</li>

<li>Read an English article.</li>

</ul>

<div class="word">

<h4>📘 Word of the Day</h4>

<b>Breathtaking</b>

<br><br>

Meaning:

Something extremely beautiful or surprising.

</div>

</div>

""", unsafe_allow_html=True)

with right:

    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=700",
        use_container_width=True,
    )

    st.markdown(
        "<p class='caption'>Learning English every day.</p>",
        unsafe_allow_html=True,
    )

    st.metric("Posts", "01")

    st.metric("Words Learned", "03")

    st.metric("Days Studying", "01")

st.divider()

st.image(
    "imagem.jpg",
    use_container_width=True,
))
