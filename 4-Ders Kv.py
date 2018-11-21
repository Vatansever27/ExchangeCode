from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

class Cizim(Widget):
    def on_touch_down(self, touch):
        with self.canvas:

            touch.ud["line"] = Line(points = (touch.x , touch.y))

    def on_touch_move(self, touch):

        touch.ud["Line"].points += (touch.x , touch.y)

class Fare(App):
    def build(self):
        return Cizim()




if __name__ == "__main__":
    Fare().run()



# Çalışmıyor :)
