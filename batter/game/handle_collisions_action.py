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
        #marquee = cast["marquee"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"]
        #marquee.set_text("")
        #if paddle.get_position().equals(ball.get_position()):
           # pass
        if ball.get_position().get_y() < 1:
            ball.set_velocity(ball.get_velocity().reverse())
            pass
        