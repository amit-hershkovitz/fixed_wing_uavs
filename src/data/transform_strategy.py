from abc import ABC, abstractmethod
import os

from image_processing import convert_to_jpg


class TransformStrategy(ABC):
    @abstractmethod
    def transform(self, image_paths: list[str, ...]) -> list[str, ...]:
        pass


class DefaultTransformStrategy(TransformStrategy):
    def transform(self, image_paths: list[str, ...]) -> list[str, ...]:
        converted_paths = []
        for path in image_paths:
            _, ext = os.path.splitext(path)

            if ext != '.jpg':
                converted_path = convert_to_jpg(path)
                converted_paths.append(converted_path)
                os.remove(path)
            else:
                converted_paths.append(path)

        return converted_paths

