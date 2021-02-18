import time
from datetime import datetime as dt

# hostsPath = r"C:\Windows\System32\..." версия для Виндоус
hostsPath = r"home/" # for linux
redirect = "127.0.0.1"
# 
websites = ["site1", "site2"]
while True:
    # 
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Sorry Not Allowrd...")
        # ....
    else:
        pass # coming soon...