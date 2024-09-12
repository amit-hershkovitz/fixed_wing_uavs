from abc import ABC, abstractmethod

from image_processing import convert_to_jpg


class TransformStrategy(ABC):
    @abstractmethod
    def transform(self, *image_paths):
        pass


class DefaultTransform(TransformStrategy):
    def transform(self, *image_paths):
        for path in image_paths:
            convert_to_jpg(path)

