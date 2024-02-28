import streamlit as st
from PIL import Image

# 画像を表示
image = Image.open("./images/tentative_logo_design.jpg")

keywords = dict()
keywords["beginning"] = "キーワード: イエス・キリスト"
keywords["development"] = "キーワード: カトリック教会、プロテスタント教会、正教会"
keywords["turn"] = "キーワード: 旧約聖書、新約聖書、初代教会"
keywords["resolution"] = "キーワード: 礼拝、聖書、社会奉仕活動"
image = "./images/tentative_logo_design.jpg"

def generate_video():
    pass
    
def main_page():
    # 以下をメインページに表示
    left_column, right_column = st.columns([2,5])
    left_column.image(image, caption='Tentative logo', width=200)
    right_column.title("One minute to find out anything")
    right_column.caption("Learn the barrier to entry of any field in one minute.")
    
    st.write("")
    st.write("")
    txt = st.text_area(
        "Text to analyze",
        "Please enter a term you would like to know more about.",
        )

    st.write(f'You wrote {len(txt)} characters.')
    if st.button("Generate"):
        st.session_state["page"] = "video"
    


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
    video_path = "./voicevox/result/output_with_srt.mp4"
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
    
    if st.button("Go Back"):
        st.session_state["page"] = "main"

def sub_video_page():
    # 以下をサイドバーに表示
    image = Image.open("./images/tentative_logo_design.jpg")
    left_column, right_column = st.sidebar.columns([1,4])
    left_column.image(image, caption='Tentative logo', use_column_width=True)
    right_column.title("One minute to find out anything")
    right_column.caption("Learn the barrier to entry of any field in one minute.")
    st.sidebar.write("For each term entered, a one-minute explanatory video of the term is generated.")

    tab1, tab2 = st.sidebar.tabs(["Options", "Generation"])
    image = Image.open("./images/tentative_logo_design.jpg")
    with tab1:
        tab1.header("Options")
        WRITING_STYLE = tab1.slider("writing style", 0, 100, 50)
        tab1.caption("0: elementary 100: professional")
        ACCURACY = tab1.slider("accuracy", 0, 100, 50)
        LANGUAGE = tab1.selectbox("language", ("Japanese", "English"))


    with tab2:

        tab2.write("")
        tab2.write("")
        txt = tab2.text_area(
            "Text to analyze",
            "Please enter a term you would like to know more about.",
            )

        tab2.write(f'You wrote {len(txt)} characters.')

        BUTTON = st.button("Generate video", on_click=generate_video)

def webpages():
    main_page()
    sub_page()

def video_webpages():
    main_video_page()
    sub_video_page()
    
# セッション状態の初期化
if "page" not in st.session_state:
    st.session_state["page"] = "main"

# 現在のページに基づいて表示を切り替え
if st.session_state["page"] == "main":
    webpages()
elif st.session_state["page"] == "video":
    video_webpages()
