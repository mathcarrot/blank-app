import streamlit as st

st.title("자기 소개")

st.header("강경민")
st.write("제 이름은 강경민입니다. 저는 인천대학교 수학교육과에 재학 중인 학생입니다.")
st.header("")
st.write("저는 강경민입니다.")
st.header("입력 요소")
name = st.text_input("강경민")
age = st.number_input("28")

