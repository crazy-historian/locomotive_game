import arcade
import arcade.gui
import json


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.TOPAZ)

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Играть", width=300)
        self.v_box.add(start_button.with_space_around(bottom=30))

        settings_button = arcade.gui.UIFlatButton(text="Выбрать задание", width=300)
        self.v_box.add(settings_button.with_space_around(bottom=30))

        help_buttons = arcade.gui.UIFlatButton(text="Помощь", width=300)
        self.v_box.add(help_buttons.with_space_around(bottom=30))

        quit_button = QuitButton(text="Выйти из игры", width=300)
        self.v_box.add(quit_button)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )


    def on_draw(self):
        self.clear()
        self.manager.draw()

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class TrainGame(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, 'Train Game', resizable=True)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.TOPAZ)


    def on_update(self, delta_time):
        pass


def main():
    window = arcade.Window()
    start_view = GameView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()