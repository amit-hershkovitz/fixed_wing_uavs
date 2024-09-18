import sys
import os

from images_database import ImagesDatabase


def image_sources_from_local_directory(directory_path: str, database_path: str):
    db = ImagesDatabase(database_path)

    # List all files
    file_paths = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if
                  os.path.isfile(os.path.join(directory_path, f))]

    for file_path in file_paths:
        db.insert_source(file_path, 'local_image')


if __name__ == '__main__':
    image_sources_from_local_directory(sys.argv[1], sys.argv[2])
