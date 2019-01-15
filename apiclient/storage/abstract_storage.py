import abc


class AbstractStorage(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, directory):
        pass

    @abc.abstractmethod
    def save_clan(self, tag, data):
        pass

    @abc.abstractmethod
    def read_clan(self, tag):
        pass

    @abc.abstractmethod
    def read_player(self, tag):
        pass

    @abc.abstractmethod
    def save_player(self, tag, data):
        pass
