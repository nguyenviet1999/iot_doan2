from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder 
from kivy.config import Config
from kivy.core.audio import SoundLoader
import pyrebase
import threading
import time
from firebase import firebase
from kivy.core.window import Window
temp, hum, sign_app, status_light, sign_fan_app, status_fan = "", "", "", "","",""
sign_app, sign_fan_app, value_btn_light, sign_btn_light = "", "", "", None

app = firebase.FirebaseApplication("https://dht11-29479-default-rtdb.firebaseio.com/", None)

config = {
  "apiKey": "AIzaSyBtq5sxCa0Bx0EqG7UTYcnmxeW70JMW79c",
  "authDomain": "dht11-29479.firebaseapp.com",
  "databaseURL": "https://dht11-29479-default-rtdb.firebaseio.com",
  "projectId": "dht11-29479",
  "storageBucket": "dht11-29479.appspot.com",
  "messagingSenderId": "605861105328",
  "appId": "1:605861105328:web:41afb27bb16029de63f575",
  "measurementId": "G-BJ6FGB0QRQ"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


class Door(Screen):
    pass
class Bed_room(Screen):
    pass
class Kitchen_room(Screen):
    pass
class Hello(Screen):
    def __init__(self, **kwargs):
        super(Hello, self).__init__(**kwargs)
        Clock.schedule_interval(self.statusLight, 0.01)
        #Clock.schedule_interval(self.statusfan, 1)
        Clock.schedule_interval(self.change_temp_hum, 2)
    
    def event_button_light(self, *args):
        global value_btn_light, database, sign_btn_light, sign_app, status_light
        
        if value_btn_light == 1:
            sign_btn_light = 0
            sign_app = "off"
        if value_btn_light == 0:
            sign_btn_light = 1
            sign_app = "on"

    def event_button_fan(self, *args):
        global sign_fan_app, database, flag_fan
        print("fan")
    
    def statusLight(self, *args):
        global sign_app, value_btn_light, status_light, sign_btn_light
        if sign_app == "on" or status_light == "on":
            self.ids.btn_light.text_color = (242/255, 217/255, 116/255,1)
            self.ids.cover_light.text_color = (242/255, 217/255, 116/255,1)
            self.ids.card_coverlight.opacity = 0.5
            value_btn_light = 1
            sign_app = ""
        if sign_app == "off" or status_light == "off":
            value_btn_light = 0
            sign_app = ""
            self.ids.btn_light.text_color = (83/255, 78/255, 82/255,1)
            self.ids.cover_light.text_color = (238/255, 237/255, 237/255,1)
            self.ids.card_coverlight.opacity = 0.2
        

    def statusfan(self, *args):
        global status_fan
        print(status_fan)
        if status_fan == "on":
            self.ids.switch_fan.active = True
        else:
            self.ids.switch_fan.active = False
    
    def change_temp_hum(self, *args):
        global temp, hum
        self.ids.label_temp.text = temp
        self.ids.label_hum.text = hum

class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        self.theme_cls.primary_palette = 'Gray'
        self.theme_cls.primary_hue = '800'
        screen = Builder.load_file("helper.kv")
        self.theme_cls.theme_style = 'Light'
        return screen
    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

def get_data():
    global temp, hum, database, status_light, status_fan, sign_fan_app, sign_app, flag_light, app
    while True:
        data = database.child("DHT11").get()
        hum = data.val()["hum"]
        temp = data.val()["temp"]
        status_light = data.val()["status_light"]
        status_fan = data.val()["status_fan"]
        #sign_app = data.val()["sign_app"]
        sign_fan_app = data.val()["sign_fan_app"]
        time.sleep(0.05)

def send_data():
    global value_btn_light, database, sign_btn_light, app
    flag1, flag2 = False, False
    while True:
        if sign_btn_light == 0 and flag1 == False:
            print("off")
            app.put("/DHT11", "sign_app", "off_light")
            sign_btn_light = None
        if sign_btn_light == 1 and flag2 == False:
            print("on")
            app.put("/DHT11", "sign_app", "on_light")
            sign_btn_light = None
        time.sleep(0.05)

threading.Thread(target=get_data).start()
threading.Thread(target=send_data).start()
DemoApp().run()