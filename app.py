# Import libraries
import joblib
import streamlit as st
import numpy as np
import pandas as pd

# Import models
rgr = joblib.load('model/rgr.pkl')
clf = joblib.load('model/clf.pkl')

# Prediction function
def predict(model, df):
    prediction = model.predict(df)[0]
    return prediction

def run():

    st.sidebar.info('This app predicts faculty salaries.')
    st.sidebar.success('http://www.github.com/irtizak/salaries')
    
    add_selectbox = st.sidebar.selectbox(
        'What model would you like to use?',
        ('Regression', 'Classification')
    )

    st.title('Salary Prediction App')

    yrs_since_phd = st.number_input('Years Since Ph.D.', min_value=0., max_value=60., value=22.)
    yrs_service = st.number_input('Years of Service', min_value=0., max_value=60., value=17.)
    rank = st.selectbox('Rank', ('AsstProf', 'AssocProf', 'Prof'))
    discipline = st.selectbox('Discipline', ('A', 'B'))
    sex = st.selectbox('Sex', ('Male', 'Female'))

    output=''
    
    col_names = ['yrs_since_phd', 'yrs_service', 'rank', 'discipline', 'sex']
    input_data = [[yrs_since_phd], [yrs_service], [rank], [discipline], [sex]]
    data_dict = dict(zip(col_names, input_data))
    df = pd.DataFrame.from_dict(data_dict)
    
    if st.button('Predict'):
        if add_selectbox == 'Regression':
            output = round(predict(rgr, df), 0)
            st.success('The predicted salary is {}'.format(output))
        else:
            output = round(predict(clf, df), 0)
            output_dict = {1: 'ABOVE', 0: 'BELOW'}
            st.success('{} median salary.'.format(output_dict[output]))

if __name__ == '__main__':
    run()
