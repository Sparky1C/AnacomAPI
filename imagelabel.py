import logging
import numpy as np

class ImageAnnotator:
    def __init__(self, categories: List[str]):
        self.categories = categories

    def annotate(self, data: np.ndarray) -> Dict[str, List[Tuple[int, int]]]:
        annotations = {}
        for category in self.categories:
            annotations[category] = [(i, j) for i in range(data.shape[0]) for j in range(data.shape[1]) if np.array_equal(data[i][j], np.array(category))]
        return annotations


class ImageAnalyzer:
    def analyze(self, data: np.ndarray) -> Dict[str, float]:
        analysis = {
            "dimensions": (data.shape[0], data.shape[1]),
            "num_pixels": data.shape[0] * data.shape[1],
            "average_intensity": np.mean(data),
            "contrast": np.std(data)
        }
        return analysis


class ImageProcessor:
    def __init__(self):
        self.logger = self._setup_logger()

    def annotate_image(self, data: np.ndarray, categories: List[str]) -> Dict[str, List[Tuple[int, int]]]:
        """
        Annotates and labels the given image based on the user's input.

        :param data: The image to annotate.
        :param categories: A list of categories to label.
        :return: A dictionary containing the annotated and labeled image.
        """
        annotator = ImageAnnotator(categories)

        try:
            annotations = annotator.annotate(data)
            return annotations
        except Exception as e:
            self.logger.exception("Annotating the image failed.")
            raise e

    def analyze_image(self, data: np.ndarray) -> Dict[str, float]:
        """
        Analyzes the given image for dimensions, number of pixels, average intensity, and contrast.

        :param data: The image to analyze.
        :return: A dictionary containing the analysis results.
        """
        analyzer = ImageAnalyzer()

        try:
            analysis = analyzer.analyze(data)
            return analysis
        except Exception as e:
            self.logger.exception("Analyzing the image failed.")
            raise e

    def label_images(self, data: List[np.ndarray], categories: List[str]) -> List[Dict[str, List[Tuple[int, int]]]]:
        """
        Annotates and labels a large amount of images based on the user's input.

        :param data: A list of images to annotate.
        :param categories: A list of categories to label.
        :return: A list of dictionaries containing the annotated and labeled images.
        """
        labeled_data = []

        for datum in data:
            annotations = self.annotate_image(datum, categories=categories)
            labeled_data.append(annotations)

        return labeled_data

    def analyze_images(self, data: List[np.ndarray]) -> List[Dict[str, float]]:
        """
        Analyzes a large amount of images for dimensions, number of pixels, average intensity, and contrast.

        :param data: A list of images to analyze.
        :return: A list of dictionaries containing the analysis results.
        """
        analyzed_data = []

        for datum in data:
            analysis = self.analyze_image(datum)
            analyzed_data.append(analysis)

        return analyzed_data

    def _setup_logger(self):
        """
        Sets up a logger for the ImageProcessor class.
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        logger.addHandler(console_handler)

        return logger
