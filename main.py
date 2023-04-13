from Controllers import Controller
from Controllers.AdminController import AdminController
from Controllers.UserController import UserController


def main():
    # first of all launch authentification
    userlogged = False
    while userlogged is False:
        userlogged = Controller.launchAuth()
        if Controller.failCounter > 2:
            exit("You failed too much")

    # then start the loop with the right user
    controller = None
    if userlogged.getRole().getName() == 'Admin':
        controller = AdminController(userlogged)
    elif userlogged.getRole().getName() == 'User':
        controller = UserController(userlogged)

    controller.run()


if __name__ == "__main__":
    main()
