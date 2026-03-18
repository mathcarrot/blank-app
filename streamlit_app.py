import streamlit as st

st.title("자기 소개")

st.header("기본 정보 입력")

name = st.text_input("이름:", "강경민")
age = st.number_input("나이:", min_value=1, max_value=100, value=28)
grade = st.selectbox("학년", ["1학년", "2학년", "3학년", "4학년"], index=2)

st.header("추가 자기소개")
hobby = st.text_input("취미를 입력하세요", "수학 문제 풀기")
goal = st.text_area("목표나 꿈을 입력하세요", "수학교사가 되는 것이 꿈입니다.")

st.header("자기소개 내용")
st.write(f"제 이름은 {name}입니다.")
st.write(f"나이는 {age}살입니다.")
st.write(f"학년은 {grade}입니다.")
st.write(f"취미는 {hobby}입니다.")
st.write(f"목표: {goal}")
st.write("저는 인천대학교 수학교육과에 재학 중인 학생입니다.")

