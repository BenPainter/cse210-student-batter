import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0]
        bricks = cast["brick"]
        paddle_position = paddle.get_position()
        ball_position = ball.get_position()

        for brick in bricks:
            if ball_position.equals(brick.get_position()):
                ball.set_velocity(ball.get_velocity().reverse_y())
                bricks.remove(brick)
        cast["brick"] = bricks

        if ball_position.get_y() == 1:
            ball.set_velocity(ball.get_velocity().reverse_y())

        if ball_position.get_x() <= 4:
            ball.set_velocity(ball.get_velocity().reverse_x())

        if ball_position.get_x() >= 76:
            ball.set_velocity(ball.get_velocity().reverse_x())

        if paddle_position.get_y() - 1 == ball_position.get_y():
            min_x = paddle_position.get_x()
            max_x = min_x + len(paddle.get_text())
            if ball_position.get_x() >= min_x and ball_position.get_x() <= max_x:
                ball.set_velocity(ball.get_velocity().reverse_y_paddle())
        
        return cast
        