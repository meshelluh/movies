import webbrowser


class Movie ():
	""" 
	This classs creates the main movie object 
	that holds each movie's information.
    """
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  #noqa
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		"""
        This plays the trailer for the movie.
        """
		webbrowser.open(self.trailer_youtube_url)
