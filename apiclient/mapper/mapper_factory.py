from clan_mapper import ClanMapper
from player_mapper import PlayerMapper


class MapperFactory(object):

    def factory(type):
        """Creates an instance of AbstractMapper class

        :raises: RuntimeError
        """
        if type == 'clan':
            return ClanMapper()
        if type == 'player':
            return PlayerMapper()

        raise RuntimeError('Unable to instantiate mapper with type %s' % type)
    factory = staticmethod(factory)
