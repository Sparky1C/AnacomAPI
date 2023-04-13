import logging
from typing import Dict, List, Tuple

import numpy as np


class ImageAnnotator:
    """
    Annotates an image based on a given list of categories.
    """

    def __init__(self, categories: List[str]):
        self.categories = categories

    def annotate(self, data: np.ndarray) -> Dict[str, List[Tuple[int, int]]]:
        """
        Annotates an image by finding all coordinates of pixels that match each category.

        :param data: The image to annotate.
        :return: A dictionary of category labels to lists of (i, j) coordinates.
        """
        annotations = {}

        for category in self.categories:
            matching_pixels = [(i, j) for i in range(data.shape[0]) for j in range(data.shape[1]) if np.array_equal(data[i][j], np.array(category))]
            annotations[category] = matching_pixels

        return annotations


class ImageAnalyzer:
    """
    Analyzes an image for various properties.
    """

    def analyze(self, data: np.ndarray) -> Dict[str, float]:
        """
        Analyzes an image for its dimensions, number of pixels, average intensity, and contrast.

        :param data: The image to analyze.
        :return: A dictionary of analysis results.
        """
        analysis = {
            "dimensions": (data.shape[0], data.shape[1]),
            "num_pixels": data.shape[0] * data.shape[1],
            "average_intensity": np.mean(data),
            "contrast": np.std(data)
        }

        return analysis


class ImageProcessor:
    """
    Processes images by annotating and analyzing them.
    """

    def __init__(self):
        self.logger = self._setup_logger()

    def annotate_image(self, image: np.ndarray, categories: List[str]) -> Dict[str, List[Tuple[int, int]]]:
        """
        Annotates and labels the given image based on a list of categories.

        :param image: The image to annotate.
        :param categories: A list of category labels.
        :return: A dictionary of annotated categories and their corresponding pixel coordinates.
        """
        annotator = ImageAnnotator(categories)

        try:
            annotations = annotator.annotate(image)
            return annotations
        except Exception as e:
            self.logger.exception("Annotating the image failed.")
            raise e

    def analyze_image(self, image: np.ndarray) -> Dict[str, float]:
        """
        Analyzes the given image for dimensions, number of pixels, average intensity, and contrast.

        :param image: The image to analyze.
        :return: A dictionary of analysis results.
        """
        analyzer = ImageAnalyzer()

        try:
            analysis = analyzer.analyze(image)
            return analysis
        except Exception as e:
            self.logger.exception("Analyzing the image failed.")
            raise e

    def label_images(self, images: List[np.ndarray], categories: List[str]) -> List[Dict[str, List[Tuple[int, int]]]]:
        """
        Labels the given list of images based on a list of categories.

        :param images: A list of images to label.
        :param categories: A list of category labels.
        :return: A list of dictionaries of annotated categories and their corresponding pixel coordinates for each image.
        """
        annotations = []

        for image in images:
            try:
                annotation = self.annotate_image(image, categories)
                annotations.append(annotation)
            except Exception as e:
                self.logger.exception("An error occurred while labeling an image.")
                raise e

        return annotations
