import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title("데이터 시각화 예시")

st.header("샘플 데이터 시각화")

# 샘플 데이터 생성
np.random.seed(42)
data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(1, 100, 10),
    'category': np.random.choice(['A', 'B', 'C'], 10)
})

st.subheader("선 그래프")
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'])
st.pyplot(fig)

st.subheader("막대 그래프")
fig, ax = plt.subplots()
ax.bar(data['x'], data['y'])
st.pyplot(fig)

st.subheader("산점도 (Plotly)")
fig = px.scatter(data, x='x', y='y', color='category')
st.plotly_chart(fig)

st.subheader("히스토그램")
fig, ax = plt.subplots()
ax.hist(data['y'], bins=5)
st.pyplot(fig)

st.header("사용자 데이터 입력")

st.subheader("수동 데이터 입력")
x_input = st.text_input("X 값들 (쉼표로 구분)", "1,2,3,4,5")
y_input = st.text_input("Y 값들 (쉼표로 구분)", "10,20,30,40,50")

if st.button("차트 생성"):
    try:
        x_vals = [float(x.strip()) for x in x_input.split(',')]
        y_vals = [float(y.strip()) for y in y_input.split(',')]
        if len(x_vals) == len(y_vals):
            user_data = pd.DataFrame({'x': x_vals, 'y': y_vals})
            fig, ax = plt.subplots()
            ax.scatter(user_data['x'], user_data['y'])
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            st.pyplot(fig)
        else:
            st.error("X와 Y의 개수가 같아야 합니다.")
    except ValueError:
        st.error("숫자만 입력하세요.")

st.subheader("CSV 데이터 입력")
csv_input = st.text_area("CSV 데이터를 입력하세요 (헤더 포함)", "x,y\n1,10\n2,20\n3,30")

if st.button("CSV 차트 생성"):
    try:
        from io import StringIO
        csv_data = pd.read_csv(StringIO(csv_input))
        st.write(csv_data)
        fig = px.line(csv_data, x=csv_data.columns[0], y=csv_data.columns[1])
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"데이터 처리 오류: {e}")
