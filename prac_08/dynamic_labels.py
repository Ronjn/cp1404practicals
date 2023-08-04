from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "4th name"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # create a button for each data entry, specifying the text
            temp_label = Label(text=name)
            # add the button to the "entries_box" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
