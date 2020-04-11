from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.storage.jsonstore import JsonStore

# Layouts
Builder.load_file("layout.kv")

# Screens
Builder.load_file("backdrop.kv")


class ExampleBackdrop(Screen):
    pass


class BackLayerTextItem(ThemableBehavior, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    hint_text = StringProperty()


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "RWAR VPN"
        self.theme_cls.primary_palette = "BlueGray"
        super().__init__(**kwargs)
        self.store = JsonStore('rwar_vpn.json')
        self.store.store_load()

    def build(self):
        self.root = ExampleBackdrop()

    def store_kv(self, key: str, value: str):
        self.store.store_put(key, value)
        self.store.store_sync()


if __name__ == "__main__":
    MainApp().run()
