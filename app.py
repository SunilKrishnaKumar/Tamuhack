import time, os
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from utils import find_new_users
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

scheduler = BackgroundScheduler()
scheduler.add_job(func=find_new_users, trigger="interval", seconds=3)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
