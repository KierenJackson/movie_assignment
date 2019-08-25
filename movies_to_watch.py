"""
Name: Kieren Jackson
Date started: 25/08/19
GitHub URL:
"""


def main():
    print("Movies To Watch 1.0 - by Kieren Jackson")
    print_menu()
    selection = menu_selection()


def print_menu():
    print("Menu: \nL - List movies \nA - Add new movie \nW - Watch a movie \nQ - Quit")


def menu_selection():
    answer = input(">>> ").upper()
    while answer not in "LAWQ":
        print("Invalid menu choice")
        print_menu()
        answer = input(">>> ").upper()
    return answer


if __name__ == '__main__':
    main()

