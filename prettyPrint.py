from menu import menu
from contentBuilder import buildWithAsterisk, buildWithHashMark, buildWithAnyChar
from fileManipulator import fileManipulator


class prettyPrint:
    __instance = None

    @staticmethod
    def getInstance():
        if prettyPrint.__instance == None:
            prettyPrint()
        return prettyPrint.__instance

    def __init__(self):
        if prettyPrint.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            prettyPrint.__instance = self

    def workOption1(self, content: str, filePath: str, fileOption: str):
        """
        :param content: user's content that will be inserted to file
        :param filePath: the file path of file that the content will be inserted to file
        :param fileOption: append/write
        :return: copy of Content obj that was created
        """
        contentObj = buildWithAsterisk()
        contentObj.buildFrame()
        contentObj.buildContent(content)
        fileManipulator.insertContentToFile(contentObj.content.getContent(), filePath, fileOption)
        copyObj = contentObj.content.getCopy(contentObj.content)
        return copyObj

    def workOption2(self, content: str, filePath: str, fileOption: str):
        """
        :param content: user's content that will be inserted to file
        :param filePath: the file path of file that the content will be inserted to
        :param fileOption: append/write
        :return: copy of Content obj that  was created
        """
        contentObj = buildWithHashMark()
        contentObj.buildFrame()
        contentObj.buildContent(content)
        fileManipulator.insertContentToFile(contentObj.content.getContent(), filePath, fileOption)
        copyObj = contentObj.content.getCopy(contentObj.content)
        return copyObj

    def workOption3(self, content: str, filePath: str, fileOption: str):
        """
        :param content: user's content that will be inserted to file
        :param filePath: the file path of file that the content will be inserted to
        :param fileOption: append/write
        :return: copy of Content obj that was created
        """
        contentObj = buildWithAnyChar()
        frame = input("Please enter a char:\n")  # user's choice of a char as frame
        contentObj.buildFrame((str(frame))[0])  # if the user input more than one char
        contentObj.buildContent(content)
        fileManipulator.insertContentToFile(contentObj.content.getContent(), filePath, fileOption)
        copyObj = contentObj.content.getCopy(contentObj.content)
        return copyObj

    def workOption4(self, content: str, frame: str, filePath: str, fileOption: str):
        """
        :param content: user's content that will be inserted to file
        :param frame: last used frame (last choice)
        :param filePath: the file path of file that the content will be inserted to
        :param fileOption: write/append
        """
        contentObj = buildWithAnyChar()
        contentObj.buildFrame(frame)
        contentObj.buildContent(content)
        fileManipulator.insertContentToFile(contentObj.content.getContent(), filePath, fileOption)

    def workOption5(self, filePath: str):
        """
        :param filePath: file's path to to a file that the user want to see its content
        """
        fileManipulator.showContentFromFile(filePath)

    def workBuilder(self, userOption: str, content: str, filePath: str, fileOption: str):
        """
        function dealing with user's choices between 1 to 3 (included)
        :param userOption: user's choice between 1 to 3 (included)
        :param content: user's content that will be inserted to file
        :param filePath: the file path of file that the content will be inserted to
        :param fileOption: append/write
        :return: copy of Content obj that was created
        """
        copyObj = None
        if int(userOption) == 1:
            copyObj = self.workOption1(content, filePath, fileOption)
        elif int(userOption) == 2:
            copyObj = self.workOption2(content, filePath, fileOption)
        else: # int(userOption) == 3:
            copyObj = self.workOption3(content, filePath, fileOption)

        return copyObj

    def runFacade(self):
        """
        The main method of the program, defined in the documentation
        """
        userOption = 0
        copyObj = None
        filePath, fileOption = menu.firstMenu()
        while userOption != '7':
            userOption = menu.secondMenu()
            if int(userOption) in list(range(1,4)):
                content = menu.thirdMenu()
                copyObj = self.workBuilder(userOption, content, filePath, fileOption)
            if userOption == '5':
                self.workOption5(filePath)
            if userOption == '6':
                # when file deleted, the 'last choice' initiated to None, and the first menu shown to user
                copyObj = None
                fileManipulator.deleteContentFromFile(filePath)
                filePath, fileOption = menu.firstMenu()
            if copyObj != None and userOption == '4':
                content = menu.thirdMenu()
                self.workOption4(content, copyObj.getFrame()[0], filePath, fileOption)
            if copyObj == None and userOption == '4':
                print("There is no last choice available yet")

    def run(self):
        self.runFacade()
