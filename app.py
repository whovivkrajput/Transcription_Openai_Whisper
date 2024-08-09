import streamlit as st
from pathlib import Path
import base64
import wx
import os

from whisper_infer import convert_vid_to_audio, whisper_inference

st.set_page_config(
     page_title='Transcript - Whisper',
     layout="centered",
     initial_sidebar_state="expanded",
)
    
def main():
    cs_sidebar()
    print("1")
    selectedMediaPath = cs_body()
    print("2")
    # selectedMediaPath = select_media()
    print("3")
    if selectedMediaPath != None:
        # raise ValueError("Selected media path cannot be None")
    
        audioPath = convert_vid_to_audio(selectedMediaPath)
        transcriptText = whisper_inference(selectedMediaPath)
        txt = st.markdown(transcriptText)
        # txt = st.text_area(label= "Output:",value = transcriptText)
        # return st.text(transcriptText)
        # print(transcriptText)
        # output = view_output(transcriptText)
        return None

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def cs_sidebar():
    st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Whisper by OpenAI</h1>",unsafe_allow_html=True)
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=302 height=150>](https://streamlit.io/)'''
                        .format(img_to_bytes(r"C:\Users\Vivek Singh Rajput\Desktop\recent_studies_projects\SpeechtoText\data\openai_whisper.png"))
                        , unsafe_allow_html=True)
    
    st.sidebar.header('Transcript Audio & Video')

    st.sidebar.markdown('''
            <small>Whisper is a transformer based pre-trained model for automatic speech recognition (ASR) and speech translation.</small>
            ''', unsafe_allow_html=True)
    return None

def cs_body():
    st.markdown("<h1 style='text-align: center; color: white;'>Upload ,Process, Get Transcript..!!</h1>",unsafe_allow_html=True)
    file_path = None
    
    if st.button("Browse"):
        dialog = wx.FileDialog(None, "Select the File", style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() ==  wx.ID_OK:
            file_path = dialog.GetPath()
            print("############", file_path)
        return file_path

# def view_output(text):
#     txt = st.text_area(label= "Output:",value = text)
#     return st.write(txt) 



# def select_media():
#     if st.button("Browse"):
#         dialog = wx.FileDialog(None, "Select the File", style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
#         if dialog.ShowModal() ==  wx.ID_OK:
#             file_path = dialog.GetPath()
#             # audioPath = convert_vid_to_audio(file_path)
#             # print("###############", audioPath)
#     return None
    # else:
    #     file_path = None
    #     # pass
    # if not os.path.exists(file_path):
    #     raise FileNotFoundError(f"The file at does not exist or path is None.")
    # else:
        

if __name__ == "__main__":
  tmpApp = wx.PySimpleApp()
  result = main()
  del tmpApp