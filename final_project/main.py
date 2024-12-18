import tkinter as tk
from tkinter import ttk, messagebox
import requests
import time
import json
from tkinter import font as tkfont
from bs4 import BeautifulSoup

class LyricsExtractor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lyrics Extractor")
        self.root.geometry("1000x800")
        
        # Set classic theme
        self.root.configure(bg='#000000')
        
        # Custom fonts
        title_font = tkfont.Font(family="Times New Roman", size=24, weight="bold")
        heading_font = tkfont.Font(family="Times New Roman", size=14)
        text_font = tkfont.Font(family="Times New Roman", size=12)

        # Styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='#000', font=heading_font)
        style.configure('TEntry', font=text_font)
        style.configure('TButton', font=heading_font)
        
        # Title Frame
        title_frame = ttk.Frame(self.root, padding="20")
        title_frame.pack(fill=tk.X)
        
        title_label = ttk.Label(title_frame, text="Classic Lyrics Finder", 
                              font=title_font, foreground='#2C3E50')
        title_label.pack()

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="40")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Search Frame
        search_frame = ttk.Frame(self.main_frame)
        search_frame.pack(fill=tk.X, pady=(0,20))

        # Input fields with suggestions
        input_frame = ttk.Frame(search_frame)
        input_frame.pack(side=tk.LEFT)

        ttk.Label(input_frame, text="Artist:").pack(anchor='w')
        self.artist_entry = ttk.Entry(input_frame, width=40)
        self.artist_entry.pack(pady=(0,10))
        self.artist_suggestions = tk.Listbox(input_frame, height=3, width=38, 
                                           font=text_font, bg='#FFFFFF')
        self.artist_suggestions.pack()
        
        ttk.Label(input_frame, text="Song:").pack(anchor='w', pady=(10,0))
        self.song_entry = ttk.Entry(input_frame, width=40)
        self.song_entry.pack(pady=(0,10))
        self.song_suggestions = tk.Listbox(input_frame, height=3, width=38,
                                         font=text_font, bg='#FFFFFF')
        self.song_suggestions.pack()

        # Bind entry changes to show suggestions
        self.artist_entry.bind('<KeyRelease>', self.show_artist_suggestions)
        self.song_entry.bind('<KeyRelease>', self.show_song_suggestions)

        # Search button with classic styling
        button_frame = ttk.Frame(search_frame)
        button_frame.pack(side=tk.LEFT, padx=(20,0), anchor='n')
        
        self.search_btn = ttk.Button(button_frame, text="Search Lyrics",
                                   command=self.fetch_lyrics, style='Accent.TButton')
        self.search_btn.pack(pady=20)

        # Lyrics display with classic paper-like background
        self.lyrics_frame = ttk.Frame(self.main_frame)
        self.lyrics_frame.pack(fill=tk.BOTH, expand=True)

        self.lyrics_text = tk.Text(self.lyrics_frame, wrap=tk.WORD,
                                 font=text_font, bg='#FFFEF0', fg='#000000',
                                 padx=20, pady=20)
        self.lyrics_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Classic scrollbar
        scrollbar = ttk.Scrollbar(self.lyrics_frame, orient=tk.VERTICAL,
                                command=self.lyrics_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lyrics_text.configure(yscrollcommand=scrollbar.set)

        # Controls frame
        controls_frame = ttk.Frame(self.main_frame)
        controls_frame.pack(fill=tk.X, pady=10)

        # Auto-scroll control with classic styling
        self.auto_scroll_var = tk.BooleanVar(value=False)
        self.auto_scroll_check = ttk.Checkbutton(controls_frame,
                                               text="Auto-scroll lyrics",
                                               variable=self.auto_scroll_var,
                                               style='TCheckbutton')
        self.auto_scroll_check.pack(side=tk.LEFT)

        # Progress bar with classic styling
        self.progress = ttk.Progressbar(controls_frame, length=300, 
                                      mode='determinate', style='Horizontal.TProgressbar')
        self.progress.pack(side=tk.RIGHT)

    def show_artist_suggestions(self, event):
        # Simulated artist suggestions - replace with actual API call
        query = self.artist_entry.get().lower()
        suggestions = [
            "The Beatles", "Queen", "Pink Floyd", "Led Zeppelin",
            "Michael Jackson", "Elvis Presley", "Bob Dylan", "David Bowie"
        ]
        self.artist_suggestions.delete(0, tk.END)
        for artist in suggestions:
            if query in artist.lower():
                self.artist_suggestions.insert(tk.END, artist)

    def show_song_suggestions(self, event):
        # Simulated song suggestions - replace with actual API call
        query = self.song_entry.get().lower()
        artist = self.artist_entry.get()
        # Would normally fetch songs based on selected artist
        suggestions = [
            "Yesterday", "Bohemian Rhapsody", "Stairway to Heaven",
            "Imagine", "Like a Rolling Stone", "Hotel California"
        ]
        self.song_suggestions.delete(0, tk.END)
        for song in suggestions:
            if query in song.lower():
                self.song_suggestions.insert(tk.END, song)

    def fetch_lyrics(self):
        artist = self.artist_entry.get().strip()
        song = self.song_entry.get().strip()

        if not artist or not song:
            messagebox.showerror("Error", "Please enter both artist and song name")
            return

        self.lyrics_text.delete(1.0, tk.END)
        self.progress['value'] = 0
        self.root.update()

        try:
            # Try lyrics.ovh API first
            alt_url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
            alt_response = requests.get(alt_url)
            self.progress['value'] = 50
            self.root.update()
            
            if alt_response.status_code == 200:
                lyrics = alt_response.json().get('lyrics', '')
                if lyrics:
                    self.display_lyrics(lyrics)
                    self.progress['value'] = 100
                    self.root.update()
                    return

            # If lyrics.ovh fails, try AZLyrics
            artist = artist.lower().replace(" ", "")
            song = song.lower().replace(" ", "")
            url = f"https://www.azlyrics.com/lyrics/{artist}/{song}.html"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers)
            self.progress['value'] = 75
            self.root.update()

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                lyrics_div = soup.find('div', class_='', id='')  # AZLyrics usually has lyrics in a div without class/id
                if lyrics_div:
                    lyrics = lyrics_div.get_text().strip()
                    self.display_lyrics(lyrics)
                else:
                    self.lyrics_text.insert(tk.END, "Could not find lyrics")
            else:
                self.lyrics_text.insert(tk.END, "Could not fetch lyrics")

            self.progress['value'] = 100
            self.root.update()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.progress['value'] = 0
            self.root.update()

    def display_lyrics(self, lyrics):
        self.lyrics_text.delete(1.0, tk.END)
        self.lyrics_text.insert(tk.END, lyrics)
        
        if self.auto_scroll_var.get():
            self.start_auto_scroll()

    def start_auto_scroll(self):
        """Auto-scroll lyrics at a readable pace"""
        def scroll():
            if self.auto_scroll_var.get():
                self.lyrics_text.yview_scroll(1, 'units')
                self.root.after(100, scroll)
        scroll()

    def run(self):
        self.root.mainloop()

def main():
    app = LyricsExtractor()
    app.run()

if __name__ == "__main__":
    main()
