from abc import ABC, abstractmethod
import os
from shutil import copy

from video_processing import download_video, extract_video_frames, reject_frames


class ExtractStrategy(ABC):
    @abstractmethod
    def extract(self, source: str, destination: str, source_id: int) -> list[str, ...]:
        pass


class YoutubeDownloadStrategy(ExtractStrategy):
    def extract(self, source: str, destination: str, source_id: int) -> list[str, ...]:
        video_path = download_video(source, destination)
        image_paths = extract_video_frames(video_path, destination, source_id)
        os.remove(video_path)
        image_paths = reject_frames(image_paths)
        return image_paths


class LocalImageStrategy(ExtractStrategy):
    def extract(self, source: str, destination: str, source_id: int) -> list[str]:
        _, filename = os.path.split(source)
        path = os.path.join(destination, filename)
        copy(source, path)

        return [path]
