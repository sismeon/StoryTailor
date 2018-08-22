from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database.models import State, Room

from typing import List


class GameScreen(Screen):
    txt_input = ObjectProperty(None)
    txt_output = ObjectProperty(None)

    current_room: Room = None

    # I feel like this could be made cooler

    def remove_first_line(self):
        text: List[str] = self.txt_output.text.split("\n")
        text.pop(0)

        self.txt_output.text = "\n".join(text)

    def add_bottom_line(self, line: str):
        text: List[str] = self.txt_output.text.split("\n")
        text.append(line)

        self.txt_output.text = "\n".join(text)

    def add_newline(self):
        text: List[str] = self.txt_output.text.split("\n")
        text.append("")

        self.txt_output.text = "\n".join(text)

    def clear(self):
        self.txt_output.text = ""

    def new_room(self, room: Room):
        self.current_room = room
        self.print_room_content()

    def print_room_content(self):
        self.clear()
        self.txt_output = self.current_room.content

    def print_message(self, urgent: bool, message: str):
        if urgent:
            self.clear()
        else:
            self.print_room_content()

        self.add_newline()
        self.add_bottom_line(message)
        self.add_bottom_line("[Press any key to continue]")

    # display the character's stats

    def display_stats(self, state: State):
        pass
