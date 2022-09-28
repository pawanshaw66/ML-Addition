import streamlit as st
import joblib




def main():
    html_temp = """
    <div style = "background-color:lightblue;padding:16px">
    <h2 style = "color:black";text-align:center> Addition  Prediction Using ML</h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('model_joblib')
    
    p1 = st.number_input("Enter first number")
    
    p2 = st.number_input("Enter second number")
    
    
    if st.button('Predict'):
      pred =   model.predict([[p1,p2]]) 
      st.success("Addition is  {}".format(pred[0]))
    
    
    
    
    
    
    
    
if __name__== '__main__':
    main()    