from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "songs/%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        }
    ],
    "postprocessor_args": ["-ar", "16000"],
    "prefer_ffmpeg": True,
    "keepvideo": False,
}


def download(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    link = input("Enter the url of the song\n: ")
    download(link)
