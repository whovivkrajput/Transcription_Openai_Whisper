from moviepy.editor import *
import os
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
import streamlit as st

#convert vid to audio
def convert_vid_to_audio(video_path):
    if video_path is None:
        raise ValueError("The video path cannot be None")
    try:
        clip = VideoFileClip(video_path)
        audio_path = video_path.split(".")+"_audio.mp3"
        clip.audio.write_audiofile(audio_path)
        return audio_path
    except Exception as e:
        print(f"Error processing video: {e}")

def whisper_inference(media_path):

    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = "openai/whisper-base"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype = torch_dtype, low_cpu_mem_usage=True, use_safetensors = True
    )

    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model = model,
        tokenizer = processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=30,
        batch_size=16,
        return_timestamps=True,
        torch_dtype=torch_dtype,
        device=device,
    )

    result = pipe(media_path)
    # output = st.text_area(label = "Output",value=result["text"])

    # return st.write(output)
    return result["text"]

