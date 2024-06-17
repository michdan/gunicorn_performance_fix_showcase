Just run 'docker-compose build' and after 'docker-compose up'.
There will be two server instances and two client instances.
One server with Gunicorn with this fix: https://github.com/benoitc/gunicorn/pull/3228 
and client sending requests in loop,
another with Gunicorn 22.0.0 version and client sending requests in loop.
Settings for both servers are the same.
We can see that in Gunicorn 22.0.0, worker waits for long time to finish restart while 
in Gunicorn fixed version restart is very fast (without errors on the client side).