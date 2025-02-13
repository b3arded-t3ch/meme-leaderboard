#!/usr/bin/python3
import sqlite3

class MemeDatabase:
    """defines abstract class containing methods for storage systems"""
    def save_meme(self, meme):
        raise NotImplementedError
    def get_all_memes(self):
        raise NotImplementedError

class MemeController:
    """
    This is the class to manage the meming.
    It contains methods for the business logic of the app
    It is more like the class for image model
    """

    def __init__(self, meme_database: MemeDatabase):
        self.meme_database = meme_database

    def save_meme(self, meme: str):
        """business logic for meme submission"""
        # check if it's a valid format
        if not isinstance(meme, str):
            raise ValueError("invalid format")
        else:
            self.meme_database.save_meme(meme)

    def get_all_memes(self):
        """retrieves all memes from the database"""
        return self.meme_database.get_all_memes()

class InMemoryMemeDatabase(MemeDatabase):
    """uses a simple list to store images"""
    def __init__(self):
        super().__init__()
        self.images = []

    def save_meme(self, img):
        """function to save meme"""
        self.images.append(img)

    def get_all_memes(self):
        """retrieves all images"""
        return self.images

class SqliteDatabase(MemeDatabase):
    """A real database to store and retrieve images"""
    def __init__(self):
        self.con = sqlite3.connect("meme_db")
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS images (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        imgfile BLOB
                        )""")
    def save_meme(self, img_path):
        """insert image"""
        with open(img_path, 'rb') as f:
            image_data = f.read()
        self.cur.execute("INSERT INTO images(imgfile) VALUES(?)", (image_data,))
        self.con.commit()

    def get_all_memes(self):
        """retrieve memes"""
        try:
            res = self.cur.execute("SELECT imgfile FROM images")
            all_memes = res.fetchall()
            img = [img[0] for img in all_memes]
            return img
        except Exception as e:
            raise RuntimeError(e)

    def close(self):
        """Closes the database"""
        self.con.close()
