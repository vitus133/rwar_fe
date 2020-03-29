from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.dropdownitem import MDDropDownItem

# Your layouts.
Builder.load_file("layout.kv")

# Usage example of MDBackdrop.
Builder.load_file("backdrop.kv")


class ExampleBackdrop(Screen):
    pass

class SelectableItem(ThemableBehavior):
    selected_item = BooleanProperty(False)
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            for item in self.parent.children:
                if item.selected_item:
                    item.selected_item = False
            self.selected_item = True
        return super().on_touch_down(touch)


class ItemBackdropBackLayer(SelectableItem, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)


class TextItemScreen2(ThemableBehavior, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    hint_text = StringProperty()


class CheckBoxOption(SelectableItem, BoxLayout):
    pass


class DropDownOption(MDDropDownItem, SelectableItem):
    pass


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