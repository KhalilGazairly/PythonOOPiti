import psycopg2

class connection:
    def __init__(self, user, dbname, host, passwd, port):
        self.user = user
        self.dbname = dbname
        self.host = host
        self.passwd = passwd
        self.port = port
        self.con = ''

    def open_connection(self):
        print("Start connection ...")
        self.con = psycopg2.connect(
            database = self.dbname,
            user = self.user,
            host = self.host,
            password = self.passwd,
            port = self.port
            )
        print('connected successefully')
        return self.con
    
    def close_connection(self):
        self.con.close()
        print('Connection is closed now')
        return 1
    
    def insert(self, table_name, *args):
        exec = self.con.cursor()
        statement = f'insert into {table_name} values {str(args)};'
        exec.execute(statement)
        self.con.commit()
        print('inserted successefully')

    def delete(self, table_name, condition):
        exec = self.con.cursor()
        statement = f'delete from {table_name} where {condition};'
        exec.execute(statement)
        self.con.commit()
        print('deleted successefully')
        
    def update(self, table_name, new_vales, condition):
        exec = self.con.cursor()
        statement = f'update {table_name} set {new_vales} where {condition};'
        exec.execute(statement)
        self.con.commit()
        print('updated successefully')

    def select(self, table_name, condition):
        exec = self.con.cursor()
        statement = f'select * from {table_name} where {condition};'
        exec.execute(statement)
        self.con.commit()
        print('selected successefully')