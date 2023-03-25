from Controllers import UserController as Ctrls
from Controllers import Controller


def main():

    # first of all launch authentification
    while True:
        res = Controller.launchAuth()
        if res is False:
            Controller.launchAuth()
        else:
            break

    # then start the loop with the right user

    # TODO: specify the type of Controller according to the user status
    while True:
        val = input()
        Ctrls.UserController().displayMessage(val)


if __name__ == "__main__":
    main()
