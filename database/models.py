from typing import List, Dict
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)

    story = Column(Integer, ForeignKey("stories.id"))

    def to_json(self) -> Dict:
        data = {
            "id": self.id,
            "name": self.name,
            "desc": self.desc
        }

        return data

    @staticmethod
    def from_json(data: Dict) -> 'Item':
        item = Item()

        item.id = data["id"]
        item.name = data["name"]
        item.desc = data["desc"]

        return item

# TODO Decide of the fields in Room


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    north = Column(Integer)
    south = Column(Integer)
    east = Column(Integer)
    west = Column(Integer)
    title = Column(String)
    content = Column(String)

    story = Column(Integer, ForeignKey("stories.id"))

    def to_json(self) -> Dict:
        data = {
            "id": self.id,
            "north": self.north,
            "south": self.south,
            "east": self.east,
            "west": self.west,
            "title": self.title,
            "content": self.content
        }

        return data

    @staticmethod
    def from_json(data: Dict) -> 'Room':
        room = Room()

        room.id = data["id"]
        room.north = data["north"]
        room.south = data["south"]
        room.east = data["east"]
        room.west = data["west"]
        room.title = data["title"]
        room.content = data["content"]

        return room


class BaseCharacterInfo(Base):
    __tablename__ = "base_character_infos"

    id = Column(Integer, primary_key=True)
    res_name = Column(String)
    max_hp = Column(Integer)
    max_res = Column(Integer)

    story = Column(Integer, ForeignKey("stories.id"))

    def to_json(self) -> Dict:
        data = {
            "name": self.name,
            "res_name": self.res_name,
            "max_hp": self.max_hp,
            "max_res": self.max_res
        }

        return data

    @staticmethod
    def from_json(data: Dict) -> 'BaseCharacterInfo':
        return BaseCharacterInfo(**data)

# TODO Decide of the fields in State


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    curr_hp = Column(Integer)
    curr_res = Column(Integer)
    curr_room = Column(Integer)

    story = Column(Integer, ForeignKey("stories.id"))

# TODO Finish the to_json, from_json, to_db and from_db methods


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)

    items = relationship("Item")
    rooms = relationship("Room")
    base_character_info = relationship("BaseCharacterInfo")
    state = relationship("State")

    def create_state(self):
        new_state = State()

        new_state.curr_hp = self.base_character_info.max_hp
        new_state.curr_res = self.base_character_info.max_res

        self.state = new_state

    def save_state(self, connection):
        pass

    def to_json(self) -> Dict:
        data = {
            "id": self.id,
            "items": [x for x in (item.to_json() for item in self.items)],
            "rooms": [x for x in (room.to_json() for room in self.rooms)],
            "base_character_info": self.base_character_info.to_json()
        }

        return data

    def to_db(self):
        pass

    @staticmethod
    def from_db(connection) -> 'Story':
        pass

    @staticmethod
    def from_json(data: Dict) -> 'Story':
        story = Story()

        story.id = data["id"]
        story.items = list(map(Item.from_json, data["items"]))
        story.rooms = list(map(Room.from_json, data["rooms"]))
        story.base_character_info = BaseCharacterInfo.from_json(data["base_character_info"])

        return story
