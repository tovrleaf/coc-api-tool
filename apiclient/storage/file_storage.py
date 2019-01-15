import os
import re
from apiclient.exceptions import StorageException
from abstract_storage import AbstractStorage


class FileStorage(AbstractStorage):

    def __init__(self, directory):
        """Constructor for FileStorage class.

        :raises: apiclient.exception If directory contains non
            alphanumeric chars.
        """
        # \w is equivalent to [A-Za-z0-9_]
        if re.match("^[\\w\\/-]+$", directory) is None:
            raise StorageException(
                '%s can only contain alphanumeric characters' % directory)

        if os.path.isdir(directory) is not True:
            raise StorageException('%s is not a valid directory' % directory)
        self.directory = directory

    def save_clan(self, tag, data):
        """Save clan information to a file
        """
        self.__save_to_file('clan', tag, data)

    def read_clan(self, tag):
        return self.__read_from_file('clan', tag)

    def read_player(self, tag):
        return self.__read_from_file('player', tag)

    def save_player(self, tag, data):
        """Save player information to a file
        """
        self.__save_to_file('player', tag, data)

    def __save_to_file(self, token, tag, data):
        f = open('%s/%s-%s.json' % (self.directory, token, tag), 'w+')
        f.write(data)
        f.close()

    def __read_from_file(self, token, tag):
        try:
            f = open('%s/%s-%s.json' % (self.directory, token, tag), 'r')
        except IOError:
            raise StorageException(
                'Unable to read data for a %s with tag %s' % (token, tag))
        if f.mode != 'r':
            return None
        return f.read()
