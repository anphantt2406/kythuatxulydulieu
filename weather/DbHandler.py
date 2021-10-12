import psycopg2
import json

class DbHandler:
    conn = ''

    def __init__(self):
        self.config = json.load(open('config\db_config.json'))

    def open_connection_db (self):
        self.conn = psycopg2.connect(database = self.config.get('database'), user = self.config.get('user'), password = self.config.get('password'), port = self.config.get('port') )
        print('Connect successfully..')

    def insertRecord(self, record_insert):
        sql = """ INSERT INTO weather_temp_his (city_id,
        weather_id,
        temp,
        feels_like,
        temp_min,
        temp_max,
        pressure,
        humidity,
        visibility,
        wind_speed,
        wind_deg,
        clouds,
        created_date) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.open_connection_db()
        cursor = self.conn.cursor()
        cursor.execute(sql,record_insert)
        self.conn.commit()
        self.conn.close()

