import sys

from images_database import ImagesDatabase
from data_source import VideoSourceFactory, LocalImageSourceFactory


def process_data(database_path: str, raw_destination: str, interim_destination: str):
    db = ImagesDatabase(database_path)
    unprocessed_sources = db.get_unprocessed_sources()
    source_factories = {'video': VideoSourceFactory(), 'local_image': LocalImageSourceFactory()}

    for unprocessed_source in unprocessed_sources:

        source_id, source_path, source_type, added = unprocessed_source
        source_factory = source_factories[source_type]
        source = source_factory.create(db, source_id, source_path, source_type, added)

        if source_type == 'video':
            ans = input('Video source detected. would you like to process it? [y/n]')
            if ans == 'n':
                break

        extracted_paths = source.extract(raw_destination)
        transformed_paths = source.transform(extracted_paths)
        source.load(transformed_paths, interim_destination)


if __name__ == '__main__':
    process_data(sys.argv[1], sys.argv[2], sys.argv[3])

