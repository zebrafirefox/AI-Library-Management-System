from domain.User import User

class Main:
    def __init__(self):
        print("LMS starting")

    def run(self):
        user = User("Fred", "fred@gmail.com", "Sydney")
        print(user)

if __name__ == "__main__":
    main = Main()
    main.run()
