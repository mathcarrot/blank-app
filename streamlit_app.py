import streamlit as st

# CSS로 디자인 수정: 배경색, 헤더 크기 조정
st.markdown("""
<style>
body {
    background-color: #f0f8ff;  /* 연한 파란색 배경 */
    font-family: Arial, sans-serif;
}
.stApp {
    max-width: 1300px;
    margin: 0 auto;
}
h1, h2, h3 {
    color: #333;
    font-size: 0.9em;  /* 헤더 글자 크기 더 줄임 */
}
</style>
""", unsafe_allow_html=True)

st.title("자기 소개")

st.header("강경민")

st.markdown("**이름:** 강경민")
st.markdown("**나이:** 28살")
st.markdown("**학년:** 3학년")
st.markdown("**전공:** 수학교육과")
st.markdown("**학교:** 인천대학교")

st.header("취미와 관심사")
st.write("취미는 수학 문제 풀기와 프로그래밍입니다.")
st.write("관심사는 교육 기술과 인공지능입니다.")

st.header("성격과 장점")
st.write("성격은 긍정적이고 열정적입니다.")
st.write("장점은 끈기와 문제 해결 능력입니다.")

st.header("목표와 꿈")
st.write("목표는 수학교사가 되는 것입니다.")
st.write("꿈은 학생들에게 수학의 재미를 가르치는 것입니다.")

st.header("미래 계획")
st.write("미래에는 교육 분야에서 혁신을 이루고 싶습니다.")
st.write("더 많은 사람들에게 수학 교육의 중요성을 알리고 싶습니다.")

st.header("추가 정보")
st.write("저는 열정적인 학습자이며, 새로운 기술을 배우는 것을 좋아합니다.")
st.write("팀 프로젝트와 협업을 즐깁니다.")

