from abc import ABC, abstractmethod
import os
import subprocess

from video_processing import download_video, extract_video_frames


class ExtractStrategy(ABC):
    @abstractmethod
    def extract(self, source: str, destination: str, source_id: int):
        pass


class YoutubeDownloadStrategy(ExtractStrategy):
    def extract(self, source: str, destination: str, source_id):
        video = download_video(source, destination)
        image_paths = extract_video_frames(video, destination, source_id)

        return image_paths


class LocalImageStrategy(ExtractStrategy):
    def extract(self, source: str, destination: str, source_id: int):
        _, filename = os.path.split(source)
        os.rename(source, os.path.join(destination, filename))

