import fresh_tomatoes
import media

#print( A_trip_to_jamaica.storyline)
# A_trip_to_jamaica.show_trailer()
A_trip_to_jamaica = media.Movie("A Trip to Jamaica",
                                    "A story of a boy and his toys that come to life",
                                    "https://upload.wikimedia.org/wikipedia/en/e/e6/A_Trip_to_Jamaica_poster.jpg",
                                    "https://www.youtube.com/watch?v=J9upTBWiW8I")

#print( half_of_a_yellow_sun.storyline)
# half_of_a_yellow_sun.show_trailer()

half_of_a_yellow_sun = media.Movie("Half of a yello sun",
                                    "A story of a boy and his toys that come to life",
                                    "https://upload.wikimedia.org/wikipedia/en/2/25/Half_of_a_Yellow_Sun.jpg",
                                    "https://www.youtube.com/watch?v=5wF4wU6HuUk")
#print(sin_city.storyline)
# sin_city.show_trailer()
sin_city = media.Movie("Sin City",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/9/9e/Sincitypostercast.jpg",
                        "https://www.youtube.com/watch?v=r0PDOQglpDQ")

#print(troy.storyline)
#troy.show_trailer()
troy = media.Movie("Troy",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b8/Troy2004Poster.jpg",
                     "https://www.youtube.com/watch?v=ekshABiptOY")

#print(logan.storyline)
#logan.show_trailer()
logan = media.Movie("Logan",
                    "A weary Logan cares for an ailing Professor X, somewhere on the Mexican border",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=RH3OxVFvTeg")

#print(school_of_rock.storyline)
#school_of_rock.show_trailer()
school_of_rock = media.Movie("School of Rock",
                             "No Vacancy,a rock band, performs at a nightclub three weeks before auditioning",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
#print(wedding_party.storyline)
#wedding_party.show_trailer()
wedding_party = media.Movie("Wedding party",
                            "The Wedding party follows the shenanigans that go on during the planning of a wedding in Nigeria",
                            "https://upload.wikimedia.org/wikipedia/en/0/0d/Weddingparty.jpg",
                            "https://www.youtube.com/watch?v=zbnXd-zCD6I")
#print(desperado.storyline)
#desperado.show_trailer()
desperado = media.Movie("Desperado",
                        "An American man tells the story of how he witnessed a massacre in another bar committed",
                        "https://upload.wikimedia.org/wikipedia/en/a/a6/Desperado1.jpg",
                        "https://www.youtube.com/watch?v=xZdZv3kT9xk")

movies = [A_trip_to_jamaica, half_of_a_yellow_sun, sin_city, troy, logan, school_of_rock, wedding_party, desperado]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
