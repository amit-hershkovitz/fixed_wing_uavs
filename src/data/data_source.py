from abc import ABC, abstractmethod
from datetime import datetime

from functools import partial

from images_database import ImagesDatabase
from extract_strategy import YoutubeDownloadStrategy, LocalImageStrategy
from transform_strategy import DefaultTransformStrategy
from load_strategy import DefaultLoadStrategy


class DataSource:
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

        self._extract_strategy = extract_strategy()
        self._transform_strategy = transform_strategy()
        self._load_strategy = load_strategy()

    def extract(self, destination) -> list[str, ...]:
        return self._extract_strategy.extract(self.source_path, destination, self.source_id)

    def transform(self, paths) -> list[str, ...]:
        return self._transform_strategy.transform(paths)

    def load(self, source_paths, destination):
        self._load_strategy.load(source_paths, destination, self.source_id, self.database)


VideoSource = partial(DataSource,
                      extract_strategy=YoutubeDownloadStrategy,
                      transform_strategy=DefaultTransformStrategy,
                      load_strategy=DefaultLoadStrategy
                      )

LocalImageSource = partial(DataSource,
                           extract_strategy=LocalImageStrategy,
                           transform_strategy=DefaultTransformStrategy,
                           load_strategy=DefaultLoadStrategy
                           )


class DataSourceFactory(ABC):
    @abstractmethod
    def create(self, database, source_id, source_path, source_type, added):
        pass


class VideoSourceFactory(DataSourceFactory):
    def create(self, database, source_id, source_path, source_type, added):
        return VideoSource(database=database,
                           source_id=source_id,
                           source_path=source_path,
                           source_type=source_type,
                           added=added)


class LocalImageSourceFactory(DataSourceFactory):
    def create(self, database, source_id, source_path, source_type, added):
        return LocalImageSource(database=database,
                                source_id=source_id,
                                source_path=source_path,
                                source_type=source_type,
                                added=added)
