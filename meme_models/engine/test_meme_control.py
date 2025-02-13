#!/usr/bin/python3
from meme_control import MemeController, SqliteDatabase

def test_can_save_meme():
    """To test user can save image"""
    images_inventory = SqliteDatabase()
    images_inventory.save_meme("new_img.jpeg")
    assert "new_img.jpeg" in images_inventory.get_all_memes()
