import os


class fileManipulator:
    def __init__(self):
        pass

    @staticmethod
    def isFilePathExist(filePath:str):
        """
        :param filePath: file's path to check
        :return: boolean if the given file path exist
        """
        return os.path.exists(filePath)

    @staticmethod
    def createEmptyFile(filePath: str):
        """
        :param filePath: a string
        :return: creates an empty file with the given file's path
        """
        open(filePath, 'a').close()

    @staticmethod
    def writeContentToFile(content: str, filePath: str):
        """
        :param content: a string that will be inserted to file
        :param filePath: a string of file's path
        :return: content is inserted to file with the given file's path (all content before is overridden)
        """
        with open(filePath, "w") as file:
            file.write(content)

    @staticmethod
    def appendContentToFile(content: str, filePath: str):
        """
        :param content: a string that will be appended to file
        :param filePath: a file's path string
        :return: content appended to file
        """
        with open(filePath, "a") as file:
            if os.stat(filePath).st_size == 0:  # append to an empty file
                file.write(content)
            else:
                file.write("\n" + content)

    @staticmethod
    def insertContentToFile(content: str, filePath: str, fileOption: str):
        """
        :param content: a string of content
        :param filePath: file's path to whom content will be appended/written
        :param fileOption: write/append
        """
        if (str(fileOption)).lower() == 'append':
            fileManipulator.appendContentToFile(content, filePath)
        else:
            fileManipulator.writeContentToFile(content, filePath)

    @staticmethod
    def showContentFromFile(filePath: str):
        """
        :param filePath: a string of file's path to be shown
        :return: prints the content of a file with the given file's path
        """
        with open(filePath, "r") as file:
            contentInFile = file.read()
        print(contentInFile)

    @staticmethod
    def deleteContentFromFile(filePath: str):
        """
        :param filePath: a string of file's path
        :return: deletes the file with the given file's path, if the the file path exist
        """
        if fileManipulator.isFilePathExist(filePath):
            os.remove(filePath)
