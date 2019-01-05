# create Song class in this file



class Song:

    def __init__(self, name, artist, year, learned=False): #initializer
        self.name = name
        self.artist = artist
        self.year = year
        self.learned = learned

    def __str__(self):
        #formatting and printing


    def __eq__(self, other):
        #equalizing function to help delete the duplicate songs

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_year(self):
        return self.year

    def learn(self):
        if not self.learned:
            self.learned = True
            return True
        else:
            return False
