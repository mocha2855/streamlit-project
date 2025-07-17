import streamlit as st
import pandas as pd 
import plotly

st.set_page_config(page_title = 'home')
st.title("비만 분류 데이터분석 방법")
st.header('데이터 개요', divider = 'rainbow')

st.markdown('''
            
            BMI(체질량지수) 기반의 비만 분류 데이터셋을 분석합니다.
            이 데이터셋은 다양한 특성을 바탕으로 비만 여부를 예측하며, 주요 항목은 아래와 같습니다
            <ul style="list-style-type : circle; padding-left: 20px;">
                <li><strong>AGE</strong>:나이</li>
                <li><strong>GENDER</strong>:성별(MALE, FEMALE)</li>
                <li><strong>GENDER</strong>:성별(MALE, FEMALE)</li>
                <li><strong>HEIGHT</strong>:키(CM)</li>
                <li><strong>WEIGHT</strong>:몸무게(KG)</li>
                <li><strong>BMI</strong>:체질량지수</li>
                <li><strong>LABEL</strong>:비만여부(Normal Weight, Overweight, Obese, Underweight)</li>
            </ul>

''', unsafe_allow_html=True)