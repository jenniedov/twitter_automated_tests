

class TwitterUsers():
    """Map person's name to twitter username"""
    _map = {
        "Kate Falanga": "Squidish_QA",
        "Laurie Marmon": "lalybi",
        "Andreea Popescu": "andreea_popescu"
    }

    @classmethod
    def get_username_by_name(cls, name):
        return cls._map[name]




