#!/usr/bin/python3
from meme_control import MemeController, InMemoryMemeDatabase 

def test_can_save_img():
    """To test user can save image"""
    images_inventory = InMemoryMemeDatabase()
    images_inventory.save_img("img_001")
    assert "img_001" in images_inventory.get_all_imgs()
