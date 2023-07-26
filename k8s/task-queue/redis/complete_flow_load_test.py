import gevent
import requests
import time
from locust import HttpUser, task, constant, events

def async_success(name:str, start_time:float, resp):
    events.request.fire(
        request_type=resp.request.method,
        name=name,
        response_time=int((time.monotonic() - start_time) * 1000),
        response_length=len(resp.content), 
        # no exception = successs
    )

def async_failure(name:str, start_time:float, resp, message:str):
    events.request.fire(
        request_type=resp.request.method,
        name=name,
        response_time=int((time.monotonic() - start_time) * 1000),
        response_length=len(resp.content), 
        exception=Exception(message), # throw exception = failure
    )

class reportService(HttpUser):
    
    wait_time = constant(1)

    def _do_async_thing_handler(self, timeout:float=600):
        post_resp = requests.post(self.host + 'report')
        if not post_resp.status_code == 200:
            return
        id = post_resp.json()['report_id']
        print(id)

        # Now poll for an ACTIVE status
        start_time = time.monotonic()
        end_time = start_time + timeout
        while time.monotonic() < end_time:
            r = requests.get(self.host + 'report/' + id)
            if r.status_code == 200 and r.json()['result'] != None:
                async_success('POST /report/ID - async', start_time, post_resp)
                return

            # IMPORTANT: Sleep must be monkey-patched by gevent (typical), or else
            # use gevent.sleep to avoid blocking the world.
            gevent.sleep(1)
        async_failure('POST /report/ID - async', start_time, post_resp, 'Failed - timed out after %s seconds' % timeout)

    @task
    def do_async_thing(self):
        gevent.spawn(self._do_async_thing_handler)