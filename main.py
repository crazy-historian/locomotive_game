
import arcade
import arcade.gui

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class TrainGame(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, 'Train Game', resizable=True)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.TOPAZ)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Играть", width=300)
        self.v_box.add(start_button.with_space_around(bottom=30))

        settings_button = arcade.gui.UIFlatButton(text="Выбрать задание", width=300)
        self.v_box.add(settings_button.with_space_around(bottom=30))

        help_buttons = arcade.gui.UIFlatButton(text="Помощь", width=300)
        self.v_box.add(help_buttons.with_space_around(bottom=30))

        quit_button = QuitButton(text="Выйти из игры", width=300)
        self.v_box.add(quit_button)

        @settings_button.event("on_click")
        def on_click_settings(event):
            print("Settings:", event)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )


    def on_draw(self):
        self.clear()
        self.manager.draw()


    def on_update(self, delta_time):
        pass

window = TrainGame()
arcade.run()


