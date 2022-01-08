import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import webbrowser


#im = Image.open('./fifa20.png')
#st.image(im,width = 700,caption = "Fifa 2021")
# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
    return 'Check yourself for Diabetes'

# defining the function which will make the prediction using our model

def prediction(Age, Sex, ChestPainType, RestingBP, Cholesterol,FastingBS, RestingECG, MaxHR,ExerciseAngina,Oldpeak,ST_Slope):

    prediction = classifier.predict(
        [[Age, Sex, ChestPainType, RestingBP, Cholesterol,FastingBS, RestingECG, MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])
    print(prediction)
    if prediction == 0.00:
        prediction = 'You are healthy'
    elif prediction==1.00:
        prediction='You are more likely to have a heart Disease'
    return prediction
    

    # this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    #st.title("Fifa Overall Player Rating Prediction")
    
    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:orange;padding:13px">
    <h1 style ="color:black;text-align:center;">Heart Diesease</h1>
    <p>Input a number corresponding to the option you want to select where options are provided</p>
    </div>
    """
    
    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    st.title("please enter the parameters")  # get input values
    Age = st.number_input('Age')
    Sex = st.number_input("Sex(1.male 2.female)")
    ChestPainType = st.number_input("ChestPainType(0.ASY,1.ATA, 2.NAP,3.TA)")
    RestingBP = st.number_input("RestingBP")
    Cholesterol = st.number_input("Cholesterol")
    FastingBS = st.number_input("FastingBS")
    RestingECG = st.number_input("RestingECG( 0.LVH, 1.Normal, 2.ST )")
    MaxHR = st.number_input("MaxHR")
    ExerciseAngina = st.number_input('ExerciseAngina(0.No, 1.Yes)')
    Oldpeak = st.number_input("Oldpeak")
    ST_Slope = st.number_input('ST_Slope( 0.Down, 1.Up, 2.Flat)')
    



    result =""
    
    #predict button
    if st.button("Predict"):
        result = prediction(Age, Sex, ChestPainType, RestingBP, Cholesterol,FastingBS, RestingECG, MaxHR,ExerciseAngina,Oldpeak,ST_Slope)
    
    st.success(result)
    

    #source code button
    url = 'https://github.com/victoryeovil/'

    if st.button('Github'):
        webbrowser.open_new_tab(url)




    
if __name__=='__main__':
    main()
