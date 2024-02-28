import streamlit as st
from PIL import Image
import glob

def generate_video():
    st.write("Generating video...")

def generate_table_of_contents(name):
    # 目次ファイルを読み込み
    path = f"./table_of_contents/{name}.md"
    with open(path, "r") as f:
        lines = f.readlines()
    # 目次の各行に対するボタンを生成
    for i, line in enumerate(lines):
        sectionname = line.replace(" ", "")
        sectionname = sectionname.replace("\n", "")
        sectionname = sectionname.replace("　", "")
        sectionname = sectionname.replace("-", "")
        if st.button(sectionname, key=f"{name}_toc_{i}"):
            # 選択された目次の行をセッション状態に保存
            st.session_state.selected_section = sectionname

# 書籍選択を処理する関数
def select_book(name):
    st.session_state.selected_book = name

def show_section_content(section):
    path = f"./contents/{st.session_state.selected_book}/{section}.md"
    # 選択されたセクションのコンテンツを表示（ここでは仮の実装）
    # HTMLファイルを読み込む
    with open(path, "r") as f:
        content = f.read()

    # HTMLコンテンツをStreamlitアプリに表示する
    st.markdown(content, unsafe_allow_html=True)

# 「前に戻る」ボタンの処理
def go_back():
    st.session_state.selected_book = None
    st.session_state.selected_section = None

# セッション状態の初期化
if 'selected_book' not in st.session_state:
    st.session_state.selected_book = None
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = None

# 書籍が選択されていない場合に書籍リストを表示
if st.session_state.selected_book is None:
    st.title("Digital Books")
    num = 5  
    c = st.container()
    cols = c.columns(num)
    files = glob.glob("./images/digital_books/*")
    digital_books = [Image.open(file) for file in files]
    books_name = [file.split("/")[-1].split(".")[0] for file in files]

    for i, (digital_book, name) in enumerate(zip(digital_books, books_name)):
        digital_book = digital_book.resize((100, 150))
        cols[i % num].image(digital_book, use_column_width=True, caption=name)

        if cols[i % num].button("Select", key=name):
            select_book(name)

# 書籍が選択されている場合に目次と「前に戻る」ボタンを表示
# 目次ページ
elif st.session_state.selected_book is not None and st.session_state.selected_section is None:
    generate_table_of_contents(st.session_state.selected_book)
    if st.button("Go Back"):
        go_back()

# セクション内容ページ
else:
    show_section_content(st.session_state.selected_section)
    if st.button("Go Back to Table of Contents"):
        st.session_state.selected_section = None

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