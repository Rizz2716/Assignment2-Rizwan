# createSongList class in this file

from song import Song


class Songlist:

    def __init__(self, filename):

        self.list_of_songs = []

        in_file = open(filename, 'r') #reading the file

        for line in in_file: #extracting the line
            temp_song_info = line.split(',') #splitting the line to extract the information
            new_song = Song(temp_song_info[0], temp_song_info[1], temp_song_info[2])
            temp_song_info[3] = temp_song_info[3].strip('\n')
            if temp_song_info[3] == "y":
                new_song.learn()
            self.list_of_songs.append(new_song)

        in_file.close()

    def save_song_list(self, filename):

        output_file = open(filename, 'w') #writing into the file

        for song in self.list_of_songs: #to write y or n according to the learned or unlearned file

            if song.learned:
                song_learned = "y"
            else:
                song_learned = "n"

            print("{},{},{},{}".format(song.name, song.artist, song.year, song_learned), file=output_file)

        output_file.close()

    def sort_songs_by_title(self): #sorting according to the title
        self.list_of_songs = sorted(self.list_of_songs, key=Song.get_name)
        return True

    def sort_songs_by_artist(self): # sorting according to the artist
        self.list_of_songs = sorted(self.list_of_songs, key=Song.get_artist)
        return True

    def sort_songs_by_year(self): #sorting according to the year
        self.list_of_songs = sorted(self.list_of_songs, key=Song.get_year)
        return True

    def get_number_of_songs_learned(self): #counting the number of songs that have been learned
        learned_songs = 0
        for song in self.list_of_songs:
            if song.learned:
                learned_songs += 1
        return learned_songs

    def add_song(self, new_song): #adding a song to the list
        self.list_of_songs.append(new_song)

    def delete_song(self, existing_song): #deleting the song, if the song already exists
        for i, song in enumerate(self.list_of_songs):
            if song == existing_song:
                del self.list_of_songs[i]
                break
