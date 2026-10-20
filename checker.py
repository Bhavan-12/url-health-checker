import requests
import time

urls = ["https://google.com", "https://github.com", "https://youtube.com", "https://thissitedoesnotexist12345.com"]

for url in urls:
    try:
        start = time.perf_counter()
        response = requests.get(url, timeout=5)
        end = time.perf_counter()
        print(url, response.status_code, end - start)
    except:
        print(url, "FAILED")