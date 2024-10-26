from peewee import PostgresqlDatabase
import socket, os

class DatabaseSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseSingleton._instance is None:
            DatabaseSingleton._instance = PostgresqlDatabase(
                'pokedex',
                user='postgres',
                password=os.getenv('SENHA_POSTGRES'),
                host=socket.gethostbyname(socket.gethostname()),
                port=5432
            )
        return DatabaseSingleton._instance