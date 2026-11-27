from package.controllers.system import System


def workspace():

    system = System()
    system.start()


if __name__ == "__main__":

    workspace()
