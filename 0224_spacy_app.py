import streamlit as st
import pickle, os
import spacy
from spacy_streamlit import visualize_ner


st.set_page_config(layout="wide")

header = st.beta_container()

text_input, text_output = st.beta_columns(2)

with header:
    st.title("Atlas Research Named Entity Recognition Demo")

with text_input:
    st.header("Text Input")
    user_input = st.text_area("Add your clinical notes below:", height=600)

with text_output:
    st.header("Tagged Output")

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(user_input)
    visualize_ner(doc, labels=nlp.get_pipe("ner").labels, title="")

about_section = st.beta_container()

with about_section:
    st.header("About")
    st.text("This application utilizes ClinicalBERT trained on data from the i2b2 2011 NLP challenge.")

# def load_model(model_file):
#     # Load model json file
#     json_file = open('model.json', 'r')
#
#     # Load Ktrain preproc file
#     features = pickle.load(open('preproc.sav', 'rb'))
#
#     loaded_model_json = json_file.read()
#     json_file.close()
#     loaded_model = model_from_json(loaded_model_json)
#
#     loaded_model.load_weights("model.h5")
#     print("Model Loaded from disk")
#
#     # compile and evaluate loaded model
#     loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#     return loaded_model, features
#
#
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