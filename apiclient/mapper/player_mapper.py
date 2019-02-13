from abstract_mapper import AbstractMapper
from apiclient.model.player_model import PlayerModel


class PlayerMapper(AbstractMapper):

    def map_dict_to_model(self, data, model=None):

        if model is None:
            model = PlayerModel()

        model.tag = data['tag']
        model.name = data['name']
        model.exp_level = data['expLevel']
        model.trophies = data['trophies']
        model.versus_trophies = data['versusTrophies']
        model.donations = data['donations']
        model.donations_received = data['donationsReceived']

        return model
