from datetime import datetime
from DbHandler import DbHandler

class ProcessData:
    
    def __init__(self, data):
        self.data = data

    def process_data(self):
        
        record_to_insert = (
        self.data.get('id')
        ,self.data.get('weather')[0].get('id')
        ,self.data.get('main').get('temp')
        ,self.data.get('main').get('feels_like')
        ,self.data.get('main').get('temp_min')
        ,self.data.get('main').get('temp_max')
        ,self.data.get('main').get('pressure')
        ,self.data.get('main').get('humidity')
        ,self.data.get('visibility')
        ,self.data.get('wind').get('speed')
        ,self.data.get('wind').get('deg')
        ,self.data.get('clouds').get('all')
        ,datetime.fromtimestamp(self.data.get('dt'))
        )

        dbhandler =  DbHandler() # Khoi tạo đối tượng
        dbhandler.insertRecord(record_to_insert)