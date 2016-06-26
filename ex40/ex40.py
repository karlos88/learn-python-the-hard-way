# --------- Code from exercise ------------- #
# class Song(object):
#
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
#
# happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])
#
# bulls_on_parade = Song(["They rally around tha family",
#                         "With pockets full of shells"])
#
# happy_bday.sing_me_a_song()
#
# bulls_on_parade.sing_me_a_song()

# My own exercise

class Jukebox:
    def __init__(self, songs):
        '''
        Initializing jukebox, starting at track 1 (index 0)
        '''
        self.track_no = 0
        self.songs = songs
        self.set_lyrics()

    def next(self):
        '''
        Increment track by 1 and load lyrics;
        If already at last track - start album again at first track.
        If-else approach
        '''
        if self.track_no == (len(self.songs) - 1):
            self.track_no = 0
        else:
            self.track_no += 1

        self.set_lyrics()

    def back(self):
        '''
        Decrement track by 1 and load lyrics;
        If already at first track - do not decrement;
        If-else approach.
        '''

        if self.track_no == 0:
            pass # no need to do anything, it's already = 0
        else:
            self.track_no -= 1

        # This works too
        # if self.track_no != 0:
        #     self.track_no -= 1

        self.set_lyrics()

    def go_to_track(self, track_no):
        '''
        Go to selected track
        Intentionally no range checking so we can use try-catch in other function
        '''
        self.track_no = track_no
        self.set_lyrics()

    def go_to_first(self):
        '''
        Go to first track
        '''
        self.go_to_track(0)

    def set_lyrics(self):
        '''
        Load lyrics for selected track.
         If for some reason wrong index number for track was given - set it back to 0.
        '''
        try:
            self.lyrics = self.songs[self.track_no]
        except:
            print("Wrong track number, starting at 0...")
            self.go_to_first()
            self.lyrics = self.songs[self.track_no]

    def play(self):
        print(self.lyrics)


song_1 = "Song 1 lyrics: la, la, la la laaaa!"
song_2 = "Song 2 lyrics: ba dum, tsss!"
song_3 = "Song 3 lyrics: Ram pam pam"
song_4 = "Song 4 lyrics: LEEEEEROY JEEEENKINS!"
album = [song_1, song_2, song_3, song_4]

jukebox = Jukebox(album)
jukebox.play()
jukebox.next()
jukebox.play()
jukebox.next()
jukebox.play()
jukebox.next()
jukebox.play()
jukebox.next()
jukebox.play()
jukebox.next()
jukebox.play()
jukebox.next()
jukebox.play()
jukebox.back()
jukebox.play()
jukebox.back()
jukebox.play()
jukebox.back()
jukebox.play()
jukebox.back()
jukebox.play()
jukebox.go_to_track(10)
jukebox.play()
jukebox.go_to_track(2)
jukebox.play()
jukebox.go_to_first()
jukebox.play()