import os
import numpy as np
from PIL import Image

from ..feature_extractor import FeatureExtractor


class Fingerprint(object):
    def __init__(self, path, SNIPPET_WIDTH, NUMBER_PIXELS):
        self.path_to_images_of_class = path
        self.class_name = os.path.split(path)[-1]
        self.image_names = []

        self.number_of_images = 0
        self.number_of_snippets = 0
        self.fingerprint = np.array(())
        self.SNIPPET_WIDTH = SNIPPET_WIDTH
        self.NUMBER_PIXELS = NUMBER_PIXELS

        self.load_images()


    def update_pixelSize(self, NUMBER_PIXELS):

        # TODO: inform user that feature amount is larger than snippet size
        if self.SNIPPET_WIDTH*self.SNIPPET_WIDTH < NUMBER_PIXELS:
            self.NUMBER_PIXELS = self.SNIPPET_WIDTH*self.SNIPPET_WIDTH
        else:
            self.NUMBER_PIXELS = NUMBER_PIXELS


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
            # TODO: check order of width and height
            amount_snippets_x_axis = width // self.SNIPPET_WIDTH
            amount_snippets_y_axis = height // self.SNIPPET_WIDTH
            amount_snippets += amount_snippets_x_axis * amount_snippets_y_axis

        self.number_of_snippets = amount_snippets


    def get_numbers(self):
        return(self.number_of_images, self.number_of_snippets)


    def extract_fingerprint(self):

        feature_extractor = FeatureExtractor(self.path_to_images_of_class, self.img_names, self.number_of_snippets,
                                             self.SNIPPET_WIDTH, self.NUMBER_PIXELS)
        self.fingerprint = feature_extractor.get_accumulated_spectra()


    def get_fingerprint(self):

        return(self.fingerprint)

