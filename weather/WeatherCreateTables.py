from DbHandler import DbHandler

def create_tables():
    sql_weather_city_dim = '''CREATE TABLE IF NOT EXISTS weather_city_dim
    (
    id	VARCHAR PRIMARY KEY ,
    city_name	VARCHAR(50) 	,	
    city_code	INTEGER  		,	
    longtitude	decimal(18,3)	,	
    lattitude	decimal(18,3)	,	
    active	INTEGER	,	
    created_date	timestamp		
    ) ;'''

    sql_weather_des_dim = '''CREATE TABLE IF NOT EXISTS weather_description_dim
    (
    id	VARCHAR	Primary key ,
    city_id	VARCHAR	,
    main_weather	VARCHAR	,
    description	VARCHAR	,
    created_date	timestamp	
    ); '''

    sql_weather_temp_his = '''CREATE TABLE IF NOT EXISTS weather_temp_his
    (
    id	int GENERATED ALWAYS AS IDENTITY Primary key,
    city_id	varchar	,
    weather_id	varchar	,
    temp	decimal(18,2),
    feels_like float,
    temp_min decimal(18,2), 
    temp_max decimal(18,2),
    pressure	intEGER	,
    humidity	intEGER	,
    visibility	intEGER	,
    wind_speed	decimal(18,2)	,
    wind_deg	decimal(18,2)	,
    clouds	intEGER	,
    created_date	timestamp without time zone

    );'''

    # open connection to db
    dbOperation = DbHandler()
    dbOperation.open_connection_db()

    cursor = dbOperation.conn.cursor()
    cursor.execute(sql_weather_city_dim)
    cursor.execute(sql_weather_des_dim)
    cursor.execute(sql_weather_temp_his)
    dbOperation.conn.commit()
    dbOperation.conn.close()
    
    print('Create tables successfully... ')

if __name__ == '__main__':
    create_tables()