import threading
import requests
import time

def get_data_sync(urls):
    st = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    et = time.time()
    estimated_time = et - st
    print(f"Executed in: {estimated_time} seconds.")
    return json_array

urls = ["https://postman-echo.com/delay/5"] * 10
get_data_sync(urls) #60 seconds for whole process.