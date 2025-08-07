import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import pytesseract
from PIL import Image
import io
import requests

class OCRApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.btn = Button(text="Rozpoznaj tekst", size_hint=(1, 0.2))
        self.btn.bind(on_press=self.recognize_text)
        self.result = Label(text="Wynik pojawi się tutaj", size_hint=(1, 0.8))
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.result)
        return self.layout

    def recognize_text(self, instance):
        try:
            # Pobierz przykładowy obraz
            url = "https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/phototest.tif"
            response = requests.get(url)
            img = Image.open(io.BytesIO(response.content))
            
            # Rozpoznaj tekst
            text = pytesseract.image_to_string(img)
            self.result.text = f"Rozpoznany tekst:\n\n{text}"
        except Exception as e:
            self.result.text = f"Błąd: {str(e)}"

if __name__ == "__main__":
    OCRApp().run()
