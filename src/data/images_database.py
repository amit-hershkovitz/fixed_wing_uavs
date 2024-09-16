import sqlite3
import time


class ImagesDatabase:
    def __init__(self, root_folder: str, database_name: str):
        self.root_folder = root_folder
        self.database_name = database_name

        self._create_images_table()
        self._create_data_sources_table()

    def add_source(self, source_path, source_type):
        add_time = time.strftime('%Y-%m-%d %H:%M:%S')
        with sqlite3.connect(f'{self.root_folder}/{self.database_name}.db') as conn:
            conn.cursor().execute(f"""
                                INSERT INTO DataSources (source_path, source_type, added)
                                VALUES ('{source_path}', '{source_type}', '{add_time}')
                                """
                                  )
            conn.commit()

    def create_empty_image_entry(self) -> int:
        create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        with sqlite3.connect(f'{self.root_folder}/{self.database_name}.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                                INSERT INTO Images (image_path, source_id, created)
                                VALUES (NULL, NULL, '{create_time}')
                                """
                           )
            conn.commit()

        return cursor.lastrowid

    def insert_image(self, image_id: int, image_path: str, source_type: str):
        with sqlite3.connect(f'{self.root_folder}/{self.database_name}.db') as conn:
            conn.cursor().execute(f"""
                                UPDATE Images 
                                SET source_path = '{image_path}'
                                    source_type = '{source_type}'
                                WHERE image_id = {image_id}
                                """
                                  )
            conn.commit()

    def _create_data_sources_table(self):
        with sqlite3.connect(f'{self.root_folder}/{self.database_name}.db') as conn:
            conn.cursor().execute("""
                                CREATE TABLE IF NOT EXISTS DataSources (
                                    source_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    source_path TEXT UNIQUE,
                                    source_type TEXT,
                                    added DATETIME
                                )
                                """
                                  )
            conn.commit()

    def _create_images_table(self):
        with sqlite3.connect(f'{self.root_folder}/{self.database_name}.db') as conn:
            conn.cursor().execute("""
                                CREATE TABLE IF NOT EXISTS Images (
                                    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    image_path TEXT UNIQUE,
                                    created DATETIME,
                                    source_id INTEGER
                                )
                                """
                                  )
            conn.commit()


if __name__ == '__main__':
    db = ImagesDatabase('/home/amit/codes/projects/python/fixed_wing_uavs/data', 'database')
    id = db.create_empty_image_entry()
    print(id)
