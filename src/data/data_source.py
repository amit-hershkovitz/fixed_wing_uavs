from abc import ABC, abstractmethod
from datetime import datetime

from functools import partial

from images_database import ImagesDatabase
from extract_strategy import YoutubeDownloadStrategy, LocalImageStrategy
from transform_strategy import DefaultTransformStrategy
from load_strategy import DefaultLoadStrategy


class DataSource(ABC):
    def __init__(self,
                 database: ImagesDatabase,
                 source_id: int,
                 source_path: str,
                 source_type: str,
                 added: datetime,
                 extract_strategy,
                 transform_strategy,
                 load_strategy):

        self.database = database
        self.source_id = source_id
        self.source_path = source_path
        self.source_type = source_type
        self.added = added

        self._extract_strategy = extract_strategy
        self._transform_strategy = transform_strategy
        self._load_strategy = load_strategy

    def extract(self, destination):
        self._extract_strategy.extract(self.source_path, destination)

    def transform(self, destination, *paths):
        self._transform_strategy.transform()

    def load(self):
        self._load_strategy.load()


VideoSource = partial(DataSource,
                      extract_stretegy=YoutubeDownloadStrategy,
                      transform_strategy=DefaultTransformStrategy,
                      load_strategy=DefaultLoadStrategy
                      )


LocalImageSource = partial(DataSource,
                           extract_strategy=LocalImageStrategy,
                           transform_strategy=DefaultTransformStrategy,
                           load_strategy=DefaultLoadStrategy
                           )
