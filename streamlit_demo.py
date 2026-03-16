import streamlit as st

st.title("Streamlit 요소 데모")

st.header("텍스트 요소")
st.write("이것은 일반 텍스트입니다.")
st.markdown("**마크다운** 지원")
st.code("print('Hello, Streamlit!')", language="python")

st.header("입력 요소")
name = st.text_input("이름을 입력하세요:")
age = st.number_input("나이를 입력하세요:", min_value=0, max_value=120)
color = st.selectbox("좋아하는 색을 선택하세요:", ["빨강", "파랑", "초록"])
agree = st.checkbox("동의합니다")

st.header("버튼과 상호작용")
if st.button("클릭!"):
    st.success("버튼이 클릭되었습니다.")

st.header("데이터 표시")
st.table({"이름": ["홍길동", "김철수"], "나이": [25, 30]})
st.dataframe({"A": [1, 2, 3], "B": [4, 5, 6]})

st.header("차트")
st.line_chart([1, 2, 3, 4, 5])
st.bar_chart([5, 4, 3, 2, 1])

st.header("파일 업로드")
file = st.file_uploader("파일을 업로드하세요")
if file:
    st.write("업로드된 파일 이름:", file.name)

st.header("슬라이더")
value = st.slider("값을 선택하세요", 0, 100)
st.write("선택한 값:", value)

st.header("이미지 표시")
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")
