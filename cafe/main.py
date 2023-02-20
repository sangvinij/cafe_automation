import webbrowser

from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


class Tab(MDFloatLayout, MDTabsBase):
    pass


class CafeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('cafe/main.kv')

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Red'
        return self.screen

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        print('tab clicked! ' + tab_text)

    def links(self, index):
        if index == 1:
            webbrowser.open('http://vk.com/sangvinij')
        else:
            webbrowser.open('http://instagram.com/sangvinij')
