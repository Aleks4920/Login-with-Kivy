from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.core.window import Window


Window.clearcolor = (0, 0, 0.1, 0.9)



class login(Screen):
    password = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(login, self).__init__(**kwargs)


    def submit(self):
        if self.password.text != "":
            self.reset()
    def reset(self):
        self.password.text = ""

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass
kv = Builder.load_file("pv2.kv")
sm = WindowManager()

screens = [login(name="login"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class Project(App):
    def build(self):
        return sm



if __name__ == "__main__":
    Project().run()
