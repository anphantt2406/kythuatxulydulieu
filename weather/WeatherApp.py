import json
import schedule
import time

import sys
import time
import signal


from ApiHandler import ApiHandler
from DataProcessing import ProcessData

def processData():
    for id in ids:
        # print(id.get('id'))
        weather = ApiHandler(id.get('id'), token)
        # result = weather.getWeatherData()
        dataProccessing = ProcessData(weather.getWeatherData())
        dataProccessing.process_data()

def cb_sigint_handler(signum, stack):
    global is_interrupted
    print ("SIGINT received")
    is_interrupted = True

if __name__ == "__main__":
    apiConfig = json.load(open("config/api_config.json","r"))
    ids = apiConfig.get('ids')
    token = apiConfig.get('APPID')

    schedule.every().days.at("09:30:00").do(processData)
    schedule.every().days.at("10:00:00").do(processData)
    schedule.every().days.at("10:30:00").do(processData)
    schedule.every().days.at("11:00:00").do(processData)
    schedule.every().days.at("11:30:00").do(processData)
    schedule.every().days.at("13:30:00").do(processData)
    schedule.every().days.at("14:00:00").do(processData)
    schedule.every().days.at("14:30:00").do(processData)
    schedule.every().days.at("15:00:00").do(processData)
    schedule.every().days.at("15:30:00").do(processData)
    schedule.every().days.at("16:00:00").do(processData)
    schedule.every().days.at("16:30:00").do(processData)
    schedule.every().days.at("17:00:00").do(processData)
    schedule.every().days.at("17:30:00").do(processData)

    # schedule.every().days.at("17:31:00").do(processData)

    # schedule.every(5).seconds.do(processData)
    is_interrupted = False
    signal.signal(signal.SIGINT, cb_sigint_handler)
    while(1):
        # do stuff here 
        print ("processing...")
        schedule.run_pending()
        time.sleep(1)
        if is_interrupted:
            print ("Exiting..")
            # do clean up
            sys.exit(0)

    # while 1:
    #     schedule.run_pending()
    #     time.sleep(10)  # seconds nghỉ trước khi chạy tác vụ tiếp theo


# python gameover.py => Ctrl + C to exiting => run in terminal 