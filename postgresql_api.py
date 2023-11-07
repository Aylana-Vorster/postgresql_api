import psycopg2

class postgresql:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.db = database
        self.user = user
        self.password = password

    def connect(self):
        conn = psycopg2.connect( 
                host=self.host,
                port=self.port,
                database=self.db,
                user=self.user,
                password=self.password)
        return conn
    

    def PSQL_Query(query,self):
        # Very general way of conducting a query where the query is passed as if you would run it with the query tool in pgadmin4
        # See an example in the README file
        conn = self.connect()

        try:
            cur = conn.cursor()
            cur.execute(query)
            data = cur.fetchall()
        except Exception as e:
            return e
        finally:
            conn.close()
        return data

    def PSQL_Insert(query, self):
        #An insert will not return data, so this function is to commit changes to the DB only
        conn = self.connect()

        try:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()  # Commit the changes for an insert operation
        except Exception as e:
            return e
        finally:
            conn.close()
            return 'OK'

    def PSQL_Reset_Table(tablename,self):
        # This deletes all data in a whole table
        conn = self.connect()

        try:
            cur = conn.cursor()
            cur.execute('''
                        DELETE FROM public."'''+tablename+  '''"                   
                        ''' )
            conn.commit()  # Commit the changes for a delete operation
            return 'OK'
        except Exception as e:
            return e
        finally:
            conn.close

