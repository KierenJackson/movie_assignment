"""
Name: Kieren Jackson
Date started: 25/08/19
GitHub URL:
"""


MOVIES_FILE = "movies.csv"


def main():

    movies = movie_sorter()

    print("Movies To Watch 1.0 - by Kieren Jackson")
    print_menu()
    menu_answer = menu_input()
    menu_selection(menu_answer, movies)


def movie_sorter():
    movies = []
    movie_file = open(MOVIES_FILE, "r")
    unsorted_movies = movie_file.readlines()
    movie_file.close()

    for movie in range(len(unsorted_movies)):
        movies.append(unsorted_movies[movie].rstrip())

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


def int_checker():
    while True:
        try:
            num = int(input(">>>"))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            return num


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
        print("Enter the number of a movie to mark as watched")
        movie_number = int_checker()
        while movie_number < 0 or movie_number >= len(movies):
            if movie_number < 0:
                print("Number must be >= 0")
                movie_number = int_checker()
            else:
                print("Invalid movie number")
                movie_number = int_checker()

        watch_movie(movie_number, movies)

        print_menu()
        menu_answer = menu_input()
        menu_selection(menu_answer, movies)
    elif answer == "Q":
        print("{} movies saved to movies.csv".format(len(movies)))
        print("Have a nice day :)")
        quit


def watch_movie(movie_number, movies):
    marked_status = movies[movie_number][3]
    if marked_status == "w":
        print("You have already watched {}".format(movies[movie_number][0]))
    else:
        movies[movie_number][3] = "w"
        print("{} from {} watched".format(movies[movie_number][0], movies[movie_number][1]))


def movie_list(movies):
    number = 1

    for movie in movies:
        if movie[3] == "u":
            watched_status = "*"
        else:
            watched_status = ""
        print("{}. {:1} {:35} - {:>5} ({})".format(number,watched_status, movie[0], movie[1], movie[2]))
        number += 1


if __name__ == '__main__':
    main()

