"""
Name: Kieren Jackson
Date started: 25/08/19
GitHub URL:
"""

from operator import itemgetter

MOVIES_FILE = "movies.csv"


def main():
    movies = []
    movie_file = open(MOVIES_FILE, "r")
    unsorted_movies = movie_file.readlines()
    movie_file.close()

    for movie in range(len(unsorted_movies)):
        movies.append(unsorted_movies[movie].rstrip())

    movies = list_comma_splitter(movies)
    movies = year_sorter(movies)

    print("Movies To Watch 1.0 - by Kieren Jackson")
    print_menu()
    menu_answer = menu_input()
    menu_selection(menu_answer, movies)


def list_comma_splitter(movies):
    for n in range(len(movies)):
        movies[n] = movies[n].split(",")

    return movies


def print_menu():
    print("Menu: \nL - List movies \nA - Add new movie \nW - Watch a movie \nQ - Quit")


def menu_input():
    answer = input(">>> ").upper()
    while answer not in "LAWQ":
        print("Invalid menu choice")
        print_menu()
        answer = input(">>> ").upper()
    return answer


def int_checker(text):
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            return num


def year_sorter(movies):
    for movie in movies:
        movie[1] = int(movie[1])

    movies.sort(key=itemgetter(1, 0))

    return movies


def menu_selection(answer, movies):
    if answer == "L":
        movie_list(movies)
        print_menu()
        menu_answer = menu_input()
        menu_selection(menu_answer, movies)
    elif answer == "A":
        pass
        print_menu()
        menu_answer = menu_input()
        menu_selection(menu_answer, movies)
    elif answer == "W":
        movie_unwatched = watched_movie_checker(movies)
        if movie_unwatched:
            print("Enter the number of a movie to mark as watched")
            int_movie_text = ">>>"
            movie_number = int_checker(int_movie_text)
            while movie_number < 0 or movie_number >= len(movies):
                if movie_number < 0:
                    print("Number must be >= 0")
                    movie_number = int_checker(int_movie_text)
                else:
                    print("Invalid movie number")
                    movie_number = int_checker(int_movie_text)

            watch_movie(movie_number, movies)
            print_menu()
            menu_answer = menu_input()
            menu_selection(menu_answer, movies)
        else:
            print("No more movies to watch!")
            print_menu()
            menu_answer = menu_input()
            menu_selection(menu_answer, movies)
    elif answer == "Q":
        print("{} movies saved to movies.csv".format(len(movies)))
        print("Have a nice day :)")
        quit


def watched_movie_checker(movies):
    for movie in movies:
        if movie[3] == "u":
            return True

    return False


def add_movie(movies):
    list_append_number = len(movies)
    movies.append([])

    title = str(input("Title: "))
    movies[list_append_number].append(title)

    year_int_text = "Year: "
    year = int_checker(year_int_text)
    while year < 0:
        print("Number must be >= 0")
        year = int_checker(year_int_text)
    movies[list_append_number].append(year)

    category = str(input("Category: "))
    movies[list_append_number].append(category)

    movies[list_append_number].append("u")


def watch_movie(movie_number, movies):
    marked_status = movies[movie_number][3]
    if marked_status == "w":
        print("You have already watched {}".format(movies[movie_number][0]))
    else:
        movies[movie_number][3] = "w"
        print("{} from {} watched".format(movies[movie_number][0], movies[movie_number][1]))


def movie_list(movies):
    number = 0

    for movie in movies:
        if movie[3] == "u":
            watched_status = "*"
        else:
            watched_status = ""
        print("{}. {:1} {:35} - {:>5} ({})".format(number, watched_status, movie[0], movie[1], movie[2]))
        number += 1


if __name__ == '__main__':
    main()

