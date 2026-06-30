import streamlit as st

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Only English Time",
    page_icon="🌻",
    layout="wide",
)

# =========================================================
# SESSION STATE (controls which page is active)
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "HOME"

def go_to(page_name: str):
    st.session_state.page = page_name

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
/* Hide default Streamlit chrome */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    max-width:1200px;
    padding-top:2rem;
}

section[data-testid="stSidebar"]{
    border-right:3px solid #262730;
}
section[data-testid="stSidebar"] img{
    border-radius:50%;
}

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

/* Menu buttons get styled like pills via the stButton wrapper */
div[data-testid="stHorizontalBlock"] button{
    border-radius:30px !important;
    border:2px solid #262730 !important;
    font-weight:bold !important;
    background:white !important;
    color:#262730 !important;
    transition:0.25s !important;
}
div[data-testid="stHorizontalBlock"] button:hover{
    background:#1E88E5 !important;
    color:white !important;
    border-color:#1E88E5 !important;
}

.post{
    background:white;
    padding:35px;
    border-radius:20px;
    box-shadow:0px 8px 20px rgba(0,0,0,.15);
    margin-bottom:25px;
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

.tag{
    display:inline-block;
    background:#FFF3CD;
    color:#856404;
    padding:3px 12px;
    border-radius:20px;
    font-size:13px;
    font-weight:bold;
    margin-right:6px;
}

.caption{
    text-align:center;
    color:gray;
    font-size:14px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA — vocabulary, grammar tips, writing posts
# =========================================================
VOCAB = [
    {"word": "Breathtaking", "meaning": "Something extremely beautiful or surprising.", "example": "The sunset over the mountains was breathtaking."},
    {"word": "Resilient", "meaning": "Able to recover quickly from difficulties.", "example": "She stayed resilient even after losing her job."},
    {"word": "Overwhelmed", "meaning": "Having too much to deal with at once.", "example": "I felt overwhelmed by all the homework this week."},
]

GRAMMAR_TIPS = [
    {"title": "Present Perfect vs Past Simple", "text": "Use Present Perfect for actions connected to now ('I have studied English for 2 years'); use Past Simple for finished actions with a specific time ('I studied English in 2022')."},
    {"title": "Articles: A / An / The", "text": "Use 'a/an' for something not specific or mentioned for the first time. Use 'the' when both speaker and listener know exactly what is being referred to."},
    {"title": "Common mistake: Make vs Do", "text": "'Make' is for creating something (make a cake, make a decision). 'Do' is for activities/tasks (do homework, do exercise)."},
]

POSTS = [
    {
        "title": "📖 My First Day Writing in English",
        "date": "Day 1",
        "tags": ["Writing", "Beginner"],
        "body": """
Welcome to my first blog post! I created this page to practice English every day and share my learning journey.

**Today's Goals**
- Write in English
- Learn three new words
- Practice grammar
- Read an English article
""",
        "word_of_day": VOCAB[0],
    },
    {
        "title": "🗣️ Talking About My Weekend",
        "date": "Day 5",
        "tags": ["Writing", "Speaking"],
        "body": """
This week I tried to describe my weekend out loud in English before writing it down. It's harder than it looks!

I went to the park, read a book, and called my sister. Small sentences, but real practice.
""",
        "word_of_day": VOCAB[1],
    },
    {
        "title": "📝 Grammar Struggles: Present Perfect",
        "date": "Day 9",
        "tags": ["Grammar"],
        "body": """
I keep mixing up Present Perfect and Past Simple. Today I studied the difference and wrote ten example sentences to fix it in my memory.
""",
        "word_of_day": VOCAB[2],
    },
]

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown("## 👩 About Me")
    try:
        st.image("student.jpg", width=220)
    except Exception:
        st.warning("Add the file student.jpg")

    st.markdown("---")
    st.write("""
Hello! 👋  
My name is Maria. I'm an English student and this blog is where I document my learning journey.

**Here you'll find:**  
📚 Daily Vocabulary  
✍️ Writing Practice  
📖 Grammar Tips  
💡 English Expressions  
🎯 Study Goals  
🌎 My Progress
""")
    st.button("🌻 Follow My Journey", use_container_width=True)

# =========================================================
# HEADER
# =========================================================
st.markdown("<div class='title'>ONLY ENGLISH TIME</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Blog for sharing my English learning experience</div>",
    unsafe_allow_html=True,
)

# =========================================================
# REAL NAVIGATION MENU (functional buttons)
# =========================================================
menu_cols = st.columns(5)
menu_items = ["HOME", "VOCABULARY", "GRAMMAR", "WRITING", "ABOUT"]
for col, item in zip(menu_cols, menu_items):
    with col:
        st.button(item, use_container_width=True, on_click=go_to, args=(item,))

st.write("")

# =========================================================
# PAGE: HOME
# =========================================================
if st.session_state.page == "HOME":
    left, right = st.columns([2.2, 1])

    with left:
        post = POSTS[0]
        tags_html = "".join(f"<span class='tag'>{t}</span>" for t in post["tags"])
        st.markdown(f"""
        <div class="post">
            <h2>{post['title']}</h2>
            <p><i>Published — {post['date']}</i></p>
            {tags_html}
            <p>{post['body']}</p>
            <div class="word">
                <h4>📘 Word of the Day</h4>
                <b>{post['word_of_day']['word']}</b><br><br>
                Meaning: {post['word_of_day']['meaning']}<br>
                <i>Example: {post['word_of_day']['example']}</i>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Recent Posts")
        for p in POSTS[1:]:
            with st.container(border=True):
                st.markdown(f"**{p['title']}**  \n*{p['date']}*")
                st.caption(p["body"].strip().split("\n")[0])
                if st.button("Read more →", key=f"read_{p['title']}"):
                    go_to("WRITING")
                    st.rerun()

    with right:
        st.image(
            "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=700",
            use_container_width=True,
        )
        st.markdown("<p class='caption'>Learning English every day.</p>", unsafe_allow_html=True)
        st.metric("Posts", str(len(POSTS)))
        st.metric("Words Learned", str(len(VOCAB)))
        st.metric("Days Studying", "09")

    st.divider()
    st.markdown("<center><h3>🌻 Let's Learn Together!</h3></center>", unsafe_allow_html=True)

# =========================================================
# PAGE: VOCABULARY
# =========================================================
elif st.session_state.page == "VOCABULARY":
    st.markdown("## 📚 Vocabulary List")
    for v in VOCAB:
        with st.container(border=True):
            st.markdown(f"### {v['word']}")
            st.write(f"**Meaning:** {v['meaning']}")
            st.write(f"*Example:* {v['example']}")

# =========================================================
# PAGE: GRAMMAR
# =========================================================
elif st.session_state.page == "GRAMMAR":
    st.markdown("## 📖 Grammar Tips")
    for g in GRAMMAR_TIPS:
        with st.expander(g["title"]):
            st.write(g["text"])

# =========================================================
# PAGE: WRITING
# =========================================================
elif st.session_state.page == "WRITING":
    st.markdown("## ✍️ My Writing Practice")
    for p in POSTS:
        tags_html = "".join(f"<span class='tag'>{t}</span>" for t in p["tags"])
        st.markdown(f"""
        <div class="post">
            <h2>{p['title']}</h2>
            <p><i>Published — {p['date']}</i></p>
            {tags_html}
            <p>{p['body']}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PAGE: ABOUT
# =========================================================
elif st.session_state.page == "ABOUT":
    st.markdown("## 👩 About Me")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("student.jpg", width=250)
        except Exception:
            st.warning("Add the file student.jpg")
    with col2:
        st.write("""
        Hi, I'm **Maria**! I started this blog to document my English learning journey —
        from new vocabulary to grammar struggles and small writing wins.

        **My goals:**
        - Reach an upper-intermediate level by the end of the year
        - Write at least 3 posts a week
        - Read one English article every day
        """)
        st.progress(35, text="Progress toward fluency goal")
