class MovieReview:
    def __init__(self, movie, story, actors, music):
        self.movie_name = movie

        self.story_rating = story
        self.actor_rating = actors
        self.music_rating = music
        
        self.avg = int((self.story_rating + self.actor_rating + self.music_rating/3))

     self.myrating = {
    "Movie Name" : self.movie_name,
    "Story rating" : self.story_rating,
    "Actory Rating" : self.actor_rating,
    "Music Rating" : self.music_rating,
    "Avg Rating" : self.avg

     }