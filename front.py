import streamlit as st
import requests

st.title('Bank Project')

api_url = 'http://127.0.0.1:8000/predict/'

person_age = st.number_input('Age', min_value=0, max_value=100)

person_gender = st.selectbox('Gender', ['Male', 'Female'])
person_education = st.selectbox('Education', ['Bachelor', 'Doctorate', 'High School', 'Master', 'Associate'])
person_income = st.number_input('Income', min_value=0.0)
person_emp_exp = st.number_input('Employment Expense', min_value=0, max_value=100)
person_home_ownership = st.selectbox('Home Ownership', ['OTHER', 'OWN', 'RENT', 'MORTGAGE'])
loan_amount = st.number_input('Amount', min_value=0.0, step=500.0)
loan_intent = st.selectbox('Loan purpose', ['EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE', 'DEBTCONSOLIDATION'])
loan_int_rate = st.number_input('Interest Rate', min_value=0.0)
loan_percent_income = st.number_input('Percentage of Income', min_value=0.0, max_value=1.0)
cb_person_cred_hist_length = st.number_input('Custom Credit History Length', min_value=0.0)
credit_score = st.number_input('Credit Score', min_value=0,step=10)
previous_loan_defaults_on_file = st.selectbox('Previous Loan Default On File', ('Yes', 'No'))



bank_data = {
    'person_age': person_age,
    'person_gender': person_gender,
    'person_education': person_education,
    'person_income': person_income,
    'person_emp_exp': person_emp_exp,
    'person_home_ownership': person_home_ownership,
    'loan_amnt': loan_amount,
    'loan_intent': loan_intent,
    'loan_int_rate': loan_int_rate,
    'loan_percent_income': loan_percent_income,
    'cb_person_cred_hist_length': cb_person_cred_hist_length,
    'credit_score': credit_score,
    'previous_loan_defaults_on_file': previous_loan_defaults_on_file
    }

if st.button('Predict'):
    try:
        answer = requests.post(api_url, json=bank_data, timeout=10)
        answer.raise_for_status()
        result = answer.json()
        st.success(f"Result: {result.get('result')}")
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP ошибка: {http_err}")
    except requests.exceptions.ConnectionError:
        st.error("Ошибка подключения: не удалось соединиться с сервером FastAPI")
    except requests.exceptions.Timeout:
        st.error("Превышено время ожидания запроса к API")
    except requests.exceptions.RequestException as err:
        st.error(f"Произошла ошибка при запросе: {err}")