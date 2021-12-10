import contextlib
import time

import aiohttp
import asyncio
import requests
from requests_futures import sessions

#URL = "http://httpbin.org/delay/1"
URL = "http://172.18.43.192:8080/async"  # delay 3 sec 
TRIES = 10

### http client cmp, https://julien.danjou.info/python-and-fast-http-clients/
### using proxy in all, by set env: 
### export HTTP_PROXY="http://172.18.43.51:8080", or 
### coding it at requests/session level 

@contextlib.contextmanager
def report_time(test):
    t0 = time.time()
    yield
    print("Time needed for `%s' called: %.2fs"
          % (test, time.time() - t0))


with report_time("serialized"):
    for i in range(TRIES):
        requests.get(URL)


session = requests.Session()
with report_time("Session"):
    for i in range(TRIES):
        session.get(URL)     # share the same connection 


session = sessions.FuturesSession(max_workers=2)
with report_time("FuturesSession w/ 2 workers"):
    futures = [session.get(URL)  # using thread pool for parallel 
               for i in range(TRIES)]
    for f in futures:
        f.result()


session = sessions.FuturesSession(max_workers=TRIES)
with report_time("FuturesSession w/ max workers"):
    futures = [session.get(URL)
               for i in range(TRIES)]
    for f in futures:
        f.result()


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.read()

loop = asyncio.get_event_loop()
with report_time("aiohttp"):
    loop.run_until_complete(
        asyncio.gather(*[get(URL)
                         for i in range(TRIES)]))
                         
                         
### streamed async                           
async def gets(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.content.read()

loop = asyncio.get_event_loop()
with report_time("aiohttp-stream"):
    tasks = [asyncio.ensure_future(get(URL))]
    loop.run_until_complete(asyncio.wait(tasks))
    print("Results: %s" % [task.result() for task in tasks])
