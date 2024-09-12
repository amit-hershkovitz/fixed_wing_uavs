import sqlite3
import time


class ImagesDatabase:
    def __init__(self, root_folder: str, database_name: str):
        self.root_folder = root_folder
        self.database_name = database_name
        self.connection = sqlite3.connect(f'{root_folder}/{database_name}.db')
        self.cursor = self.connection.cursor()

        self._create_images_table()
        self._create_data_sources_table()

    def add_source(self, source_path, source_type):
        add_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute(f"""
                            INSERT INTO DataSources (source_path, source_type, added)
                            VALUES ('{source_path}', '{source_type}', '{add_time}')
                            """
                            )

    def _create_data_sources_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS DataSources (
                                source_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                source_path TEXT UNIQUE,
                                source_type TEXT,
                                added DATETIME
                            )
                            """
                            )

    def _create_images_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Images (
                                image_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                image_path TEXT UNIQUE,
                                created DATETIME,
                                source_id INTEGER,
                                image_size INTEGER,
                                image_width INTEGER,
                                image_height INTEGER
                            )
                            """
                            )
