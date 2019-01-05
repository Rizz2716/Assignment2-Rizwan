"""
Name: Mohamed Rizwan
Date: 05/01/2019
Brief Project Description: The program reads the songs from the songs file and it displays the list of learned and
unlearned songs. The user gets the opportunity to add new songs and he also gets the opportunity to sort the song display
according to the artist or the year or the title. It displays the number of learned and unlearned songs and changes colour
according to whether it is learned or unlearned.
GitHub URL:
"""

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button

from song import Song
from songlist import Songlist

Config.set('graphics', 'resizable', False)

version = "2.0"
program_author = "Rizwan"

MySongList = Songlist("songs.csv")


class SongLearnApp(App):
    def build(self):
        Window.size = (1280, 720)
        self.title = "Songs to be learnt {} - by {}".format(version, program_author) #displaying on the top
        self.root = Builder.load_file('app.kv') #loading the kv file

        MySongList.sort_songs_by_year()

        #To do: sort songs by title, year and artist

    def add_song_to_list(self, name, artist, year):
        # To do: allow user to add song, validate the input and make sure all fields are entered



    def resort_order_of_song(self):
        #resetting the order after adding the song


    def learn_this_song(self, instance):
        #displaying that you have already learned the song if the user selects the learned song to learn it again



    def clear_new_song_fields(self):
        # clearing the fields



SongLearnApp().run()
