import os
from abc import ABC, abstractmethod
from images_database import ImagesDatabase


class LoadStrategy(ABC):
    @abstractmethod
    def load(self, source_paths: list[str, ...], destination: str, source_id: int, database: ImagesDatabase):
        pass


class DefaultLoadStrategy(LoadStrategy):
    def load(self,
             source_paths: list[str, ...],
             destination: str,
             source_id: int,
             database: ImagesDatabase):

        for path in source_paths:
            image_id = database.create_empty_image_entry()
            standardized_path = f'{destination}/{image_id}.jpg'
            os.rename(path, standardized_path)
            database.insert_image(image_id, standardized_path, source_id)

