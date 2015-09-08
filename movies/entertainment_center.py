# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://img1.wikia.nocookie.net/__cb20140816182710/disney/images/4/4c/Toy-story-movie-posters-4.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

age_of_adaline = media.Movie("Age of Adaline",
                        "After miraculously remaining 29 years old for almost eight decades, Adaline Bowman (Blake Lively) has lived a solitary existence, never allowing herself to get close to anyone who might reveal her secret.",
                        "http://ia.media-imdb.com/images/M/MV5BMTAzMTQzMTA2MjheQTJeQWpwZ15BbWU4MDk2MTg2MzUx._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=slkDzs9vUY8")

it_follows = media.Movie("It Follows",
                        "After carefree teenager Jay (Maika Monroe) sleeps with her new boyfriend, Hugh (Jake Weary), for the first time, she learns that she is the latest recipient of a fatal curse.",
                        "http://ia.media-imdb.com/images/M/MV5BMTUwMDEzNDI1MF5BMl5BanBnXkFtZTgwNzAyODU5MzE@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=9tyMi1Hn32I")

citizenfour = media.Movie("CitizenFour",
                        "CITIZENFOUR is a real life thriller, unfolding by the minute, giving audiences unprecedented access to filmmaker Laura Poitras and journalist Glenn Greenwald’s encounters with Edward Snowden in Hong Kong.",
                        "http://resizing.flixster.com/9kOIeftR2d1dq7D9I8s-RrQ1p9Y=/800x1174/dkpu1ddg7pbsk.cloudfront.net/movie/11/18/10/11181051_ori.jpg",
                        "https://www.youtube.com/watch?v=SImMDZV3xPk")

the_duff = media.Movie("The Duff",
                        "Bianca (Mae Whitman) is a content high school senior whose world is shattered when she learns the student body refers to her as ‘The DUFF’ (Designated Ugly Fat Friend) to her prettier, more popular friends.",
                        "http://ia.media-imdb.com/images/M/MV5BMTc3OTg3MDUwN15BMl5BanBnXkFtZTgwMTAwMTkxNDE@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=cISh0wmeZBQ")

big_eyes = media.Movie("Big Eyes",
                        "From the whimsical mind of director Tim Burton, BIG EYES tells the outrageous true story of one of the most epic art frauds in history.",
                        "https://upload.wikimedia.org/wikipedia/en/3/39/Big_Eyes_poster.jpg",
                        "https://www.youtube.com/watch?v=R8HsTKJHZ7Y")


#the_duff.show_trailer()

movies = [toy_story, age_of_adaline, it_follows, citizenfour, the_duff]
fresh_tomatoes.open_movies_page(movies)
