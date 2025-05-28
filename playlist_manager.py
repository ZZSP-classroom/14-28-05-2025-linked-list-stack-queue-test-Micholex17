from linked_list import *

class Playlist:
    def __init__(self):
        self.__l = LinkedList()
    
    def add_song(self, value):
        self.__l.insertAtEnd(value)
    
    def remove_song(self, index = 0):
        self.__l.remove_at_index(index)
    
    def get_next_song(self):
        return self.__l.head.data

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
