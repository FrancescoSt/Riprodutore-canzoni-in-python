import os
import pygame
import time
import tkinter as tk
from tkinter import filedialog

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def get_song_list(folder_path):
    song_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            song_list.append(os.path.join(folder_path, filename))
    return song_list

class MusicPlayer:
    def __init__(self, song_list):
        self.song_list = song_list
        self.current_song_index = 0

        self.root = tk.Tk()
        self.root.title("Music Player")

        self.song_label = tk.Label(self.root, text="Current Song: ")
        self.song_label.pack()

        self.previous_button = tk.Button(self.root, text="Previous", command=self.play_previous_song)
        self.previous_button.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play_current_song)
        self.play_button.pack()

        self.next_button = tk.Button(self.root, text="Next", command=self.play_next_song)
        self.next_button.pack()

    def play_current_song(self):
        file_path = self.song_list[self.current_song_index]
        # Gestione dell'UnicodeError: decodifica il percorso del file
        decoded_path = file_path.encode('utf-8').decode('unicode-escape')
        self.song_label["text"] = "Current Song: " + os.path.basename(decoded_path)
        play_music(decoded_path)

    def play_previous_song(self):
        self.current_song_index -= 1
        if self.current_song_index < 0:
            self.current_song_index = len(self.song_list) - 1
        self.play_current_song()

    def play_next_song(self):
        self.current_song_index += 1
        if self.current_song_index >= len(self.song_list):
            self.current_song_index = 0
        self.play_current_song()

    def start(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    root.withdraw()  # Nasconde la finestra principale di Tkinter
    folder_path = filedialog.askdirectory(title="Select Folder")
    if not folder_path:
        return

    song_list = get_song_list(folder_path)
    if not song_list:
        print("No songs found in the selected folder.")
        return

    music_player = MusicPlayer(song_list)
    music_player.start()

if __name__ == "__main__":
    main()
