from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.window import Window

class GamingPanel(App):
    def build(self):
        Window.clearcolor = (0.04, 0.04, 0.07, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="[b]🔥 FREE FIRE PRACTICE PANEL 🔥[/b]",
            markup=True,
            font_size=22
        ))

        layout.add_widget(Label(
            text="Sensitivity Settings",
            font_size=20
        ))

        for name, value in [
            ("General", 95),
            ("Red Dot", 90),
            ("2X Scope", 85),
            ("4X Scope", 80),
            ("Sniper Scope", 50)
        ]:
            layout.add_widget(Label(text=name))

            slider = Slider(
                min=0,
                max=200,
                value=value
            )

            layout.add_widget(slider)

        self.total = 0
        self.headshots = 0

        self.stats = Label(
            text="Shots: 0 | Headshots: 0",
            font_size=17
        )
        layout.add_widget(self.stats)

        button = Button(
            text="🎯 RECORD HEADSHOT",
            size_hint_y=None,
            height=60
        )
        button.bind(on_press=self.record)
        layout.add_widget(button)

        return layout

    def record(self, instance):
        self.total += 1
        self.headshots += 1
        self.stats.text = (
            f"Shots: {self.total} | "
            f"Headshots: {self.headshots}"
        )

GamingPanel().run()
