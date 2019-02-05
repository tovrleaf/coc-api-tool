import abc


class AbstractMapper(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def map_dict_to_model(self, data, model=None):
        """Map data to model
        """
        pass
