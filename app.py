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
# SESSION STATE
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "HOME"

def go_to(page_name: str):
    st.session_state.page = page_name

# =========================================================
# DESIGN SYSTEM — navy & gold
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Inter:wght@400;500;600;700&display=swap');

:root{
    --navy:#1B2A4A;
    --navy-light:#27406e;
    --gold:#D9A441;
    --gold-light:#F8EFD9;
    --bg:#F7F8FA;
    --text:#1B2A4A;
    --muted:#6B7280;
}

html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
    color:var(--text);
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background:var(--bg);
}

.block-container{
    max-width:1180px;
    padding-top:1.2rem;
}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"]{
    background:var(--navy);
    border-right:none;
}
section[data-testid="stSidebar"] *{
    color:#EDEFF5 !important;
}
section[data-testid="stSidebar"] img{
    border-radius:14px;
    border:3px solid var(--gold);
}
section[data-testid="stSidebar"] hr{
    border-color:rgba(255,255,255,.15);
}
section[data-testid="stSidebar"] button{
    background:var(--gold) !important;
    color:var(--navy) !important;
    border:none !important;
    font-weight:700 !important;
    border-radius:30px !important;
}

/* ---------- Navbar ---------- */
.navbar{
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:14px 6px 22px 6px;
    border-bottom:1px solid #E5E7EB;
    margin-bottom:30px;
}
.navbar .brand{
    display:flex;
    align-items:center;
    gap:10px;
    font-family:'Playfair Display', serif;
    font-weight:700;
    font-size:20px;
    color:var(--navy);
}
.navbar .brand-icon{
    background:var(--gold);
    color:var(--navy);
    width:34px;
    height:34px;
    border-radius:9px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:18px;
}
.navbar .badge{
    background:var(--gold-light);
    color:#8A6A1E;
    border:1px solid #F0DBA0;
    padding:6px 16px;
    border-radius:30px;
    font-size:13px;
    font-weight:600;
}

/* Functional nav buttons row */
div[data-testid="stHorizontalBlock"] button{
    background:transparent !important;
    border:none !important;
    color:var(--navy) !important;
    font-weight:600 !important;
    font-size:15px !important;
    box-shadow:none !important;
}
div[data-testid="stHorizontalBlock"] button:hover{
    color:var(--gold) !important;
}

/* ---------- Eyebrow / section labels ---------- */
.eyebrow{
    display:flex;
    align-items:center;
    gap:10px;
    color:var(--gold);
    font-weight:700;
    font-size:13px;
    letter-spacing:1.5px;
    margin-bottom:14px;
}
.eyebrow::before{
    content:"";
    width:24px;
    height:2px;
    background:var(--gold);
    display:inline-block;
}

h1.serif, h2.serif{
    font-family:'Playfair Display', serif;
    color:var(--navy);
    font-weight:700;
    line-height:1.15;
}

/* ---------- Stat cards ---------- */
.stat-card{
    background:var(--gold-light);
    border:1px solid #F0DBA0;
    border-left:5px solid var(--gold);
    border-radius:14px;
    padding:18px 20px;
}
.stat-card .stat-icon{
    font-size:20px;
    margin-bottom:8px;
}
.stat-card .stat-number{
    font-family:'Playfair Display', serif;
    font-size:26px;
    font-weight:700;
    color:var(--navy);
}
.stat-card .stat-label{
    color:#8A6A1E;
    font-size:13px;
}

/* ---------- Generic content card ---------- */
.card{
    background:white;
    border:1px solid #ECEEF2;
    border-radius:16px;
    padding:28px;
    box-shadow:0 6px 18px rgba(27,42,74,.05);
    margin-bottom:22px;
}
.card h2, .card h3{
    font-family:'Playfair Display', serif;
    color:var(--navy);
}

.icon-circle{
    width:42px;
    height:42px;
    border-radius:10px;
    background:var(--navy);
    color:var(--gold);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:18px;
    margin-bottom:14px;
}

.pill{
    display:inline-block;
    background:var(--gold-light);
    color:#8A6A1E;
    border:1px solid #F0DBA0;
    padding:4px 14px;
    border-radius:30px;
    font-size:12px;
    font-weight:700;
    margin-right:6px;
}

.checkline{
    color:var(--muted);
    font-size:14px;
    margin:4px 0;
}
.checkline b{ color:var(--gold); }

.word-box{
    margin-top:24px;
    background:var(--navy);
    color:white;
    border-left:6px solid var(--gold);
    padding:20px;
    border-radius:12px;
}
.word-box h4{ color:var(--gold); margin-top:0; }

.caption-muted{
    text-align:center;
    color:var(--muted);
    font-size:13px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA
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
        "title": "My First Day Writing in English",
        "date": "Day 1",
        "tags": ["Writing", "Beginner"],
        "body": """Welcome to my first blog post! I created this page to practice English every day and share my learning journey.

**Today's Goals**
- Write in English
- Learn three new words
- Practice grammar
- Read an English article""",
        "word_of_day": VOCAB[0],
    },
    {
        "title": "Talking About My Weekend",
        "date": "Day 5",
        "tags": ["Writing", "Speaking"],
        "body": """This week I tried to describe my weekend out loud in English before writing it down. It's harder than it looks!

I went to the park, read a book, and called my sister. Small sentences, but real practice.""",
        "word_of_day": VOCAB[1],
    },
    {
        "title": "Grammar Struggles: Present Perfect",
        "date": "Day 9",
        "tags": ["Grammar"],
        "body": """I keep mixing up Present Perfect and Past Simple. Today I studied the difference and wrote ten example sentences to fix it in my memory.""",
        "word_of_day": VOCAB[2],
    },
]

JOURNEY = [
    {
        "icon": "🎓", "status": "Ongoing",
        "title": "Letras: English Language & Literature",
        "subtitle": "Universidade Federal · 2023 – present",
        "items": ["Applied Linguistics", "English Literature I & II", "Pedagogy of Language Teaching", "Academic Writing in English"],
    },
    {
        "icon": "📖", "status": "120 hours",
        "title": "Teaching Internship — English",
        "subtitle": "Escola Estadual [School Name] · 2025 – 2026",
        "items": ["Classroom observation (40h)", "Co-teaching with supervising professor", "Lesson planning & curriculum design", "Student assessment support"],
    },
    {
        "icon": "👥", "status": "Active",
        "title": "University Participation",
        "subtitle": "Academic Activities & Projects · 2023 – present",
        "items": ["PIBID — Language Teaching Program", "Academic Writing Workshop", "English Literature Reading Group", "Student Body Representative"],
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
# NAVBAR
# =========================================================
st.markdown("""
<div class="navbar">
    <div class="brand"><span class="brand-icon">🌻</span> Only English Time</div>
    <div class="badge">Letras · English · 2026</div>
</div>
""", unsafe_allow_html=True)

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

    st.markdown('<div class="eyebrow">ABOUT ME</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="serif">Future Educator, <i>Language Enthusiast</i></h1>', unsafe_allow_html=True)
    st.write(
        "I am an undergraduate student in English Language and Literature, currently documenting my "
        "learning journey — the classrooms I have observed, the words I have learned, and the reflections "
        "that continue to shape my understanding of what it truly means to learn (and teach) a language."
    )

    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown(f"""<div class="stat-card"><div class="stat-icon">📚</div>
        <div class="stat-number">{len(POSTS)}</div><div class="stat-label">Blog Posts</div></div>""", unsafe_allow_html=True)
    with s2:
        st.markdown(f"""<div class="stat-card"><div class="stat-icon">📘</div>
        <div class="stat-number">{len(VOCAB)}</div><div class="stat-label">Words Learned</div></div>""", unsafe_allow_html=True)
    with s3:
        st.markdown("""<div class="stat-card"><div class="stat-icon">🗓️</div>
        <div class="stat-number">09</div><div class="stat-label">Days Studying</div></div>""", unsafe_allow_html=True)

    st.write("")
    left, right = st.columns([2.2, 1])

    with left:
        post = POSTS[0]
        tags_html = "".join(f"<span class='pill'>{t}</span>" for t in post["tags"])
        body_html = post["body"].replace("\n", "<br>")
        st.markdown(f"""
        <div class="card">
            <h2>{post['title']}</h2>
            <p class="caption-muted" style="text-align:left;">Published — {post['date']}</p>
            {tags_html}
            <p>{body_html}</p>
            <div class="word-box">
                <h4>📘 Word of the Day</h4>
                <b>{post['word_of_day']['word']}</b><br><br>
                Meaning: {post['word_of_day']['meaning']}<br>
                <i>Example: {post['word_of_day']['example']}</i>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="eyebrow">RECENT POSTS</div>', unsafe_allow_html=True)
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
        st.markdown("<p class='caption-muted'>Learning English every day.</p>", unsafe_allow_html=True)

    st.divider()
    st.markdown('<div class="eyebrow">ACADEMIC JOURNEY</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="serif">Where I Have Been Learning</h2>', unsafe_allow_html=True)

    j1, j2, j3 = st.columns(3)
    for col, j in zip([j1, j2, j3], JOURNEY):
        with col:
            items_html = "".join(f"<div class='checkline'><b>✓</b> {i}</div>" for i in j["items"])
            st.markdown(f"""
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div class="icon-circle">{j['icon']}</div>
                    <span class="pill">{j['status']}</span>
                </div>
                <h3 style="margin-bottom:0;">{j['title']}</h3>
                <p class="caption-muted" style="text-align:left; margin-top:2px;">{j['subtitle']}</p>
                {items_html}
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# PAGE: VOCABULARY
# =========================================================
elif st.session_state.page == "VOCABULARY":
    st.markdown('<div class="eyebrow">VOCABULARY</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="serif">Words I\'ve Learned</h2>', unsafe_allow_html=True)
    for v in VOCAB:
        st.markdown(f"""
        <div class="card">
            <div class="icon-circle">📘</div>
            <h3>{v['word']}</h3>
            <p><b>Meaning:</b> {v['meaning']}</p>
            <p><i>Example: {v['example']}</i></p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PAGE: GRAMMAR
# =========================================================
elif st.session_state.page == "GRAMMAR":
    st.markdown('<div class="eyebrow">GRAMMAR</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="serif">Grammar Tips</h2>', unsafe_allow_html=True)
    for g in GRAMMAR_TIPS:
        with st.expander(g["title"]):
            st.write(g["text"])

# =========================================================
# PAGE: WRITING
# =========================================================
elif st.session_state.page == "WRITING":
    st.markdown('<div class="eyebrow">WRITING</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="serif">My Writing Practice</h2>', unsafe_allow_html=True)
    for p in POSTS:
        tags_html = "".join(f"<span class='pill'>{t}</span>" for t in p["tags"])
        body_html = p["body"].replace("\n", "<br>")
        st.markdown(f"""
        <div class="card">
            <h2>{p['title']}</h2>
            <p class="caption-muted" style="text-align:left;">Published — {p['date']}</p>
            {tags_html}
            <p>{body_html}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PAGE: ABOUT
# =========================================================
elif st.session_state.page == "ABOUT":
    st.markdown('<div class="eyebrow">ABOUT ME</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="serif">Future Educator, <i>Language Enthusiast</i></h2>', unsafe_allow_html=True)

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

    st.write("")
    st.markdown('<div class="eyebrow">ACADEMIC JOURNEY</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="serif">Where I Have Been Learning</h2>', unsafe_allow_html=True)

    j1, j2, j3 = st.columns(3)
    for col, j in zip([j1, j2, j3], JOURNEY):
        with col:
            items_html = "".join(f"<div class='checkline'><b>✓</b> {i}</div>" for i in j["items"])
            st.markdown(f"""
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div class="icon-circle">{j['icon']}</div>
                    <span class="pill">{j['status']}</span>
                </div>
                <h3 style="margin-bottom:0;">{j['title']}</h3>
                <p class="caption-muted" style="text-align:left; margin-top:2px;">{j['subtitle']}</p>
                {items_html}
            </div>
            """, unsafe_allow_html=True)
