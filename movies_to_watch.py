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
    movie_file = open(MOVIES_FILE, "r")
    movies = movie_file.readlines()
    movie_file.close()

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


def menu_selection(answer, movies):
    if answer == "L":
        movie_list(movies)
        print_menu()
        menu_answer = menu_input()
        menu_selection(menu_answer, movies)
    elif answer == "A":
        pass
    elif answer == "W":
        pass
    elif answer == "Q":
        print("{} movies saved to movies.csv".format(len(movies)))
        print("Have a nice day :)")
        quit


def movie_list(movies):
    number = 1

    for movie in movies:
        print("{}. {:35} - {:>5} ({})".format(number, movie[0], movie[1], movie[2]))
        number += 1


if __name__ == '__main__':
    main()

