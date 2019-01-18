from common.Constant import public_playlist_code, private_playlist_code


class SongSheet:
    def __init__(self, id, name, privacy):
        self._id = id
        self._name = name
        self._privacy = privacy

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

    @property
    def privacy(self):
        return self._privacy

    @privacy.setter
    def privacy(self, value):
        self._privacy = value

    def __str__(self):
        return "[id=" + str(self._id) + \
               ", name=" + self._name + \
               "，privacy=" + ('公有歌单' if self._privacy == public_playlist_code else (
            '私有歌单' if self._privacy == private_playlist_code else '未知')) + "]"

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, SongSheet):
            return self._id == other._id and self._name == other._name
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._id) + hash(self._name)
