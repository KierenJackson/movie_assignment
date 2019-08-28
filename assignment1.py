"""
Name: Kieren Jackson
Date started: 25/08/19
GitHub URL: https://github.com/KierenJackson/movie_assignment
"""

from operator import itemgetter

MOVIES_FILE = "movies.csv"
WATCHED = "*"
UNWATCHED = ""


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
    print("{} movies loaded".format(len(movies)))
    print_menu()
    menu_answer = menu_input()
    menu_selection(menu_answer, movies)


def list_comma_splitter(movies):
    """Take movie list and split strings by commas and return it"""
    for n in range(len(movies)):
        movies[n] = movies[n].split(",")

    return movies


def print_menu():
    """Print the selection menu"""
    print("Menu: \nL - List movies \nA - Add new movie \nW - Watch a movie \nQ - Quit")


def menu_input():
    """Take users menu input then error check it and return it"""
    answer = input(">>> ").upper()
    while answer not in "LAWQ":
        print("Invalid menu choice")
        print_menu()
        answer = input(">>> ").upper()
    return answer


def int_checker(text):
    """Take in text to print in integer input then error check input and return it"""
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            return num


def year_sorter(movies):
    """Take in movie list and sort the list by year then name and return it"""
    for movie in movies:
        movie[1] = int(movie[1])

    movies.sort(key=itemgetter(1, 0))

    return movies


def int_converter(movies):
    """Take movie list and convert years from integers to strings and return it"""
    for movie in movies:
        movie[1] = str(movie[1])
    return movies


def menu_selection(answer, movies):
    """Take in user menu input and select the corresponding selection"""
    if answer == "L":
        movie_list(movies)
        print_menu()
        menu_answer = menu_input()
        menu_selection(menu_answer, movies)
    elif answer == "A":
        add_movie(movies)
        movies = year_sorter(movies)
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
        write_movie_file(movies)
        print("{} movies saved to movies.csv".format(len(movies)))
        print("Have a nice day :)")
        quit
    elif answer == "":
        print("Invalid menu choice")
        print_menu()
        menu_answer = menu_input()
        menu_selection(menu_answer, movies)


def write_movie_file(movies):
    """Take in movie list and write it to movies file"""
    amount_of_movies = 0
    movies = int_converter(movies)
    movie_file_write = open(MOVIES_FILE, "w")
    for movie in movies:
        for data in range(len(movie)):
            movie_file_write.write(movies[amount_of_movies][data])
            if data != 3:
                movie_file_write.write(",")
        movie_file_write.write("\n")
        amount_of_movies += 1
    movie_file_write.close()


def watched_movie_checker(movies):
    """Take in movie list to check if all movies are watched and return false"""
    for movie in movies:
        if movie[3] == "u":
            return True

    return False


def add_movie(movies):
    """Take in movie list and ask user for inputs about a movie then append it to movie list"""
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
    """Take in user movie selection and change movie from unwatched to watched in movie list"""
    marked_status = movies[movie_number][3]
    if marked_status == "w":
        print("You have already watched {}".format(movies[movie_number][0]))
    else:
        movies[movie_number][3] = "w"
        print("{} from {} watched".format(movies[movie_number][0], movies[movie_number][1]))


def movie_list(movies):
    """Take in movie list and print out a formatted list of all movies."""
    list_number = 0
    movies_watched = 0
    movies_unwatched = 0

    for movie in movies:
        if movie[3] == "u":
            movies_unwatched += 1
            print("{}. {:1} {:35} - {:>5} ({})".format(list_number, WATCHED, movie[0], movie[1], movie[2]))
        else:
            movies_watched += 1
            print("{}. {:1} {:35} - {:>5} ({})".format(list_number, UNWATCHED, movie[0], movie[1], movie[2]))
        list_number += 1
    print("{} movies watched, {} movies still to watch".format(movies_watched, movies_unwatched))


if __name__ == '__main__':
    main()

