from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KMS = 1.60934


class ConvertMilesKm(App):
    """ ConvertMilesKm is an app for converting miles to kilometres """
    result = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to KMs"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result = "0.0"
        return self.root

    def handle_conversion(self, value):
        """ Handle conversion, output result to self.result """
        try:
            result = float(value) * MILES_TO_KMS
            self.result = str(result)
        except ValueError:
            self.result = str(0.0)

    def handle_increment(self, increment):
        """ handle up/down button press, update the text input with new value, call conversion function """
        try:
            int(self.root.ids.input_miles.text)
        except ValueError:
            self.root.ids.input_miles.text = "0"

        number_of_miles = int(self.root.ids.input_miles.text) + increment
        self.root.ids.input_miles.text = str(number_of_miles)

        self.handle_conversion(self.root.ids.input_miles.text)


ConvertMilesKm().run()
