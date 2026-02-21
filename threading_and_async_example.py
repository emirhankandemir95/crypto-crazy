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


class ThreadingDownloader(threading.Thread):
    json_array = []
    
    
    def __init__(self, url):
        super().__init__()
        self.url = url
        
    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array

def get_data_threading(urls):
    st = time.time()
    threads = []
    
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        print(t)
        
    et = time.time()
    estimated_time = et - st
    print(f"Executed in: {estimated_time} seconds.")
    
    
urls = ["https://postman-echo.com/delay/5"] * 10
# get_data_sync(urls) #60 seconds for whole process.
get_data_threading(urls) #6 seconds for whole process.