from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
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


class ItemBackdropBackLayer(ThemableBehavior, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            for item in self.parent.children:
                if item.selected_item:
                    item.selected_item = False
            self.selected_item = True
        return super().on_touch_down(touch)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "KivyMD Example - Backdrop"
        self.theme_cls.primary_palette = "DeepPurple"
        super().__init__(**kwargs)

    def build(self):
        self.root = ExampleBackdrop()


if __name__ == "__main__":
    MainApp().run()