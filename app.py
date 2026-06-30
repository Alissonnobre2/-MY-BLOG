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
# SESSION STATE (Gerenciamento de Dados Editáveis)
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "ABOUT"  # Iniciando na aba ABOUT que você mostrou na imagem

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False

def go_to(page_name: str):
    st.session_state.page = page_name

# --- Textos Interativos da Aba ABOUT ---
if "about_title" not in st.session_state:
    st.session_state.about_title = "Future Educator, *Language Enthusiast*"
if "about_bio" not in st.session_state:
    st.session_state.about_bio = "Hi, I'm **Maria**! I started this blog to document my English learning journey — from new vocabulary to grammar struggles and small writing wins."
if "about_goals" not in st.session_state:
    st.session_state.about_goals = "Reach an upper-intermediate level by the end of the year\nWrite at least 3 posts a week\nRead one English article every day"
if "about_progress" not in st.session_state:
    st.session_state.about_progress = 35

# --- Dados das Outras Seções ---
if "VOCAB" not in st.session_state:
    st.session_state.VOCAB = [
        {"word": "Breathtaking", "meaning": "Something extremely beautiful or surprising.", "example": "The sunset over the mountains was breathtaking."},
        {"word": "Resilient", "meaning": "Able to recover quickly from difficulties.", "example": "She stayed resilient even after losing her job."},
        {"word": "Overwhelmed", "meaning": "Having too much to deal with at once.", "example": "I felt overwhelmed by all the homework this week."},
    ]

if "GRAMMAR_TIPS" not in st.session_state:
    st.session_state.GRAMMAR_TIPS = [
        {"title": "Present Perfect vs Past Simple", "text": "Use Present Perfect for actions connected to now; use Past Simple for finished actions."},
        {"title": "Articles: A / An / The", "text": "Use 'a/an' for something non-specific. Use 'the' when specific."},
    ]

if "POSTS" not in st.session_state:
    st.session_state.POSTS = [
        {
            "title": "My First Day Writing in English",
            "date": "Day 1",
            "tags": ["Writing", "Beginner"],
            "body": "Welcome to my first blog post! I created this page to practice English every day.\n\n**Today's Goals**\n- Write in English\n- Learn three new words",
            "word_idx": 0,
        }
    ]

if "JOURNEY" not in st.session_state:
    st.session_state.JOURNEY = [
        {
            "icon": "🎓", "status": "Ongoing",
            "title": "Letras: English Language & Literature",
            "subtitle": "Universidade Federal · 2023 – present",
            "items": "Applied Linguistics\nEnglish Literature I & II\nPedagogy of Language Teaching\nAcademic Writing in English",
        },
        {
            "icon": "📖", "status": "120 hours",
            "title": "Teaching Internship — English",
            "subtitle": "Escola Estadual [School Name] · 2025 – 2026",
            "items": "Classroom observation (40h)\nCo-teaching with supervising professor\nLesson planning & curriculum design\nStudent assessment support",
        },
        {
            "icon": "👥", "status": "Active",
            "title": "University Participation",
            "subtitle": "Academic Activities & Projects · 2023 – present",
            "items": "PIBID — Language Teaching Program\nAcademic Writing Workshop\nEnglish Literature Reading Group\nStudent Body Representative",
        },
    ]

# =========================================================
# DESIGN SYSTEM — Estilização do seu Figma
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
section[data-testid="stSidebar"] * {
    color:#EDEFF5 !important;
}
section[data-testid="stSidebar"] input, section[data-testid="stSidebar"] textarea {
    color: var(--navy) !important;
}
section[data-testid="stSidebar"] img{
    border-radius:14px;
    border:3px solid var(--gold);
}
section[data-testid="stSidebar"] hr{
    border-color:rgba(255,255,255,.15);
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

/* Botões de Navegação */
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

.eyebrow{
    display:flex;
    align-items:center;
    gap:10px;
    color:var(--gold);
    font-weight:700;
    font-size:13px;
    letter-spacing:1.5px;
    margin-bottom:14px;
    text-transform: uppercase;
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

/* ---------- Cards ---------- */
.card{
    background:white;
    border:1px solid #ECEEF2;
    border-radius:16px;
    padding:28px;
    box-shadow:0 6px 18px rgba(27,42,74,.05);
    margin-bottom:22px;
    height: 100%;
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
}

.checkline{
    color:var(--muted);
    font-size:14px;
    margin:6px 0;
}
.checkline b{ color:var(--gold); }

.caption-muted{
    color:var(--muted);
    font-size:13px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR / PAINEL DE EDIÇÃO
# =========================================================
with st.sidebar:
    st.session_state.edit_mode = st.toggle("✏️ Edit Page Mode", value=st.session_state.edit_mode)
    st.markdown("---")
    
    if st.session_state.edit_mode:
        st.markdown("### 🛠️ Live Page Editor")
        
        # Editar Informações Principais da aba ABOUT
        if st.session_state.page == "ABOUT":
            with st.expander("👤 Edit Profile & Goals"):
                st.session_state.about_title = st.text_input("Main Heading", st.session_state.about_title)
                st.session_state.about_bio = st.text_area("Biography Text", st.session_state.about_bio)
                st.session_state.about_goals = st.text_area("My Goals (one per line)", st.session_state.about_goals)
                st.session_state.about_progress = st.slider("Fluency Progress %", 0, 100, st.session_state.about_progress)
            
            with st.expander("🎓 Edit Academic Journey Cards"):
                j_titles = [j["title"] for j in st.session_state.JOURNEY]
                sel_j = j_titles.index(st.selectbox("Select Card", j_titles))
                st.session_state.JOURNEY[sel_j]["title"] = st.text_input("Degree/Role", st.session_state.JOURNEY[sel_j]["title"])
                st.session_state.JOURNEY[sel_j]["status"] = st.text_input("Badge (Ongoing/Hours)", st.session_state.JOURNEY[sel_j]["status"])
                st.session_state.JOURNEY[sel_j]["subtitle"] = st.text_input("Institution & Year", st.session_state.JOURNEY[sel_j]["subtitle"])
                st.session_state.JOURNEY[sel_j]["items"] = st.text_area("Bullet Points (one per line)", st.session_state.JOURNEY[sel_j]["items"])

        # Editar Posts e Vocabulários de forma geral
        with st.expander("📝 Manage Blog Posts"):
            if len(st.session_state.POSTS) > 0:
                p_titles = [p["title"] for p in st.session_state.POSTS]
                sel_p = p_titles.index(st.selectbox("Select Post", p_titles))
                st.session_state.POSTS[sel_p]["title"] = st.text_input("Post Title", st.session_state.POSTS[sel_p]["title"])
                st.session_state.POSTS[sel_p]["body"] = st.text_area("Post Content", st.session_state.POSTS[sel_p]["body"])
            if st.button("➕ Add New Post"):
                st.session_state.POSTS.append({"title": "New Writing Entry", "date": "Today", "tags": ["Writing"], "body": "Content...", "word_idx": 0})
                st.rerun()
    else:
        # Layout normal da barra lateral
        st.markdown("## 👩 Profile")
        try:
            st.image("student.jpg", width=220)
        except Exception:
            st.warning("student.jpg profile placeholder")
        st.markdown("---")
        st.caption("Only English Time © 2026")

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
# RENDERIZANDO A PÁGINA SELECIONADA
# =========================================================

# --- ABA: ABOUT (Exatamente o seu layout do Figma) ---
if st.session_state.page == "ABOUT":
    st.markdown('<div class="eyebrow">ABOUT ME</div>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="serif">{st.session_state.about_title}</h1>', unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("student.jpg", use_container_width=True)
        except Exception:
            st.warning("Upload student.jpg to GitHub")
            
    with col2:
        st.markdown(f"<p>{st.session_state.about_bio}</p>", unsafe_allow_html=True)
        st.markdown("**My goals:**")
        
        # Quebra as linhas de metas salvas dinamicamente
        for goal in st.session_state.about_goals.split("\n"):
            if goal.strip():
                st.markdown(f"• {goal}")
                
        st.write("")
        st.progress(st.session_state.about_progress, text="Progress toward fluency goal")

    st.write("")
    st.markdown("---")
    st.markdown('<div class="eyebrow">ACADEMIC JOURNEY</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="serif">Where I Have Been Learning</h2>', unsafe_allow_html=True)
    st.write("")

    # Cards da Jornada Acadêmica
    j_cols = st.columns(3)
    for col, j in zip(j_cols, st.session_state.JOURNEY):
        with col:
            lines = j["items"].split("\n")
            items_html = "".join(f"<div class='checkline'><b>✓</b> {line}</div>" for line in lines if line.strip())
            st.markdown(f"""
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                    <div class="icon-circle" style="margin:0;">{j['icon']}</div>
                    <span class="pill">{j['status']}</span>
                </div>
                <h3 style="margin:0 0 4px 0; font-size:18px;">{j['title']}</h3>
                <p class="caption-muted" style="margin:0 0 16px 0;">{j['subtitle']}</p>
                {items_html}
            </div>
            """, unsafe_allow_html=True)

# --- ABA: HOME ---
elif st.session_state.page == "HOME":
    st.markdown('<h1 class="serif">Welcome to my Feed</h1>', unsafe_allow_html=True)
    if len(st.session_state.POSTS) > 0:
        p = st.session_state.POSTS[0]
        st.markdown(f"### {p['title']}")
        st.write(p["body"])

# --- ABA: VOCABULARY ---
elif st.session_state.page == "VOCABULARY":
    st.markdown('<h2 class="serif">Vocabulary Deck</h2>', unsafe_allow_html=True)
    for v in st.session_state.VOCAB:
        st.info(f"**{v['word']}**: {v['meaning']}  \n*Example:* {v['example']}")

# --- ABA: GRAMMAR ---
elif st.session_state.page == "GRAMMAR":
    st.markdown('<h2 class="serif">Grammar Tips</h2>', unsafe_allow_html=True)
    for g in st.session_state.GRAMMAR_TIPS:
        with st.expander(g["title"]):
            st.write(g["text"])

# --- ABA: WRITING ---
elif st.session_state.page == "WRITING":
    st.markdown('<h2 class="serif">My Complete Writing Notebook</h2>', unsafe_allow_html=True)
    for p in st.session_state.POSTS:
        with st.container(border=True):
            st.subheader(p["title"])
            st.write(p["body"])
