import pandas as pd
from ..database.connection import Connection


class SQLHandler:

    def __init__(self):
        pass

    def fetch_data(self, sql: str) -> pd.DataFrame:
        conn = Connection().create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            if not data:
                raise ValueError("No data returned from the query.")
            columns = (
                [desc[0] for desc in cursor.description]
                if cursor.description is not None
                else []
            )
            df = pd.DataFrame(data, columns=columns)
            return df
        except Exception as e:
            raise ConnectionError(e)
        finally:
            cursor.close()
            conn.close()
