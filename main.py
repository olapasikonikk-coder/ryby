import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        btn = Button(text="Kliknij mnie", size_hint=(1, 0.2))
        result = Label(text="Wynik pojawi się tutaj", size_hint=(1, 0.8))
        
        def on_press(instance):
            result.text = "Przycisk kliknięty!"
        
        btn.bind(on_press=on_press)
        layout.add_widget(btn)
        layout.add_widget(result)
        return layout

if __name__ == "__main__":
    SimpleApp().run()
