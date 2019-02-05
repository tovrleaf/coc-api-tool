from abstract_mapper import AbstractMapper
from apiclient.model.member_model import MemberModel


class MemberMapper(AbstractMapper):

    def map_dict_to_model(self, data, model=None):

        if model is None:
            model = MemberModel()

        model.tag = data['tag']
        model.name = data['name']
        model.exp_level = data['expLevel']
        model.trophies = data['trophies']
        model.versus_trophies = data['versusTrophies']
        model.clan_rank = data['clanRank']
        model.previous_rank = data['previousClanRank']
        model.donations = data['donations']
        model.donations_received = data['donationsReceived']

        return model
