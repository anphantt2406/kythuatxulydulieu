import requests

class ApiHandler:

    apiUrl=''

    def __init__(self, id, token):
        self.id = id
        self.token = token
        self.apiUrl = "http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}".format(id, token)

    def getWeatherData(self):
        print(self.apiUrl)
        response = requests.get(self.apiUrl)
        return response.json()





