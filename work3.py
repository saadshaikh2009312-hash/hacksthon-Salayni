class SecureDiary:
    def __init__(self):
        self.logged_in = False

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        file = open("login.txt", "r")
        data = file.read().split()
        file.close()

        if username == data[0] and password == data[1]:
            self.logged_in = True
            print("Login Successful")
        else:
            print("Login Failed")

    def scramble(self, text):
        result = ""
        for ch in text:
            result += chr(ord(ch) + 1)
        return result

    def unscramble(self, text):
        result = ""
        for ch in text:
            result += chr(ord(ch) - 1)
        return result

    def write_diary(self):
        entry = input("Write diary entry: ")
        encrypted = self.scramble(entry)

        file = open("diary.txt", "a")
        file.write(encrypted + "\n")
        file.close()

        print("Diary Saved")

    def read_diary(self):
        file = open("diary.txt", "r")
        for line in file:
            print(self.unscramble(line.strip()))
        file.close()


diary = SecureDiary()
diary.login()

if diary.logged_in:
    diary.write_diary()
    diary.read_diary()