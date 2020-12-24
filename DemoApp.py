from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
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
                                pos_hint: {'center_x': .5, 'center_y': .5}
                                source: 'living.jpg'
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
                    font_style: 'H5'
                    halign: 'center'
                    size_hint_y: None
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'K157/28 Pham Nhu Xuong'
                            IconLeftWidget:
                                icon: 'home'
                        OneLineIconListItem:
                            text: 'Da Nang University'
                            IconLeftWidget:
                                icon: 'school'
                        OneLineIconListItem:
                            text:'0795565299'
                            IconLeftWidget:
                                icon: 'phone'
                        OneLineIconListItem:
                            MDSwitch:
                                width: dp(40)
                                pos_hint: {'center_x':.5,'center_y': .5}
                                on_active: app.check(*args)

'''
class Hello(Screen):
    pass


#sm = ScreenManager()

#sm.add_widget(Hello(name = 'hello'))
#sm.add_widget(Bye(name='bye'))

class DemoApp(MDApp):
    def build(self):
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

DemoApp().run()