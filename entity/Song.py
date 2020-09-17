class Song:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return "[id=" + str(self._id) + \
               ", name=" + self._name + "]"

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, Song):
            return self._id == other._id and self._name == other._name
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._id) + hash(self._name)