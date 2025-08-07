from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Kliknij mnie!")
        btn.bind(on_press=self.on_press)
        layout.add_widget(btn)
        return layout

    def on_press(self, instance):
        print("Przycisk kliknięty!")

if __name__ == "__main__":
    MyApp().run()
