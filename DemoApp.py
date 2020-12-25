from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder 
from kivy.config import Config
from kivy.core.window import Window
Window.size = (312, 534)
#Builder String 
helper = '''
ScreenManager:
    Hello:
<Hello>:
    name: 'hello'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        left_action_items: [["account-arrow-left", lambda x: nav_drawer.toggle_nav_drawer()]]
                        title: "Hoang Viet's Smart Home"
                        md_bg_color: .2, .2, .2, 1
                        specific_text_color: 1, 1, 1, 1
                    MDBottomNavigation:
                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Living Room'
                            icon: 'folder-home'
                            Image:
                                size_hint: 1,1
                                pos_hint: {'center_x': .5, 'center_y': .8}
                                source: 'living.jpg'
                            MDCard:
                                orientation: 'vertical'
                                pos_hint: {'center_x': .3, 'center_y': .3}
                                size_hint: .25,.25
                                pos: 70,100
                                elevation: 10
                                MDLabel:
                                    text: "Temperature"
                                    halign: 'center'
                                    pos_hint: {'center_x': .5, 'center_y':.8}
                                    theme_text_color: 'Custom'
                                    text_color : 46/255, 123/255, 50/255,1
                                    bold: True
                                    font_size : '13'
                           
                                MDLabel:
                                    text: "30"
                                    bold: True
                                    halign: 'center'
                                    pos_hint: {'center_x': .5, 'center_y':.5}
                                    font_size : '25'
                                    theme_text_color: 'Custom'
                                    text_color: 51/255, 51/255, 51/255,1
                            MDCard:
                                orientation: 'vertical'
                                pos_hint: {'center_x': .7, 'center_y': .3}
                                size_hint: .25,.25
                                pos: 230,100
                                elevation: 10
                                MDLabel:
                                    text: "Humidity"
                                    halign: 'center'
                                    pos_hint: {'center_x': .5, 'center_y':.8}
                                    theme_text_color: 'Custom'
                                    text_color : 46/255, 123/255, 50/255,1
                                    bold: True
                                    font_size : '13'
                           
                                MDLabel:
                                    text: "85"
                                    bold: True
                                    halign: 'center'
                                    pos_hint: {'center_x': .5, 'center_y':.5}
                                    font_size : '25'
                                    theme_text_color: 'Custom'
                                    text_color: 51/255, 51/255, 51/255,1
                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'Bed Room'
                            icon: 'folder-home'
                            Image:
                                pos_hint: {'center_x': .5, 'center_y': .5}
                                size: '200dp', '200dp'
                                source: 'bedroom.jpg'
                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'KitChen Room'
                            icon: 'folder-home'
                            Image:
                                pos_hint: {'center_x': .5, 'center_y': .5}
                                size: '150dp', '100dp'
                                source: 'kitchen.jpg'
                            
           
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'daidien.jpg'
                MDLabel:
                    text: 'Nguyễn Văn Hoàng Việt'
                    font_style: "Button"
                    size_hint_y: None
                    halign: 'center'
                    height: self.texture_size[1]
                MDLabel:
                    text: '106170276'
                    halign: 'center'
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'K157/28 Pham Nhu Xuong'
                            font_style: "Caption"
                            IconLeftWidget:
                                icon: 'home'
                        OneLineIconListItem:
                            text: 'Da Nang University'
                            font_style: "Caption"
                            IconLeftWidget:
                                icon: 'school'
                        OneLineIconListItem:
                            text:'0795565299'
                            font_style: "Caption"
                            IconLeftWidget:
                                icon: 'phone'
                        OneLineIconListItem:
                            text:'Dark mode'
                            font_style: "Caption"
                            IconLeftWidget:
                                icon: 'theme-light-dark'
                            MDSwitch:
                                width: dp(40)
                                pos_hint: {'center_x':.7,'center_y': .5}
                                on_active: app.check(*args)

'''
class Hello(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class MainWindow(Screen):
    pass
#sm = ScreenManager()

#sm.add_widget(Hello(name = 'hello'))
#sm.add_widget(Bye(name='bye'))

class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    data = {
        'lightbulb-on-outline':'',
        'note': 'Remember to turn OFF',
}
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '800'
 #       screen = Screen()
        screen = Builder.load_string(helper)
  #      screen.add_widget(help_str)
        self.theme_cls.theme_style = 'Light'
        return screen
    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'
    def callback(self, instance):
        print(instance.icon)

DemoApp().run()