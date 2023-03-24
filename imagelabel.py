import logging
from typing import Dict, List

class Annotator:
    def __init__(self, categories: List[str]):
        self.categories = categories

    def annotate(self, data: str) -> Dict[str, List[str]]:
        annotations = {}
        for category in self.categories:
            annotations[category] = [f"{category} {i}" for i, word in enumerate(data.split()) if word == category]
        return annotations


class Analyzer:
    def analyze(self, data: str) -> Dict[str, float]:
        analysis = {
            "complexity": len(data),
            "readability": len(data.split()),
            "maintainability": data.count(";") / max(1, data.count("\n"))
        }
        return analysis


class AnacomAI:
    def __init__(self):
        self.logger = self._setup_logger()

    def annotate(self, data: str, categories: List[str]) -> Dict[str, List[str]]:
        """
        Annotates and labels the given data based on the user's input.

        :param data: The data to annotate.
        :param categories: A list of categories to label.
        :return: A dictionary containing the annotated and labeled data.
        """
        annotator = Annotator(categories)

        try:
            annotations = annotator.annotate(data)
            return annotations
        except Exception as e:
            self.logger.exception("Annotating the data failed.")
            raise e

    def analyze(self, data: str) -> Dict[str, float]:
        """
        Analyzes the given data for complexity, readability, and maintainability.

        :param data: The data to analyze.
        :return: A dictionary containing the analysis results.
        """
        analyzer = Analyzer()

        try:
            analysis = analyzer.analyze(data)
            return analysis
        except Exception as e:
            self.logger.exception("Analyzing the data failed.")
            raise e

    def label_data(self, data: List[str], categories: List[str]) -> List[Dict[str, List[str]]]:
        """
        Annotates and labels a large amount of data based on the user's input.

        :param data: A list of data strings to annotate.
        :param categories: A list of categories to label.
        :return: A list of dictionaries containing the annotated and labeled data.
        """
        labeled_data = []

        for datum in data:
            annotations = self.annotate(datum, categories=categories)
            labeled_data.append(annotations)

        return labeled_data

    def analyze_data(self, data: List[str]) -> List[Dict[str, float]]:
        """
        Analyzes a large amount of data for complexity, readability, and maintainability.

        :param data: A list of data strings to analyze.
        :return: A list of dictionaries containing the analysis results.
        """
        analyzed_data = []

        for datum in data:
            analysis = self.analyze(datum)
            analyzed_data.append(analysis)

        return analyzed_data

    def _setup_logger(self):
        """
        Sets up a logger for the AnacomAI class.
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        logger.addHandler(console_handler)

        return logger
