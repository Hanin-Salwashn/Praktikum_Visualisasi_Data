import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

FIG_W = 5
FIG_H = 4

# ===============================
# KONFIGURASI HALAMAN
# ===============================
st.set_page_config(
    page_title="Dashboard Media Sosial Berkelanjutan",
    layout="wide"
)

# ===============================
# STYLE CSS
# ===============================
st.markdown("""
<style>
.main { padding: 1.5rem 2rem; }
.metric-box {
    background-color: #ffffff;
    padding: 1.2rem;
    border-radius: 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    text-align: center;
}
.metric-value { font-size: 28px; font-weight: bold; }
.metric-label { color: #6c757d; }
</style>
""", unsafe_allow_html=True)

# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
    return pd.read_csv("sustainability_social_media_posts.csv")

df = load_data()

# ===============================
# DATA CLEANING
# ===============================
df['post_date'] = pd.to_datetime(df['post_date'], errors='coerce')
df['tahun'] = df['post_date'].dt.year

num_cols = [
    'engagement_likes',
    'engagement_comments',
    'engagement_shares',
    'user_followers'
]

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df[num_cols] = df[num_cols].fillna(0)

# ===============================
# HEADER
# ===============================
st.title("📊 Analisis Tren dan Interaksi Konten Media Sosial Bertema Iklim")

st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")


# ===============================
# FILTER
# ===============================
f1, f2, f3 = st.columns(3)

with f1:
    platform = st.multiselect(
        "Platform",
        df['platform'].unique(),
        df['platform'].unique()
    )

with f2:
    tahun = st.multiselect(
        "Tahun",
        sorted(df['tahun'].dropna().unique()),
        sorted(df['tahun'].dropna().unique())
    )

with f3:
    sentiment = st.multiselect(
        "Sentimen",
        df['post_sentiment'].unique(),
        df['post_sentiment'].unique()
    )

df_f = df[
    (df['platform'].isin(platform)) &
    (df['tahun'].isin(tahun)) &
    (df['post_sentiment'].isin(sentiment))
]

# ===============================
# KPI
# ===============================

k1, k2, k3, k4 = st.columns(4)

k1.markdown(f"<div class='metric-box'><div class='metric-value'>{len(df_f)}</div><div class='metric-label'>Total Postingan</div></div>", unsafe_allow_html=True)
k2.markdown(f"<div class='metric-box'><div class='metric-value'>{int(df_f['engagement_likes'].mean())}</div><div class='metric-label'>Rata-rata Likes</div></div>", unsafe_allow_html=True)
k3.markdown(f"<div class='metric-box'><div class='metric-value'>{int(df_f['engagement_comments'].mean())}</div><div class='metric-label'>Rata-rata Komentar</div></div>", unsafe_allow_html=True)
k4.markdown(f"<div class='metric-box'><div class='metric-value'>{int(df_f['engagement_shares'].mean())}</div><div class='metric-label'>Rata-rata Share</div></div>", unsafe_allow_html=True)

# ===============================
# ANALISIS UTAMA
# ===============================

st.markdown("----------------------------------------------------------------------------------------------")

c1, c2, c3 = st.columns(3)

# ---------- TREN POSTINGAN ----------
with c1:
    fig, ax = plt.subplots(
        figsize=(FIG_W, FIG_H),
        constrained_layout=True
    )

    data_tren = df_f.groupby('tahun').size()
    data_tren.plot(ax=ax)

    ax.set_title("Tren Postingan")
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Jumlah")

    # 🔑 HILANGKAN KOMA DI TAHUN
    ax.set_xticks(data_tren.index)
    ax.set_xticklabels(data_tren.index.astype(int))

    st.pyplot(fig, use_container_width=True)

# ---------- JUMLAH POSTINGAN PER PLATFORM ----------
with c2:
    fig, ax = plt.subplots(
        figsize=(FIG_W, FIG_H),
        constrained_layout=True
    )

    data_pie = df_f['platform'].value_counts()

    ax.pie(
        data_pie,
        labels=data_pie.index,
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
    )

    ax.set_title("Postingan per Platform")

    # 🔑 PENTING: bikin pie benar-benar bulat & tinggi konsisten
    ax.axis('equal')

    st.pyplot(fig, use_container_width=True)
    
# ---------- TOPIK IKLIM TERPOPULER ----------
with c3:
    fig, ax = plt.subplots(
        figsize=(FIG_W, FIG_H),
        constrained_layout=True
    )

    df_f['climate_topic'].value_counts().head(8).plot(
        kind='barh',
        ax=ax
    )

    ax.set_title("Topik Iklim Terpopuler")
    ax.set_xlabel("Jumlah")

    st.pyplot(fig, use_container_width=True)

# ===============================
# DISTRIBUSI INTERAKSI
# ===============================

d1, d2 = st.columns(2)

with d1:
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    corr_data = df_f[
        ['engagement_likes', 'engagement_comments', 'engagement_shares']
    ].corr()

    im = ax.imshow(corr_data, cmap='coolwarm')
    ax.set_title("Heatmap Korelasi Interaksi")
    fig.colorbar(im)
    st.pyplot(fig, use_container_width=True)

with d2:
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.scatter(
        df_f['engagement_likes'],
        df_f['engagement_comments'],
        alpha=0.6
    )
    ax.set_xlabel("Likes")
    ax.set_ylabel("Komentar")
    ax.set_title("Scatter Likes vs Komentar")
    st.pyplot(fig, use_container_width=True)
