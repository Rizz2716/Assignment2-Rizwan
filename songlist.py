# createSongList class in this file

from song import Song


class Songlist:

    def __init__(self, filename):

        self.list_of_songs = []

        in_file = open(filename, 'r')
        #reading the file

        #To do: extracting the line and splitting the line to extract the information


    def save_song_list(self, filename):

        output_file = open(filename, 'w')
        #writing into the file

        #to do: write y or n according to the learned or unlearned file


    def sort_songs_by_title(self):
        #sorting according to the title

    def sort_songs_by_artist(self):
        # sorting according to the artist

    def sort_songs_by_year(self):
        #sorting according to the year

    def get_number_of_songs_learned(self):
        #counting the number of songs that have been learned

    def add_song(self, new_song):
        #adding a song to the list


    def delete_song(self, existing_song):
        #deleting the song, if the song already exists

