from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import random
import os
import pygame

pygame.mixer.init()

# Set up columns and number ranges
COLUMNS = {
    'B': range(1, 16),
    'I': range(16, 31),
    'N': range(31, 46),
    'G': range(46, 61),
    'O': range(61, 76)
}

def play_sound(column, number):
    file_path = f"sounds/{column.lower()}{number}.mp3"
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

class BingoApp(App):
    def build(self):
        self.drawn_numbers = []  # To track the numbers drawn
        self.game_active = False  # To check if the game is running
        self.current_call = None  # Store the current called number

        layout = BoxLayout(orientation='vertical')

        # Labels for the Bingo header (B, I, N, G, O)
        header_layout = GridLayout(cols=5, size_hint_y=0.1)
        for col in COLUMNS.keys():
            header_layout.add_widget(Label(text=col, font_size=24))

        layout.add_widget(header_layout)

        # Grid to display the numbers under each column (vertical layout)
        self.bingo_grid = GridLayout(cols=5, size_hint=(1, 0.7))
        self.number_labels = {}

        # Display all numbers 1-75 under their respective columns (vertically)
        for i in range(15):
            for col, numbers in COLUMNS.items():
                number = numbers[i]  # Get the number for this row under the column
                label = Label(text=str(number), font_size=18)
                self.bingo_grid.add_widget(label)
                self.number_labels[(col, number)] = label  # Store labels for updating later

        layout.add_widget(self.bingo_grid)

        # Buttons to control the game
        control_layout = BoxLayout(size_hint_y=0.2)
        start_button = Button(text="Start Game", on_press=self.start_game)
        stop_button = Button(text="Stop Game", on_press=self.stop_game)
        continue_button = Button(text="Continue", on_press=self.continue_game)
        restart_button = Button(text="Restart Game", on_press=self.restart_game)
        control_layout.add_widget(start_button)
        control_layout.add_widget(stop_button)
        control_layout.add_widget(continue_button)
        control_layout.add_widget(restart_button)

        layout.add_widget(control_layout)

        return layout

    def start_game(self, instance):
        self.drawn_numbers = []  # Reset drawn numbers
        self.game_active = True
        self.call_next_number()

    def stop_game(self, instance):
        self.game_active = False
        if hasattr(self, 'event'):
            self.event.cancel()

    def continue_game(self, instance):
        if self.game_active:
            self.call_next_number()

    def restart_game(self, instance):
        self.stop_game(instance)
        self.reset_board()
        self.start_game(instance)

    def call_next_number(self):
        # Draw a new random number from available pool
        if self.game_active and len(self.drawn_numbers) < 75:
            while True:
                column = random.choice(list(COLUMNS.keys()))
                number = random.choice(COLUMNS[column])
                if (column, number) not in self.drawn_numbers:
                    self.drawn_numbers.append((column, number))
                    break

            # Update the UI: mark the number as called
            self.mark_number_as_called(column, number)
            # Play sound for the number called
            play_sound(column, number)

            # Schedule the next number after a delay
            self.event = Clock.schedule_once(lambda dt: self.call_next_number(), 2)

    def mark_number_as_called(self, column, number):
        # Get the label for the specific number and change its appearance
        label = self.number_labels.get((column, number))
        if label:
            label.color = (1, 0, 0, 1)  # Mark the called number in red

    def reset_board(self):
        # Reset the board to its initial state (all numbers unmarked)
        for label in self.number_labels.values():
            label.color = (1, 1, 1, 1)  # Reset color to white for all numbers

if __name__ == "__main__":
    BingoApp().run()