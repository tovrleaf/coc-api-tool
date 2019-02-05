import abc


class AbstractStorage(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, directory):
        pass

    @abc.abstractmethod
    def save_clan(self, tag, data):
        """Save clan information
        """
        pass

    @abc.abstractmethod
    def read_clan(self, tag):
        """Read clan information
        """
        pass

    def refresh_clan(self, tag):
        """Refresh player data
        """
        data = self.read_clan(tag)
        self.save_clan(tag, data)

    @abc.abstractmethod
    def read_player(self, tag):
        """Read player information
        """
        pass

    @abc.abstractmethod
    def save_player(self, tag, data):
        """Save player information
        """
        pass

    def refresh_player(self, tag):
        """Refresh player data
        """
        data = self.read_player(tag)
        self.save_player(tag, data)
