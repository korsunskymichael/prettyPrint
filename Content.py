from abc import ABC, abstractmethod
import copy

class IContent:
    @abstractmethod
    def setFrame(self):
        pass

    @abstractmethod
    def setContent(self):
        pass


class Content(IContent):
    def __init__(self):
        self.frame = ""
        self.content = ""

    def setFrame(self, frame: str):
        self.frame = frame

    def setContent(self, content: str):
        self.content = content

    def getFrame(self):
        return self.frame

    def getContent(self):
        return self.content

    def getCopy(self, obj):
        """
        :param obj: a Content object
        :return: a deep copy of the inserted Content object
        """
        return copy.deepcopy(obj)