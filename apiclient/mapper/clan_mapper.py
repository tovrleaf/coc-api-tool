from abstract_mapper import AbstractMapper
from apiclient.model.clan_model import ClanModel
from player_mapper import PlayerMapper


class ClanMapper(AbstractMapper):

    def map_dict_to_model(self, data, model=None, populate_members=False):

        if model is None:
            model = ClanModel()

        model.id = data['tag']
        model.name = data['name']
        model.country = data['location']['name']
        model.clan_level = data['clanLevel']
        model.clan_points = data['clanPoints']
        model.clan_versus_points = data['clanVersusPoints']
        model.required_trophies = data['requiredTrophies']
        model.war_win_streak = data['warWinStreak']
        model.war_wins = data['warWins']
        model.members = data['members']

        if populate_members is True:
            self.populate_model_with_members(model, data['memberList'])

        return model

    def populate_model_with_members(self, model, member_list):
        player_mapper = PlayerMapper()
        model.member_list = {}
        for member in member_list:
            player_model = player_mapper.map_dict_to_model(member)
            model.member_list[player_model.tag] = player_model
