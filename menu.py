from fileManipulator import fileManipulator


class menu:
    def __init__(self):
        pass

    @staticmethod
    def firstMenu():
        """
        :return: a tuple consisting of inserted by user file path and fileOption (write/append)
        """
        print("Welcome to Pretty Print !!")
        filePath = input("Please enter a file path:\n"
                         "File path: ")
        print("\n")
        if fileManipulator.isFilePathExist(filePath) == False: # if filePath does not exist, empty file created
            fileManipulator.createEmptyFile(filePath)

        fileOption = input("Please enter 'write' or 'append'\n"
                               "write/append: ")
        print("\n")
        while fileOption not in ["append", "write"]: # if user inserted invalid fileOption
            fileOption = input("Please enter 'write' or 'append'\n"
                               "write/append: ")


        return (filePath, fileOption)

    @staticmethod
    def secondMenu():
        """
        :return: inserted userOption by the user
        """
        print("\nWhat would you like to do?")
        print("Please choose one of those options:")

        userOption = input("1. Write with * as frame\n"
                          "2. Write with # as frame\n"
                          "3. Choose your own character as frame\n"
                          "4. Like the last frame's choise\n"
                          "5. Show content of file\n"
                          "6. Delete content of file\n"
                          "7. Exit\n"
                          "Your choise: \n")
        try:
            # if user inserted invalid int choice (valid choice is between 1-7)
            while int(userOption) not in list(range(1,8)):
                print("Please choose a natural number between 1 to 7:")
                userOption = menu.secondMenu()
        except Exception as e:
            # if the user value is not an int
            print("Please choose a natural number between 1 to 7:")
            userOption = menu.secondMenu()
        return userOption

    @staticmethod
    def thirdMenu():
        """
        :return: inserted content by the user
        """
        content = input("Please enter a content:\n")
        return content
