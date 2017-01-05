import mraa
from datetime import date
import tornado.web
import tornado.escape
import tornado.ioloop
import time
class servomotor:
    def __init__(self,pin):
        self.pin=pin
        self.pwm=mraa.Pwm(pin)
        self.pwm.period_ms(20)
        self.pwm.enable(True)

    def set_angle(self,value):
        self.value=value
        self.pwm.write(float(0.019+.0005*(value)))
        print("the motor has been set to following angle: ",value)
        time.sleep(1)
       
a=servomotor(5)
a.set_angle(0)
time.sleep(1)
a.set_angle(180)
time.sleep(1)

class versionhandler(tornado.web.RequestHandler):
    def get(self):
        response={'version':'1.0','last_build': date.today().isoformat()}
        self.write(response)

class put_angle(tornado.web.RequestHandler):
    def put(self,value):
        int_value=int(value)
        a=servomotor(5)
        a.set_angle(int_value)

application=tornado.web.Application([
    (r"/put_angle/([0-9]+)", put_angle),
    (r"/version",versionhandler)])
print("listening at port 8888")
application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
