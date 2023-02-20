from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout


class Password(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class Login(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('login.kv')

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Red'
        return self.screen

    def sign_in(self):
        print('login button pressed',
              self.screen.ids.user.text,
              self.screen.ids.passw.ids.password.text)

    def registration(self):
        # print('registration button pressed')
        ...


if __name__ == '__main__':
    Login().run()
