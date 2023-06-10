from kivy.properties import StringProperty

from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    pass


class RegistrationScreen(MDScreen):
    pass


class Password(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
