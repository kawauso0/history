import streamlit as st
from moviepy.editor import VideoFileClip

keywords = dict()
keywords["beginning"] = "キーワード: イエス・キリスト"
keywords["development"] = "キーワード: カトリック教会、プロテスタント教会、正教会"
keywords["turn"] = "キーワード: 旧約聖書、新約聖書、初代教会"
keywords["resolution"] = "キーワード: 礼拝、聖書、社会奉仕活動"
image = "./images/tentative_logo_design.jpg"


def generate_video():
    pass

def main_video_page():
    

    left_column, right_column = st.columns([1,6])

    with left_column:
        # 画像を小さくして表示
        st.image(image, caption='Tentative logo', width=100)

    with right_column:
        # HTMLを使用してタイトルとキャプションのフォントサイズを調整
        st.markdown("<h1 style='font-size: 24px;'>One minute to find out anything</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Learn the barrier to entry of any field in one minute.</p>", unsafe_allow_html=True)
    
    
    st.title("検索結果: キリスト教")
    _, container, _ = st.columns([1, 5, 1])
    video_path = "./voicevox/output_with_srt.mp4"
    container.video(video_path)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Beginning", "Development", "Turn", "Resolution"])
    with tab1:
        st.subheader(f"{keywords['beginning']}")
        with open("./voicevox/text/beginning.txt", "r") as f:
            content = f.read()
        st.write(content)
    
    with tab2:
        st.subheader(f"{keywords['development']}")
        with open("./voicevox/text/development.txt", "r") as f:
            content = f.read()
        st.write(content)
    
    with tab3:
        st.subheader(f"{keywords['turn']}")
        with open("./voicevox/text/turn.txt", "r") as f:
            content = f.read()
        st.write(content)
    
    with tab4:
        st.subheader(f"{keywords['resolution']}")
        with open("./voicevox/text/resolution.txt", "r") as f:
            content = f.read()
        st.write(content)

def sub_page():
    # 以下をサイドバーに表示
    left_sidebar_column, right_sidebar_column = st.sidebar.columns([1,4])
    left_sidebar_column.image(image, caption='Tentative logo', use_column_width=True)
    right_sidebar_column.title("One minute to find out anything")
    right_sidebar_column.caption("Learn the barrier to entry of any field in one minute.")
    st.sidebar.write("For each term entered, a one-minute explanatory video of the term is generated.")
    st.sidebar.header("Options")
    WRITING_STYLE = st.sidebar.slider("writing style", 0, 100, 50)
    st.sidebar.caption("0: elementary 100: professional")
    ACCURACY = st.sidebar.slider("accuracy", 0, 100, 50)
    LANGUAGE = st.sidebar.selectbox("language", ("Japanese", "English"))

def webpages():
    main_page()
    sub_page()

webpages()