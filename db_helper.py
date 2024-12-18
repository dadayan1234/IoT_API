import sqlite3

class DBHelper:
    def __init__(self, db_name):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS chart_data (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                chart_name TEXT NOT NULL,
                                value REAL NOT NULL,
                                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                              )''')
            conn.commit()

    def insert_data(self, chart_name, value):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO chart_data (chart_name, value) VALUES (?, ?)', (chart_name, value))
            conn.commit()

    def get_filtered_data(self, chart_name=None, start_time=None, end_time=None):
        query = 'SELECT id, chart_name, value, timestamp FROM chart_data WHERE 1=1'
        params = []
        if chart_name:
            query += ' AND chart_name = ?'
            params.append(chart_name)
        if start_time:
            query += ' AND timestamp >= ?'
            params.append(start_time)
        if end_time:
            query += ' AND timestamp <= ?'
            params.append(end_time)

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [{'id': row[0], 'chart_name': row[1], 'value': row[2], 'timestamp': row[3]} for row in rows]
