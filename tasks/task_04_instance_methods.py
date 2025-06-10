"""
Task 4: Instance Methods - What Your Objects Can Do
Concept:
Instance methods are functions defined inside a class that operate on an object's
instance attributes (using `self`). They define an object's behaviors.
Let's design a 'Playlist' that can add songs, remove songs, and play.
"""

class Song: # Helper class for this task
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    def __str__(self):
        return f"'{self.title}' by {self.artist}"

class Playlist:
    def __init__(self, playlist_name):
        self.name = playlist_name
        self.songs = [] # Instance attribute: a list to hold Song objects
        print(f"Playlist '{self.name}' created.")

    def add_song(self, title, artist): # Instance method
        new_song = Song(title, artist)
        self.songs.append(new_song)
        print(f"Added {new_song} to '{self.name}'.")

    def remove_song(self, title_to_remove): # Instance method
        song_found = None
        for song in self.songs:
            if song.title.lower() == title_to_remove.lower():
                song_found = song
                break
        if song_found:
            self.songs.remove(song_found)
            print(f"Removed '{song_found.title}' from '{self.name}'.")
        else:
            print(f"Song '{title_to_remove}' not found in '{self.name}'.")

    def play_playlist(self): # Instance method
        if not self.songs:
            print(f"Playlist '{self.name}' is empty. Add some songs!")
            return
        print(f"\n--- Playing Playlist: {self.name} ---")
        for i, song in enumerate(self.songs):
            print(f"Now Playing ({i+1}/{len(self.songs)}): {song}")
        print("--- Playlist finished ---")

    def song_count(self): # Instance method
        return len(self.songs)

def get_input_params():
    return [
        {"name": "p_name", "label": "Playlist Name:", "type": "text_input", "default": "My Awesome Mix"},
        {"name": "song1_title", "label": "Song 1 Title:", "type": "text_input", "default": "Bohemian Rhapsody"},
        {"name": "song1_artist", "label": "Song 1 Artist:", "type": "text_input", "default": "Queen"},
        {"name": "song2_title", "label": "Song 2 Title:", "type": "text_input", "default": "Stairway to Heaven"},
        {"name": "song2_artist", "label": "Song 2 Artist:", "type": "text_input", "default": "Led Zeppelin"},
        {"name": "song_to_remove", "label": "Song Title to Remove (try one you added):", "type": "text_input", "default": "Bohemian Rhapsody"}
    ]

def run_task(p_name, song1_title, song1_artist, song2_title, song2_artist, song_to_remove):
    my_playlist = Playlist(p_name)

    print("\n--- Adding songs using instance methods ---")
    if song1_title and song1_artist:
        my_playlist.add_song(song1_title, song1_artist)
    if song2_title and song2_artist:
        my_playlist.add_song(song2_title, song2_artist)
    my_playlist.add_song("Imagine", "John Lennon") # Add a fixed one for variety

    print(f"\nPlaylist '{my_playlist.name}' now has {my_playlist.song_count()} songs.")

    my_playlist.play_playlist()

    print(f"\n--- Removing a song: '{song_to_remove}' ---")
    my_playlist.remove_song(song_to_remove)
    my_playlist.remove_song("Non Existent Song") # Try removing one not there

    my_playlist.play_playlist()

if __name__ == "__main__":
    run_task("Rock Classics", "Hotel California", "Eagles", "Kashmir", "Led Zeppelin", "Kashmir")