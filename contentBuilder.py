from abc import abstractmethod
from Content import Content

class IbuildWith:
    @abstractmethod
    def buildFrame(self, frame):
        pass

    @abstractmethod
    def buildContent(self, _content):
        pass

class buildWithAsterisk(IbuildWith):
    def __init__(self):
        """
        init of Content object
        """
        self.content = Content()

    def buildFrame(self, frame="*"):
        """
        :param frame: default as '*'
        """
        self.content.setFrame(frame * 120) # setting self.frame in Content object

    def buildContent(self, _content: str):
        # setting self.content in Content object
        self.content.setContent(self.content.getFrame() + "\n" + _content + "\n" + self.content.getFrame())


class buildWithHashMark(IbuildWith):
    def __init__(self):
        """
        init of Content object
        """
        self.content = Content()

    def buildFrame(self, frame="#"):
        """
        :param frame: default as '#'
        """
        self.content.setFrame(frame * 120)  # setting self.frame in Content object

    def buildContent(self, _content: str):
        # setting self.content in Content object
        self.content.setContent(self.content.getFrame() + "\n" + _content + "\n" + self.content.getFrame())


class buildWithAnyChar(IbuildWith):
    def __init__(self):
        """
        init of Content object
        """
        self.content = Content()

    def buildFrame(self, frame):
        """
        :param frame: a single char
        """
        self.content.setFrame(frame * 120)  # setting self.frame in Content object

    def buildContent(self, _content: str):
        # setting self.content in Content object
        self.content.setContent(self.content.getFrame() + "\n" + _content + "\n" + self.content.getFrame())
