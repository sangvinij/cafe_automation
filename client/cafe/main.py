import re
import webbrowser

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import AsyncImage

from kivy_garden.mapview import MapMarker, MapView

from kivymd.app import MDApp
from kivymd.font_definitions import fonts
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.tab import MDTabsBase

from requests.exceptions import JSONDecodeError

from .api_requests import get_latitude_and_longitude, \
    get_list_of_addresses, \
    get_list_of_categories, \
    get_list_of_links, \
    get_menu_items, \
    get_user, login, logout, register
from .login import LoginScreen, RegistrationScreen


class MainScreen(MDScreen):
    pass


class Tab(MDFloatLayout, MDTabsBase):
    pass


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class AddressMapView(MapView):
    pass


class SonBox(MDBoxLayout):
    pass


class Cards(MDGridLayout):
    def __init__(self):
        super().__init__()
        menu_items = get_menu_items()
        for item in range(len(menu_items)):
            self.add_widget(
                MDCard(
                    MDBoxLayout(
                        AsyncImage(
                            source=f'{menu_items[item]["image"]}',
                        ),
                        MDLabel(
                            font_size=10,
                            size_hint_y=.2,
                            text=f'{menu_items[item]["title"]}',
                        ),
                        MDLabel(
                            text=f'{menu_items[item]["price"]}',
                            font_size=12,
                            size_hint_y=.4,
                        ),
                        MDRectangleFlatButton(
                            text='В корзину',
                            md_bg_color='red',
                            text_color='white',
                        ),
                        orientation='vertical',
                        padding='5dp'
                    )
                ))


class CafeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file('cafe/main.kv')
        self.screen_manager = MDScreenManager()
        self.login_screen = LoginScreen(name='login_screen')
        self.registration_screen = RegistrationScreen(name='registration_screen')
        self.main_screen = MainScreen(name='main_screen')
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Red'
        self.token = None

    def sign_in(self):
        try:
            self.token = login(phone_number=self.login_screen.ids.user.text,
                               password=self.login_screen.ids.passw.ids.password.text)
            self.screen_manager.current = 'main_screen'
            self.screen_manager.transition.direction = 'left'
            return self.token

        except KeyError:
            self.login_screen.ids.user.error = True
            self.login_screen.ids.user.helper_text = 'Неправильный номер телефона или пароль'

    def build(self):
        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.registration_screen)
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.current = 'main_screen'
        self.screen_manager.current = 'login_screen'
        return self.screen_manager

    def on_start(self):
        list_of_categories = get_list_of_categories()
        for category in list_of_categories:
            self.main_screen.ids.tabs.add_widget(
                Tab(
                    MDLabel(
                        text='title'
                    ),
                    title=f"[size=18][font={fonts[-1]['fn_regular']}][/size][/font] {category}"
                )
            )

        self.main_screen.ids.main_box.add_widget(
            MDBoxLayout(
                MDBoxLayout(
                    Cards(),
                    orientation='vertical',
                    size_hint_y=1,
                    padding=8),
            )
        )

        address_map = AddressMapView()
        list_of_addresses = get_list_of_addresses()
        for address in list_of_addresses:
            latitude, longitude = get_latitude_and_longitude(address)
            map_marker = MapMarker(lon=longitude, lat=latitude)
            address_map.add_marker(map_marker)

        self.main_screen.ids.address.add_widget(address_map)

    def sign_up(self):
        phone_number = self.registration_screen.ids.phone_number
        password = self.registration_screen.ids.reg_password
        first_name = self.registration_screen.ids.first_name
        last_name = self.registration_screen.ids.last_name
        email = self.registration_screen.ids.email
        # phone_validator = r'^(\+375)(29|25|44|33)(\d{7})$'
        # password_validator = re.compile('^(?=.*?[a-z])(?=.*?[0-9]).{5,}$')
        # phone_validation = re.fullmatch(phone_validator, self.registration_screen.ids.phone_number.text)
        # if not password_validator.fullmatch(password.text) or not phone_validation:
        #     phone_number.error = True
        #     password.error = True
        #     phone_number.helper_text = 'Введите номер телефона в указанном формате'
        #     password.helper_text = 'минимум 5 символов, 1 латинская буква и 1 цифра'

        registration = register(phone_number.text,
                                password.text,
                                first_name=first_name.text,
                                last_name=last_name.text,
                                email=email.text)
        data = registration.json()

        if registration:
            self.screen_manager.current = 'login_screen'

        else:
            if 'phone_number' in data:
                phone_number.error = True
                phone_number.helper_text = data['phone_number'][0]
            elif 'password' in data:
                password.error = True
                password.helper_text = data['password'][0]

    def log_out(self):
        try:
            logout(self.token)

        except JSONDecodeError:
            pass

        finally:
            self.screen_manager.current = 'login_screen'
            self.screen_manager.transition.direction = 'right'

    def on_tab_switch(self, instance_tabs, instance_tab,
                      instance_tab_label, tab_text):
        pass

    def links(self, index):
        dict_of_social_media = get_list_of_links()
        if index == 1:
            webbrowser.open(dict_of_social_media['vk'])
        else:
            webbrowser.open(dict_of_social_media['instagram'])
