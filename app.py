import joblib
import streamlit as st
import numpy as np
import pandas as pd

reg = joblib.load('model/model.pkl')

def predict(model, input_arr):
    prediction = model.predict(input_arr)[0]
    return prediction

def run():
    # from PIL import Image
    # image = Image.open('logo.png')
    # image_flower = Image.open('flower.png')

    # st.Image(image, use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
        'How would you like to predict?',
        ('Online', 'Batch')
    )

    st.sidebar.info('This app is created to predict salaries')
    st.sidebar.success('http://www.github.com/irtizak/salaries')

    # st.sidebar.image('flower.png')

    st.title('Salary Prediction App')

    if add_selectbox == 'Online':
        yrs_since_phd = st.number_input('Years Since Ph.D. and Masters and Whatever', min_value=0., max_value=60., value=22.)
        yrs_service = st.number_input('Years of Service', min_value=0., max_value=60., value=17.)

        output=''

        input_arr = np.array([yrs_since_phd, yrs_service]).reshape(1, -1)
        
        output_dict = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

        if st.button('Predict'):
            output = predict(reg, input_arr)
#             output = output_dict[output]
        
        st.success('The predicted salary is {}'.format(output))

    # if add_selection == 'Batch':
    #     file_upload = st.file_uploader('Upload CSV file for predictions', type=['csv'])

    #     if file_upload is not None:
    #         data = pd.read_csv(file_upload)
    #         predictions = predict(model, input_df)
    #         st.write(predictions)

if __name__ == '__main__':
    run()
