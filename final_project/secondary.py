import tkinter as tk
from tkinter import ttk, messagebox
from tkhtmlview import HTMLLabel
import requests
import time
from pygame import mixer
import threading
import os
import tempfile

class LyricsExtractorWithAudio:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Enhanced Lyrics Extractor")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e2f")

        # Initialize pygame mixer
        mixer.init()

        # Add a class variable to store the temporary file path
        self.temp_audio_file = None

        # Title Section
        self.title_label = HTMLLabel(
            self.root,
            html='<h1 style="color:#f5f5f5; text-align:center;">Lyrics & Audio Player</h1>',
            background="#1e1e2f"
        )
        self.title_label.pack(pady=10)

        # Input Section
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(pady=20)

        ttk.Label(self.input_frame, text="Artist:", style="TLabel").grid(row=0, column=0, padx=5, sticky="w")
        self.artist_entry = ttk.Entry(self.input_frame, width=30)
        self.artist_entry.grid(row=0, column=1, padx=5)

        ttk.Label(self.input_frame, text="Song:", style="TLabel").grid(row=1, column=0, padx=5, sticky="w")
        self.song_entry = ttk.Entry(self.input_frame, width=30)
        self.song_entry.grid(row=1, column=1, padx=5)

        self.search_button = ttk.Button(self.input_frame, text="Search & Play", command=self.fetch_lyrics_and_audio)
        self.search_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Lyrics Section
        self.lyrics_frame = ttk.Frame(self.root)
        self.lyrics_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.lyrics_text = tk.Text(self.lyrics_frame, wrap=tk.WORD, bg="#282c34", fg="#ffffff", font=("Arial", 12))
        self.lyrics_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Controls Section
        self.controls_frame = ttk.Frame(self.root)
        self.controls_frame.pack(pady=10)

        self.play_button = ttk.Button(self.controls_frame, text="Play", command=self.play_audio)
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = ttk.Button(self.controls_frame, text="Pause", command=self.pause_audio)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = ttk.Button(self.controls_frame, text="Stop", command=self.stop_audio)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.lyrics_sync_thread = None
        self.lyrics_timestamps = []

    def fetch_lyrics_and_audio(self):
        """Fetch lyrics and download audio for playback"""
        artist = self.artist_entry.get().strip()
        song = self.song_entry.get().strip()

        if not artist or not song:
            messagebox.showerror("Error", "Please enter both artist and song name")
            return

        try:
            # Fetch lyrics from a public API
            url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
            response = requests.get(url)

            if response.status_code == 200:
                lyrics = response.json().get("lyrics", "")
                self.display_lyrics(lyrics)

                # Create a temporary file with proper permissions
                temp_dir = tempfile.gettempdir()
                self.temp_audio_file = os.path.join(temp_dir, "temp_song.mp3")
                
                # Download and save the audio file
                audio_url = "https://www.sample-videos.com/audio/mp3/crowd-cheering.mp3"
                with open(self.temp_audio_file, "wb") as f:
                    f.write(requests.get(audio_url).content)
                mixer.music.load(self.temp_audio_file)
            else:
                messagebox.showerror("Error", "Lyrics not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def display_lyrics(self, lyrics):
        """Display lyrics and parse timestamps if available"""
        self.lyrics_text.delete(1.0, tk.END)
        self.lyrics_text.insert(tk.END, lyrics)

        # Parse timestamps for synchronization
        self.lyrics_timestamps = []
        for line in lyrics.splitlines():
            if line.startswith("[") and "]" in line:
                timestamp = line[line.find("[")+1:line.find("]")]
                lyrics_line = line[line.find("]")+1:]
                self.lyrics_timestamps.append((self.timestamp_to_seconds(timestamp), lyrics_line))

    @staticmethod
    def timestamp_to_seconds(timestamp):
        """Convert timestamp (mm:ss) to seconds"""
        parts = timestamp.split(":")
        return int(parts[0]) * 60 + int(parts[1])

    def sync_lyrics(self):
        """Synchronize lyrics with audio playback"""
        start_time = time.time()
        for timestamp, line in self.lyrics_timestamps:
            while time.time() - start_time < timestamp:
                time.sleep(0.1)
            self.lyrics_text.insert(tk.END, f"\n{line}")

    def play_audio(self):
        """Play the loaded audio file"""
        mixer.music.play()

        # Start lyrics synchronization
        if self.lyrics_sync_thread is None or not self.lyrics_sync_thread.is_alive():
            self.lyrics_sync_thread = threading.Thread(target=self.sync_lyrics)
            self.lyrics_sync_thread.start()

    def pause_audio(self):
        """Pause the currently playing audio"""
        mixer.music.pause()

    def stop_audio(self):
        """Stop the audio playback"""
        mixer.music.stop()
        
        # Clean up the temporary file
        if self.temp_audio_file and os.path.exists(self.temp_audio_file):
            try:
                os.remove(self.temp_audio_file)
            except:
                pass

    def run(self):
        self.root.mainloop()

def main():
    app = LyricsExtractorWithAudio()
    app.run()

if __name__ == "__main__":
    main()
