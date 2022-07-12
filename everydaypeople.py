import streamlit as st


st.title('3V3RYDAYP3OPL3 TRANSLATOR')

input = st.text_input(label="Text Input", value="Insert text here")

caps_lock = st.checkbox('Caps')


def Translator():

    if caps_lock:
        lowercase_text = input.replace("e", "3")
        uppercase_text = lowercase_text.upper()
        st.text_input(label="T3xt Output", value=uppercase_text)

    else:
        translated_text = input.replace("e", "3")
        st.text_input(label="T3xt Output", value=translated_text)


Translator()

translate = st.button("Translat3")


