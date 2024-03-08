import yt_dlp
import json

# Lire les URL depuis le fichier texte
video_urls = []
with open("url.lst", "r", encoding="utf-8") as file:
    video_urls = [line.strip() for line in file]

# Télécharger les audios des vidéos
for url in video_urls:
    with yt_dlp.YoutubeDL({'format': 'bestaudio', 'outtmpl': '%(id)s.%(ext)s'}) as ydl:
        info_dict = ydl.extract_info(url, download=True)