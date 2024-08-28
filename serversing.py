from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import yt_dlp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # or specify your allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cur_dir = os.getcwd()

@app.post("/download_video")
def download_video(url: str = Form(...)):
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(cur_dir, "video_filename.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([url])
    return {"message": "Download completed", "path": "video_filename.mp4"}