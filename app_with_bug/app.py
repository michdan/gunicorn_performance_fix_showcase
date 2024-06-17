import multiprocessing


from flask import Flask
import time
from gevent import config, get_hub
from gevent.events import IEventLoopBlocked
import gevent.util
import logging
import zope.event
from greenlet import greenlet

# Should each hub start a native OS thread to monitor for problems?
# Such a thread will periodically check to see if the event loop is blocked for longer
# than max_blocking_time, producing output on the hub’s exception stream (stderr by default)
# if it detects this condition
# http://www.gevent.org/configuration.html#gevent._config.Config.monitor_thread
config.monitor_thread = True
config.max_blocking_time = 2


# start the monitor thread
hub = get_hub()
monitor = hub.start_periodic_monitoring_thread()





def create_app():
    # create and configure the app
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/')
    def hello():
        #time.sleep(5)
        return 'Hello, World!'

    return app





