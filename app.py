import streamlit as st

st.set_page_config(
    page_title="Only English Time",
    page_icon="🌻",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    max-width:1100px;
}

/* Remove espaços */
section.main > div{
    padding-top:1rem;
}

/* Título */

.title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    letter-spacing:4px;
}

.subtitle{
    text-align:center;
    font-size:22px;
    margin-top:-20px;
    color:#444;
}

/* Menu */

.menu{
    display:flex;
    justify-content:center;
    gap:20px;
    margin-top:25px;
    margin-bottom:40px;
}

.item{
    background:white;
    padding:8px 20px;
    border-radius:30px;
    border:2px solid black;
    font-weight:bold;
}

/* Post */

.post-title{
    font-size:35px;
    font-weight:bold;
}

.post{
    background:white;
    padding:30px;
    border-radius:15px;
}

.word{
    background:#E3F2FD;
    padding:15px;
    border-radius:10px;
    margin-top:20px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    border-right:3px solid black;
}

</style>

""", unsafe_allow_html=True)

# ---------------- Sidebar ----------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=130
    )

    st.markdown("## About Me")

    st.write("""
Hello!

I'm an English student.

Here I share:

- Daily vocabulary
- Grammar
- Writing practice
- English tips
""")

# ---------------- Cabeçalho ----------------

st.markdown(
    "<div class='title'>ONLY ENGLISH TIME</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Blog for sharing my English learning experience</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div class="menu">

<div class="item">CREED</div>

<div class="item">REPORT</div>

<div class="item">LESSON</div>

<div class="item">INTERVIEW</div>

</div>
""", unsafe_allow_html=True)

# ---------------- Conteúdo ----------------

col1,col2 = st.columns([2,1])

with col1:

    st.markdown("""
<div class="post">

<div class="post-title">

📖 My First Day Writing in English

</div>

<br>

Welcome to my first blog!

I created this page to practice English every day and share my progress.

### Today's goals

- Write in English.
- Learn three new words.
- Practice grammar.

<div class="word">

<b>Word of the Day</b>

<b>Breathtaking</b>

Meaning:
Something extremely beautiful or surprising.

</div>

</div>

""", unsafe_allow_html=True)

with col2:

    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
        use_container_width=True
    )

    st.write("This image represents my English learning journey.")

hide = """
<style>

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

</style>
"""

st.markdown(hide, unsafe_allow_html=True)
