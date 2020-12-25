from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder 
from kivy.config import Config
import pyrebase
import threading
import time

temp, hum, sign_app = "", "", ""

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

class Hello(Screen):
    def __init__(self, **kwargs):
        super(Hello, self).__init__(**kwargs)
        Clock.schedule_interval(self.change_temp_hum, 2)

    def event_button_light(self, checkbox, value):
        global sign_app
        if value:
            sign_app = "on"
        else:
            sign_app = "off"
        print(sign_app)
        

    def change_temp_hum(self, *args):
        global temp, hum
        self.ids.label_temp.text = temp
        self.ids.label_hum.text = hum

class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    data = {
        'lightbulb-on-outline':'',
        'note': 'Remember to turn OFF',
}
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '400'
        screen = Builder.load_file("helper.kv")
        self.theme_cls.theme_style = 'Light'
        return screen
    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'
    def callback(self, instance):
        print(instance.icon)

def get_data():
    global temp, hum, database
    while True:
        data = database.child("DHT11").get()
        hum = data.val()["hum"]
        temp = data.val()["temp"]
        print(hum)
        print(temp)
        time.sleep(1)

def send_data():
    global sign_app, database
    while True:
        if sign_app == "on":
            database.child("DHT11").update({"sign_app":"on"})
        if sign_app == "off":
            database.child("DHT11").update({"sign_app":"off"})
        time.sleep(0.5)

threading.Thread(target=get_data).start()
threading.Thread(target=send_data).start()
DemoApp().run()