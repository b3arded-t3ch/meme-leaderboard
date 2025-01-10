#!/usr/bin/python3
import os
import json

class Meme_Manager:
    """
    This class handles adding and fetching images from the database

    __objects: A dictionary that contains all image objects
    __file_path: The location of an image

    """
    __objects = {}
    __file_path = "file.json"

    def save_img(self)
    """serializes __objects to the JSON file"""
    __objects_dict = {}
    for key, value in self.__objects.items():
        __objects_dict[key] = value.to_dict()
    try:
        with open(self.__file_path, 'w') as img_file:
            json.dump(__objects_dict, img_file)
        return True
    except (OSError, TypeError) as e:
        return False


    def get_img(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as json_img_file:
                try:
                    img_dict = json.load(json_file)
                    for k, v in img_dict.items():
                        class_name, obj_id = k.split('.')
                        cls = eval(class_name)
                        instnc = cls(**v)
                        self.objects[k] = instnc
                except Exception:
                    pass
