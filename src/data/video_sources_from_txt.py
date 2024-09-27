import os.path
import sys

from images_database import ImagesDatabase


def video_sources_from_txt(txt_file_path: str, database_path: str):
    db = ImagesDatabase(database_path)
    with open(txt_file_path, 'r') as file:
        for line in file:
            url = line.strip()
            db.insert_source(url, 'video')


if __name__ == '__main__':
    video_sources_from_txt(sys.argv[1], sys.argv[2])
