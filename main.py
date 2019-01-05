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

        for i, song in enumerate(MySongList.list_of_songs):
            new_song_button = Button(text="\"{}\" by {} ({})".format(song.name, song.artist, song.year), id=str(i),
                                     on_release=self.learn_this_song)
            if song.learned:
                new_song_button.text += " (learned)"
                new_song_button.background_color = (1, 0, 0, 1)
            else:
                new_song_button.background_color = (0, 0, 1, 1)

            self.root.ids.songs_list_box.add_widget(new_song_button)

        self.root.ids.learned_songs.text = "Learned: {}".format(MySongList.get_number_of_songs_learned())
        self.root.ids.to_learn_songs.text = "To Learn: {}".format(len(MySongList.list_of_songs)
                                                        - MySongList.get_number_of_songs_learned())

        return self.root

    def add_song_to_list(self, name, artist, year): #validating the input of the user
        if not name.isspace() and not artist.isspace() and not year.isspace():
            if not name == "" and not artist == "" and not year == "":
                if year.isdigit():
                    if 1000 <= int(year) <= 9999:
                        new_song = Song(name, artist, year)
                        MySongList.add_song(new_song)

                        if self.root.ids.sort_label.text == "Title":
                            MySongList.sort_songs_by_title()
                        elif self.root.ids.sort_label.text == "Artist":
                            MySongList.sort_songs_by_artist()
                        elif self.root.ids.sort_label.text == "Year":
                            MySongList.sort_songs_by_year()

                        self.root.ids.songs_list_box.clear_widgets()

                        for i, song in enumerate(MySongList.list_of_songs):
                            new_song_button = Button(text="\"{}\" by {} ({})".format(song.name, song.artist, song.year),
                                                     id=str(i), on_release=self.learn_this_song)
                            if song.learned:
                                new_song_button.text += " (learned)"
                                new_song_button.background_color = (1, 0, 0, 1)
                            else:
                                new_song_button.background_color = (0, 0, 1, 1)
                            self.root.ids.songs_list_box.add_widget(new_song_button)

                        MySongList.save_song_list("songs.csv")

                        self.root.ids.learned_songs.text = "Learned: {}".format(MySongList.get_number_of_songs_learned())
                        self.root.ids.to_learn_songs.text = "To Learn: {}".format(len(MySongList.list_of_songs)
                                                                        - MySongList.get_number_of_songs_learned())
                    else:
                        self.root.ids.learning_info.text = "Year should be between 1000 and 9999."
                else:
                    self.root.ids.learning_info.text = "Please enter a valid number."
            else:
                self.root.ids.learning_info.text = "All fields must be completed."
        else:
            self.root.ids.learning_info.text = "All fields must be completed."

        self.root.ids.input_name.text = "" #resetting the values of the fields after identifying the error
        self.root.ids.input_artist.text = ""
        self.root.ids.input_year.text = ""

    def resort_order_of_song(self): #resetting the order after adding the song
        if self.root.ids.sort_label.text == "Year":
            self.root.ids.sort_label.text = "Title"
            MySongList.sort_songs_by_title()
        elif self.root.ids.sort_label.text == "Title":
            self.root.ids.sort_label.text = "Artist"
            MySongList.sort_songs_by_artist()
        elif self.root.ids.sort_label.text == "Artist":
            self.root.ids.sort_label.text = "Year"
            MySongList.sort_songs_by_year()

        self.root.ids.songs_list_box.clear_widgets()

        for i, song in enumerate(MySongList.list_of_songs):
            new_song_button = Button(text="\"{}\" by {} ({})".format(song.name, song.artist, song.year), id=str(i),
                                     on_release=self.learn_this_song)
            if song.learned:
                new_song_button.text += " (learned)"
                new_song_button.background_color = (1, 0, 0, 1)
            else:
                new_song_button.background_color = (0, 0, 1, 1)
            self.root.ids.songs_list_box.add_widget(new_song_button)

    def learn_this_song(self, instance): #displaying that you have already learned the song if the user selects the learned song to learn it again
        if MySongList.list_of_songs[int(instance.id)].learn():
            instance.background_color = (1, 0, 0, 1)
            instance.text += " (learned)"
            self.root.ids.learning_info.text = "You have learned \"{}\" by {} ({})" \
                                               ".".format(MySongList.list_of_songs[int(instance.id)].name,
                                                          MySongList.list_of_songs[int(instance.id)].artist,
                                                          MySongList.list_of_songs[int(instance.id)].year)
        else:
            self.root.ids.learning_info.text = "You have already learned \"{}\" by {} ({})" \
                                               ".".format(MySongList.list_of_songs[int(instance.id)].name,
                                                          MySongList.list_of_songs[int(instance.id)].artist,
                                                          MySongList.list_of_songs[int(instance.id)].year)

        self.root.ids.learned_songs.text = "Learned: {}".format(MySongList.get_number_of_songs_learned())
        self.root.ids.to_learn_songs.text = "To Learn: {}".format(len(MySongList.list_of_songs)
                                                        - MySongList.get_number_of_songs_learned())

        MySongList.save_song_list("songs.csv") # saving the song to the file

    def clear_new_song_fields(self): # clearing the fields
        self.root.ids.input_name.text = ""
        self.root.ids.input_artist.text = ""
        self.root.ids.input_year.text = ""


SongLearnApp().run()
