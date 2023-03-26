from Controllers.UserController import UserController
from Controllers.AdminController import AdminController
from Controllers import Controller


def main():
    # first of all launch authentification
    userlogged = False
    while userlogged is False:
        userlogged = Controller.launchAuth()

    # then start the loop with the right user
    controller = None
    if userlogged.getRole().getName() == 'Admin':
        controller = AdminController(userlogged)
    elif userlogged.getRole().getName() == 'User':
        controller = UserController(userlogged)

    while True:
        controller.displayMessage()


if __name__ == "__main__":
    main()
