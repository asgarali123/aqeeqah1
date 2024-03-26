import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from datetime import datetime, timedelta

class MainScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

class AqeeqahApp(App):
    def build(self):
        # Set background image
        Window.clearcolor = (0, 0, 0, 0)  # Set background color to transparent
        Window.max_width = Window.width  # Set app width to max width of device
        Window.max_height = Window.height  # Set app height to max height of device
        
        # Screen manager
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ResultScreen(name='result'))
        
        return sm

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout for the main screen
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Background image
        self.background_image = "masjid.png"  # Replace "masjid.png" with your actual filename
        background = Image(source=self.background_image, size_hint=(1, 1))  # Adjusted size_hint
        layout.add_widget(background)
        
        # Date input
        layout.add_widget(Label(text='When was the child born?', color=(1, 1, 1, 1), bold=True, font_name='Arial'))
        self.date_input = TextInput(hint_text='DD/MM/YYYY', multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.date_input)
        
        # Sunset time selection
        layout.add_widget(Label(text='Was the child born before sunset?', color=(1, 1, 1, 1), bold=True, font_name='Arial'))
        self.sunset_spinner = Spinner(text='Yes', values=('Yes', 'No'), size_hint=(1, None), height=40)
        layout.add_widget(self.sunset_spinner)
        
        # Gender selection
        layout.add_widget(Label(text='Is the baby a boy or a girl?', color=(1, 1, 1, 1), bold=True, font_name='Arial'))
        self.gender_spinner = Spinner(text='Boy', values=('Boy', 'Girl'), size_hint=(1, None), height=40)
        layout.add_widget(self.gender_spinner)
        
        # Submit button
        submit_button = Button(text='Submit', size_hint=(1, None), height=40)
        submit_button.bind(on_press=self.show_result)
        layout.add_widget(submit_button)
        
        self.add_widget(layout)
    
    def show_result(self, instance):
        # Get user inputs
        dob = self.date_input.text
        gender = self.gender_spinner.text
        before_sunset = self.sunset_spinner.text == 'Yes'
        
        # Convert input date string to datetime object
        dob_date = datetime.strptime(dob, '%d/%m/%Y')
        
        # Add days based on sunset
        if before_sunset:
            # Add 6 days
            due_date = dob_date + timedelta(days=6)
        else:
            # Add 7 days
            due_date = dob_date + timedelta(days=7)
        
        # Convert due date back to string
        due_date_str = due_date.strftime('%d/%m/%Y')
        
        # Determine sacrifice requirement
        if gender == 'Boy':
            sacrifice = 'You have to sacrifice 2 sheep or goats'
        else:
            sacrifice = 'You have to sacrifice 1 sheep or goat'
        
        # Display result in pop-up
        result_text = f"Masha Allah! \nMay Allah bless your baby {gender}.\n{sacrifice}. \nThe day of the aqeeqah will be on {due_date_str}"
        popup = Popup(title='Result', content=Label(text=result_text, color=(1, 1, 1, 1), bold=True, font_name='Arial'), size_hint=(None, None), size=(400, 200))
        popup.open()

# Run the app
if __name__ == '__main__':
    AqeeqahApp().run()
