from soccerpy.requester import Requester
from soccerpy.modules.search_module import SearchModule


class BaseModule:
    def __init__(self):
        self.r = Requester()
        self.finder = SearchModule()
