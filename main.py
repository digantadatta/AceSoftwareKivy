from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from myfirebase import MyFirebase

import requests
import json
import numpy as np
import pandas as pd


class HomeScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass


class InfoScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

GUI=Builder.load_file('main.kv')

class MainApp(App):
    def build(self):
        self.my_firebase=MyFirebase()
        return GUI
    def change_screen(self,screen_name):
        #get screen manager from kv file
        screen_manager=self.root.ids['screen_manager']
        screen_manager.current=screen_name


MainApp().run()