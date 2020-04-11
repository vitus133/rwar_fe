from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior


# Your layouts.
Builder.load_file("layout.kv")

# Usage example of MDBackdrop.
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
        

    def build(self):
        self.root = ExampleBackdrop()
    
    def debug_print(self):
        tb = ThemableBehavior()
        print(tb.__dir__())


if __name__ == "__main__":
    MainApp().run()