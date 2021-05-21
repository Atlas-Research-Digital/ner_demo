import streamlit as st

from model_utils import *

st.set_page_config(layout="wide")

header = st.beta_container()

text_input, text_output = st.beta_columns(2)

with header:
    st.title("Atlas Research Named Entity Recognition Demo")

with text_input:
    st.header("Text Input")
    user_input = st.text_area("Add your clinical notes below:", value="", height=600)

with text_output:
    st.header("Tagged Output")
    ner_model, preproc = load_model()
    if user_input != "":
        st.write(get_predictions(ner_model, preproc, user_input))

    # nlp = spacy.load("en_core_web_sm")
    # doc = nlp(user_input)
    # visualize_ner(doc, labels=nlp.get_pipe("ner").labels, title="")

about_section = st.beta_container()

with about_section:
    st.header("About")
    st.text("This application utilizes ClinicalBERT trained on data from the i2b2 2011 NLP challenge.")






# def main():
#     st.title("Medical Document Classifier")
#     st.subheader("Named Entity Recognition app")
#
#     if st.button("Run"):
#         st.text("Original")
#
#
#
# if __name__ = '__main__':
#     main()