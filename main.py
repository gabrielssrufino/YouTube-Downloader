import customtkinter as ctk
from tkinter import filedialog, messagebox
import yt_dlp


def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d['downloaded_bytes'] / d['total_bytes']
        progress_bar.set(percent)


def download_video_or_audio(url, folder, download_type):
    try:
        ydl_opts = {
            'format': 'best' if download_type == 'Vídeo' else 'bestaudio/best',
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
            'noplaylist': True,
            'progress_hooks': [progress_hook],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Download Completo", f"{download_type} '{ydl.extract_info(url, download=False)['title']}' foi baixado com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


def download_playlist_or_audio(url, folder, download_type):
    try:
        ydl_opts = {
            'format': 'best' if download_type == 'Vídeo' else 'bestaudio/best',
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Download Completo", f"Playlist ({download_type}) foi baixada com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_var.set(folder_selected)


def start_download():
    url = url_var.get()
    folder = folder_var.get()
    download_type = selected_type.get()

    if selected_option.get() == 'Vídeo':
        download_video_or_audio(url, folder, download_type)
    elif selected_option.get() == 'Playlist':
        download_playlist_or_audio(url, folder, download_type)
    else:
        messagebox.showwarning("Erro", "Selecione uma categoria de link válida (Vídeo ou Playlist).")


app = ctk.CTk()
app.geometry('720x480')
app.title('YOUTUBE DOWNLOADER')

sec0 = ctk.CTkLabel(app, text='Você deseja baixar:')
sec0.pack(padx=10, pady=10, anchor='w')

type_frame = ctk.CTkFrame(app, fg_color='transparent')
type_frame.pack(pady=10, anchor='w')
selected_type = ctk.StringVar(value='Vídeo')

type_video_radio = ctk.CTkRadioButton(type_frame, text='Vídeo', variable=selected_type, value='Vídeo')
type_video_radio.pack(side='left', padx=10)

type_audio_radio = ctk.CTkRadioButton(type_frame, text='Áudio', variable=selected_type, value='Áudio')
type_audio_radio.pack(side='left', padx=10)

title_sec1 = ctk.CTkLabel(app, text='Insira o link que deseja fazer download:')
title_sec1.pack(anchor='w', padx=10, pady=10)

url_var = ctk.StringVar()
link = ctk.CTkEntry(app, width=720, height=40, textvariable=url_var)
link.pack(anchor='w', padx=10)

radio_frame_text = ctk.CTkLabel(app, text='Selecione a categoria do link:')
radio_frame_text.pack(padx=10, pady=5, anchor='w')

radio_frame = ctk.CTkFrame(app, fg_color='transparent')
radio_frame.pack(pady=10, anchor='w')

selected_option = ctk.StringVar(value='Vídeo')
video_radio = ctk.CTkRadioButton(radio_frame, text='Vídeo', variable=selected_option, value='Vídeo')
video_radio.pack(side='left', padx=10)

playlist_radio = ctk.CTkRadioButton(radio_frame, text='Playlist', variable=selected_option, value='Playlist')
playlist_radio.pack(side='left', padx=10)

folder_var = ctk.StringVar()
folder_button = ctk.CTkButton(app, text='Selecionar pasta de destino', command=select_folder)
folder_button.pack(padx=10, pady=10, anchor='w')

folder_label = ctk.CTkLabel(app, textvariable=folder_var, anchor='w')
folder_label.pack(anchor='w', padx=10)

progress_bar = ctk.CTkProgressBar(app, width=700)
progress_bar.pack(padx=10, pady=20, anchor='w')
progress_bar.set(0)

download = ctk.CTkButton(app, text='Fazer download', command=start_download, height=45)
download.pack(padx=10, pady=10)

app.mainloop()
