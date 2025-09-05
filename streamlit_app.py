import streamlit as st
import pandas as pd
st.title("🎈 My First Streamlit App")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.markdown("Hello **Daniel**")
st.header("Happy to see you")
st.subheader("How are you doing")
st.badge('red')
st.balloons()
st.caption("programming made easy")
st.text("Go Home")
with st.form(key='my_form'):
    name = st.text_input("Name")
    age = st.number_input("Age")
    email = st.text_input("Email")
    st.form_submit_button("Sign Up")
x = st.slider('x')
st.write(x,'squared is',x*x)
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)