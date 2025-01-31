import  os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
import docx
from docx import Document
from PyPDF2 import PdfReader

load_dotenv()
APIKEY=os.getenv("APIKEY")
genai.configure(api_key=APIKEY) 
model=genai.GenerativeModel("gemini-1.5-flash")

def summarize_note(note_text):
    prompt= f"YOu are helpful{note_text}"
    response= model.generate_content(prompt)
    #result=response.txt
    return response.text
def extract_text_from_docx(file):
    document= Document(file)
    full_text=[paragraph.text for paragraph in document.paragraphs]
    return "\n".join(full_text)
def extract_text_from_pdf(file):
    pdf_reader= PdfReader(file)
    full_text=[page.extract_text() for page in pdf_reader.pages]
    return "\n".join(full_text)


st.title("Note summarizer")
st.write("Write your text here")

uploaded_file = st.file_uploader("Upload a file",type=["docx", "pdf"])
if uploaded_file:
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
      note_text = extract_text_from_docx(uploaded_file)
    elif uploaded_file.type=="application/pdf":
      note_text = extract_text_from_pdf(uploaded_file)
    else:
      st.error("Unsupported file type.")
      note_text= None
else:
   note_text= st.text_area("Or enter your note here:", "")


if st.button("Summarize"):
    if note_text:
        summary=summarize_note(note_text)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.warning("Please enter a note to summarize")
