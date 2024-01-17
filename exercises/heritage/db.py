class Database:

    def connect(self):
        pass

    def disconnect(self):
        pass

    def execute(self):
        pass


class MySQLDatabase(Database):

    def connect(self):
        print('Connecting to MySQL database...')

    def disconnect(self):
        print('Disconnecting from MySQL database...')

    def execute(self, query):
        print(f"Executing query '{query}' in MySQL database...")


class PostgreSQLDatabase(Database):

    def connect(self):
        print('Connecting to PostgreSQL database...')

    def disconnect(self):
        print('Disconnecting from PostgreSQL database...')

    def execute(self, query):
        print(f"Executing query '{query}' in PostgreSQL database...")
