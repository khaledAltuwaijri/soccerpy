from soccerpy.modules.Fundamentals.searchable import Searchable
from collections.abc import Sequence


class Players(Searchable, Sequence):
    def __len__(self):
        return len(self.players)

    def __getitem__(self, index):
        return self.players[index]

    def __init__(self, data):
        super(Players, self).__init__()
        self.data = data
        self.players = []
        self.process()

    def process(self):
        for player in self.data:
            self.players.append(Player(player))

    def explicit_search(self, players, query):
        status = self.finder.search_for_player_by_name(players, query=query)
        if status:
            return status
        return "Not Found"

    def search_by_name(self, query):
        dataset = self.players
        return self.explicit_search(dataset, query=query)


class Player:
    def __init__(self, player):
        self.name = player['name']
        self.position = player['position']
        self.jersey_number = player['jerseyNumber']
        self.dateOfBirth = player['dateOfBirth']
        self.nationality = player['nationality']
        self.contract_until = player['contractUntil']
        self.market_value = player['marketValue']
