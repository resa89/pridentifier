import os
import numpy as np
from PIL import Image

from config import SNIPPET_WIDTH


class Fingerprint(object):
    def __init__(self, path):
        self.path_to_images_of_class = path
        self.class_name = os.path.split(path)[-1]
        self.image_names = []

        self.number_of_images = 0
        self.number_of_snippets = 0
        self.fingerprint = np.array(())

        self.load_images()


    def load_images(self):

        self.img_names = os.listdir(self.path_to_images_of_class)
        self.img_names = [image for image in self.img_names if not image.startswith('.')]
        self.img_names.sort()

        self.number_of_images = len(self.img_names)

        amount_snippets = 0

        for image in self.img_names:
            img_path = self.path_to_images_of_class + '/' + image
            img = Image.open(img_path)
            width, height = img.size
            amount_snippets_x_axis = width / SNIPPET_WIDTH
            amount_snippets_y_axis = height / SNIPPET_WIDTH
            amount_snippets += amount_snippets_x_axis * amount_snippets_y_axis

        self.number_of_snippets = amount_snippets


    def get_numbers(self):
        return(self.number_of_images, self.number_of_snippets)


    def extract_fingerprint(self):
        pass
        #self.accumulated_fingerprint =

    def compare_to_fingerprint(self, questioned_snippet):
        pass
        # return correlation value

