from file_storage import FileStorage


class StorageFactory(object):

    def factory(type, conf):
        """Creates an instance of AbstractStorage class

        :raises: RuntimeError
        """
        if type == 'file':
            return FileStorage(conf)
        raise RuntimeError('Unable to instantiate storage with type %s' % type)
    factory = staticmethod(factory)
