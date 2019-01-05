# create your Song class in this file



class Song:

    def __init__(self, name, artist, year, learned=False): #initializer
        self.name = name
        self.artist = artist
        self.year = year
        self.learned = learned

    def __str__(self): #formatting and printing
        return "{0:30} - {1:30} ({2}) {3}".format(self.name, self.artist, self.year, self.learned)

    def __eq__(self, other): #equalizing function to help delete the duplicate songs
        if self.name == other.name:
            if self.artist == other.artist:
                if self.year == other.year:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

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
