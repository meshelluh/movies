# -*- coding: utf-8 -*-
# 
# ABOUT THIS FILE: 
# Run this file first in order to create fresh_tomatoes.html. 
# This file holds our movie instances, and puts movies in a list, and 
# calls the external rendering function. 

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A little boy named Andy loves to be in his room, playing with his toys, especially his doll named Woody. But, what do the toys do when Andy is not with them, they come to life. Woody believes that he has life (as a toy) good. However, he must worry about Andy's family moving, and what Woody does not know is about Andy's birthday party. Woody does not realize that Andy's mother gave him an action figure known as Buzz Lightyear, who does not believe that he is a toy, and quickly becomes Andy's new favorite toy.",  # noqa
                        "http://img1.wikia.nocookie.net/__cb20140816182710/disney/images/4/4c/Toy-story-movie-posters-4.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

age_of_adaline = media.Movie("Age of Adaline",
                        "After miraculously remaining 29 years old for almost eight decades, Adaline Bowman has lived a solitary existence, never allowing herself to get close to anyone who might reveal her secret. But a chance encounter with charismatic philanthropist Ellis Jones reignites her passion for life and romance. When a weekend with his parents threatens to uncover the truth, Adaline makes a decision that will change her life forever.",  # noqa
                        "http://ia.media-imdb.com/images/M/MV5BMTAzMTQzMTA2MjheQTJeQWpwZ15BbWU4MDk2MTg2MzUx._V1_SX214_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=slkDzs9vUY8")

it_follows = media.Movie("It Follows",
                        "For nineteen-year-old Jay, Autumn should be about school, boys and week-ends out at the lake. But after a seemingly innocent sexual encounter, she finds herself plagued by strange visions and the inescapable sense that someone, something, is following her. Faced with this burden, Jay and her friends must find a way to escape the horrors, that seem to be only a few steps behind.",  # noqa
                        "http://ia.media-imdb.com/images/M/MV5BMTUwMDEzNDI1MF5BMl5BanBnXkFtZTgwNzAyODU5MzE@._V1_SX640_SY720_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=9tyMi1Hn32I")

citizenfour = media.Movie("CitizenFour",
                        "In January 2013, Laura Poitras started receiving anonymous encrypted e-mails from CITIZENFOUR, who claimed to have evidence of illegal covert surveillance programs run by the NSA in collaboration with other intelligence agencies worldwide. Five months later, she and reporters Glenn Greenwald and Ewen MacAskill flew to Hong Kong for the first of many meetings with the man who turned out to be Edward Snowden. She brought her camera with her. The resulting film is history unfolding before our eyes.",  # noqa
                        "http://resizing.flixster.com/9kOIeftR2d1dq7D9I8s-RrQ1p9Y=/800x1174/dkpu1ddg7pbsk.cloudfront.net/movie/11/18/10/11181051_ori.jpg",  # noqa
                        "https://www.youtube.com/watch?v=SImMDZV3xPk")

the_duff = media.Movie("The Duff",
                        "Bianca is a content high school senior whose world is shattered when she learns the student body knows her as 'The DUFF' (Designated Ugly Fat Friend) to her prettier, more popular friends. Now, despite the words of caution from her favorite teacher, she puts aside the potential distraction of her crush, Toby, and enlists Wesley, a slick but charming jock, to help reinvent herself. To save her senior year from turning into a total disaster, Bianca must find the confidence to overthrow the school's ruthless label maker Madison.", # noqa
                        "http://ia.media-imdb.com/images/M/MV5BMTc3OTg3MDUwN15BMl5BanBnXkFtZTgwMTAwMTkxNDE@._V1_SX640_SY720_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=cISh0wmeZBQ")

big_eyes = media.Movie("Big Eyes",
                        "In San Francisco in the 1950s, Margaret was a woman trying to make it on her own after leaving her husband with only her daughter and her paintings. She meets gregarious ladies' man and fellow painter Walter Keane in a park while she was struggling to make an impact with her drawings of children with big eyes. The two quickly become a pair with outgoing Walter selling their paintings and quiet Margaret holed up at home painting even more children with big eyes. But Walter's actually selling her paintings as his own.",  # noqa
                        "https://upload.wikimedia.org/wikipedia/en/3/39/Big_Eyes_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=R8HsTKJHZ7Y")


movies = [toy_story, age_of_adaline, it_follows, citizenfour, the_duff, big_eyes]
fresh_tomatoes.open_movies_page(movies)
