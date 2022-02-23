import arcade
import arcade.gui
import json

CHARACTER_SCALING = 1
TILE_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1



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

    def on_click_child(self):
        game_window = MyGame()
        self.window.show_view(game_window)

    def on_draw(self):
        self.clear()
        self.manager.draw()


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(1280, 720, 'Train Game', resizable=True)

        self.scene = None

        self.player_sprite = None

        self.physics_engine = None

        self.camera = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):

        self.camera = arcade.Camera(self.width, self.height)

        self.scene = arcade.Scene()

        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        image_source = "1_vagoni.jpg"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 96
        self.scene.add_sprite("Player", self.player_sprite)

        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Walls"]
        )

    def on_draw(self):

        self.clear()

        self.camera.use()

        self.scene.draw()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )

        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):

        self.physics_engine.update()

        self.center_camera_to_player()


def main():

    window = arcade.Window()
    start_view = GameView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()