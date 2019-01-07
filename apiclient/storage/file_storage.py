import os
from apiclient.exceptions import StorageException


class FileStorage:

    def __init__(self, directory):

        if os.path.isdir(directory) != True:
            raise StorageException('%s is not a valid directory' % directory)
        self.directory = directory

    def save_clan(self, tag, data):
        f = open('%s/clan-%s.json' % (self.directory, tag), 'w+')
        f.write(data)
        f.close()

    def save_player(self, tag, data):
        f = open('%s/player-%s.json' % (self.directory, tag), 'w+')
        f.write(data)
        f.close()
