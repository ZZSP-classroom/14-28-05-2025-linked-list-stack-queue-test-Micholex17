import unittest
from playlist_manager import *

class PlaylistsTests(unittest.TestCase):
    def test_add_song(self):
        playlist = Playlist()

        playlist.add_song(Song("Never Fade Away", "Samurai"))

        self.assertEqual(playlist.get_next_song().title, "Never Fade Away")
        self.assertEqual(playlist.get_next_song().artist, "Samurai")

    def test_remove_song(self):
        playlist = Playlist()
        
        playlist.add_song(Song("Never Fade Away", "Samurai"))
        playlist.add_song(Song("Chippin' In", "Samurai"))

        self.assertEqual(playlist.get_next_song().title, "Never Fade Away")
        self.assertEqual(playlist.get_next_song().artist, "Samurai")

        playlist.remove_song(1)

        self.assertEqual(playlist.get_next_song().title, "Never Fade Away")
        self.assertEqual(playlist.get_next_song().artist, "Samurai")

        playlist.add_song(Song("Chippin' In", "Samurai"))
        playlist.remove_song()

        self.assertEqual(playlist.get_next_song().title, "Chippin' In")
        self.assertEqual(playlist.get_next_song().artist, "Samurai")

if __name__ == "__main__":
    unittest.main()
