import media    
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

lion_king = media.Movie("The Lion King",
                        "The story of a young lion cub's journey to adulthood",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

dark_knight = media.Movie("The Dark Knight",
                          "Local vigilante saves his hometown from an evil madman",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

rush_hour = media.Movie("Rush Hour",
                        "Crime-fighting duo search for a diplomat's kidnapped daughter",
                        "https://upload.wikimedia.org/wikipedia/en/5/55/Rush_hour_ver2.jpg",
                        "https://www.youtube.com/watch?v=JMiFsFQcFLE")

madagascar = media.Movie("Madagascar",
                         "A group of zoo animals explore a foreign land",
                         "https://upload.wikimedia.org/wikipedia/en/3/36/Madagascar_Theatrical_Poster.jpg",
                         "https://www.youtube.com/watch?v=_FvCgabQVjA")

# Generate an HTML webpage
movies = [toy_story, lion_king, dark_knight, rush_hour, madagascar]
fresh_tomatoes.open_movies_page(movies)



                        
                     


