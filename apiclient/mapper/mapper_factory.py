from clan_mapper import ClanMapper
from member_mapper import MemberMapper


class MapperFactory(object):

    def factory(type):
        """Creates an instance of AbstractMapper class

        :raises: RuntimeError
        """
        if type == 'clan':
            return ClanMapper()
        if type == 'member':
            return MemberMapper()

        raise RuntimeError('Unable to instantiate mapper with type %s' % type)
    factory = staticmethod(factory)
