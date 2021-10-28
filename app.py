from flask import Flask
from time import sleep
from os import environ
import update_bot

while True: 
    update_bot.main()
    nap_time = 21601
    sleep(nap_time)

'''
app = Flask(__name__)

@app.route("/")
def index():
    while True: 
        update_bot.main()
        nap_time = 21601
        sleep(nap_time)

if __name__ == "__main__":
    app.run(port="5000")
    '''