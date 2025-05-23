from abc import ABC, abstractmethod


class ConnectionFactory(ABC):
    """
    Abstract base class for creating database connections.
    """

    @abstractmethod
    def create_connection(self):
        """
        Create a database connection.
        """
        pass
