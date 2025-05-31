import os
import psycopg2
from psycopg2.extensions import connection
from .connection_factory import ConnectionFactory


class Connection(ConnectionFactory):

    def __init__(self):
        super().__init__()
        self.__user = os.getenv("POSTGRES_USER")
        self.__password = os.getenv("POSTGRES_PASSWORD")
        self.__host = os.getenv("POSTGRES_HOST")
        self.__port = os.getenv("POSTGRES_PORT")
        self.__dbname = os.getenv("POSTGRES_DATABASE")

    def create_connection(self) -> connection:
        """
        Function to create a connection to the PostgreSQL database using psycopg2.
        Returns:
            connection: A psycopg2 connection object.
        Raises:
            psycopg2.Error: If there is an error while connecting to the database.
        Example:
            >>> conn = Connection().engine()
            >>> cursor = conn.cursor()
            >>> cursor.execute("SELECT * FROM your_table")
            >>> results = cursor.fetchall()
            >>> print(results)
        """

        return psycopg2.connect(
            dbname=self.__dbname,
            user=self.__user,
            password=self.__password,
            host=self.__host,
            port=self.__port,
        )
