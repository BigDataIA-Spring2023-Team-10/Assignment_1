import unittest
import sqlite3

class TestSQLiteOperations(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(r"src\data\GEOSPATIAL_DATA.db")
        self.cursor = self.conn.cursor()
        
    def test_sqlite_connection(self):
        # Connect to the database (change the database file name as needed)
        
        # Check if the connection was successful
        self.assertTrue(self.conn is not None)
        
    def test_table_creation(self):
        self.cursor.execute('''DROP TABLE IF EXISTS test_table''')
        self.cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
        result = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_table'").fetchone()
        self.assertEqual(result[0], 'test_table')

    def test_insert_data(self):
        self.cursor.execute("INSERT INTO test_table (id, name) VALUES (1, 'John Doe')")
        result = self.cursor.execute("SELECT * FROM test_table").fetchone()
        self.assertEqual(result, (1, 'John Doe'))
        
    def tearDown(self):
        self.conn.close()
        
if __name__ == '__main__':
    unittest.main()
