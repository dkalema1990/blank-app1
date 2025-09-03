import streamlit as st

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