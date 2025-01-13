#!/usr/bin/python3
from  file_storage import save_meme, get_meme

class MemeController:
    """
    This is the class to manage the meming.
    It contains methods for the business logic of the app
    """

    def __init__(self, meme_database: MemeDatabase):
        self.meme_database: meme_database

    def submit_meme(self, meme: str):
        """business logic for meme submission"""
        # check if it's a valid format
        if not isinstance(meme, str):
            raise ValueError("invalid format")
        else:
            self.meme_database.save_meme(meme)

    def get_all_memes(self):
        """retrieves all memes from the database"""
        return self.meme_database.get_meme()

class MemeDatabase:
    """defines methods for storage systems"""
    def save_meme(self, meme):
        raise NotImplementedError
    def get_num_memes(self):
        raise NotImplementedError
    def get_all_memes(self):
        raise NotImplementedError

class InMemoryMemeDatabase(MemeDatabase):
    """uses a simple list to store images"""
    def __init__(self):
        super().__init__()
        self.images = []

    def save_img(self, img):
        """function to save meme)"""
        self.images.append(img)

