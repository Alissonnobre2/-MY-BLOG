import streamlit as st

# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="Only English Time",
    page_icon="🌻",
    layout="wide"
)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

/* Esconde elementos do Streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Área principal */
.block-container{
    max-width:1100px;
    padding-top:2rem;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    border-right:2px solid #262730;
}

/* Título */

.title{
    text-align:center;
    font-size:58px;
    font-weight:800;
    letter-spacing:4px;
    color:#262730;
    margin-bottom:0;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#555;
    margin-top:-15px;
    margin-bottom:30px;
}

/* Menu */

.menu{
    display:flex;
    justify-content:center;
    gap:18px;
    margin-bottom:35px;
}

.item{
    background:white;
    padding:10px 22px;
    border-radius:30px;
    border:2px solid #262730;
    font-weight:bold;
    transition:0.3s;
}

.item:hover{
    background:#1E88E5;
    color:white;
}

/* Card do post */

.post{
    background:white;
    padding:35px;
    border-radius:18px;
    box-shadow:0px 4px 12px rgba(0,0,0,.10);
}

.post-title{
    font-size:36px;
    font-weight:bold;
    color:#262730;
}

.word{
    background:#E3F2FD;
    border-left:6px solid #1E88E5;
    padding:15px;
    border-radius:8px;
    margin-top:25px;
}

.caption{
    text-align:center;
    color:gray;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    try:
        st.image("student.jpg", use_container_width=True)
    except:
        st.info("📷 Add **student.jpg** to your project.")

    st.markdown("## About Me")

    st.write("""
Hello!

I'm an English student passionate about learning English.

Here I share:

- 📚 Daily vocabulary
- ✍️ Writing practice
- 📖 Grammar
- 💡 English tips
""")

    st.button("Say Hello 👋", use_container_width=True)

# ==========================================================
# CABEÇALHO
# ==========================================================

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

# ==========================================================
# CONTEÚDO
# ==========================================================

col1, col2 = st.columns([2.3,1])

with col1:

    st.markdown("""
<div class="post">

<div class="post-title">
📖 My First Day Writing in English
</div>

<br>

Welcome to my first blog!

I created this page to practice English every day and share my progress.

<h4>Today's Goals</h4>

<ul>
<li>Write in English.</li>
<li>Learn three new words.</li>
<li>Practice grammar.</li>
<li>Never be afraid of making mistakes.</li>
</ul>

<div class="word">

<b>📘 Word of the Day</b><br><br>

<b>Breathtaking</b><br>

Meaning: Something extremely beautiful or surprising.

</div>

</div>

""", unsafe_allow_html=True)

with col2:

    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=700",
        use_container_width=True
    )

    st.markdown(
        "<p class='caption'>This image represents my English learning journey.</p>",
        unsafe_allow_html=True
    )

    st.button("Read More", use_container_width=True)

st.divider()

st.markdown(
    "<center><h4>🌻 Let's learn together!</h4></center>",
    unsafe_allow_html=True
)
