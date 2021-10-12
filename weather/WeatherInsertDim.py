import json
from datetime import datetime

from DbHandler import DbHandler
from ApiHandler import ApiHandler

def insert_tables():
    sql_insert_city_dim = """ INSERT INTO weather_city_dim (
        id,
        city_name,
        city_code,
        longtitude,
        lattitude,
        active,
        created_date ) VALUES (%s,%s,%s,%s,%s,%s,%s)   """

    sql_insert_des_dim = """ INSERT INTO weather_description_dim (
        id,
        city_id,
        main_weather,
        description,
        created_date ) VALUES (%s,%s,%s,%s,%s)   """
    
    #Open db connection
    dbOperation = DbHandler()
    dbOperation.open_connection_db()
    cursor = dbOperation.conn.cursor()

    #call api to get data
    apiConfig = json.load(open("config/api_config.json",'r'))
    ids = apiConfig.get('ids')
    token = apiConfig.get('APPID')

    for id in ids:
        callAPI = ApiHandler(id.get('id'), token)
        data = callAPI.getWeatherData()
        # print("data %s" %(id), data)
        record_insert_des_dim = (
        data.get('weather')[0].get('id'),
        data.get('id'),
        data.get('weather')[0].get('main'),
        data.get('weather')[0].get('description'),
        datetime.fromtimestamp(data.get('dt') ) )

        record_insert_city_dim = (
        data.get('id'),
        data.get('name'),
        data.get('cod'),
        data.get('coord').get('lon'),
        data.get('coord').get('lat'),
        1,
        datetime.fromtimestamp(data.get('dt') ) )


        cursor.execute(sql_insert_city_dim, record_insert_city_dim)
        cursor.execute(sql_insert_des_dim, record_insert_des_dim)

    dbOperation.conn.commit()
    dbOperation.conn.close()

    print('Insert successfully...')

if __name__ == "__main__":
    insert_tables()
