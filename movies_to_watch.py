"""
Name: Kieren Jackson
Date started: 25/08/19
GitHub URL:
"""


MOVIES_FILE = "movies.csv"


def main():


    print("Movies To Watch 1.0 - by Kieren Jackson")
    print_menu()
    menu_answer = menu_selection()


def print_menu():
    print("Menu: \nL - List movies \nA - Add new movie \nW - Watch a movie \nQ - Quit")


def menu_selection():
    answer = input(">>> ").upper()
    while answer not in "LAWQ":
        print("Invalid menu choice")
        print_menu()
        answer = input(">>> ").upper()
    return answer


def movie_list():
    number = 1
    movie_file = open(MOVIES_FILE, "r")
    movies = movie_file.readlines()
    movie_file.close()

    for n in range(len(movies)):
        movies[n] = movies[n].split(",")

    for movie in movies:
        print("{}. {:35} - {:>5} ({})".format(number, movie[0], movie[1], movie[2]))
        number += 1

6
if __name__ == '__main__':
    main()

