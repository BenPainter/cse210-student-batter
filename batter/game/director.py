from time import sleep
from game import constants


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)
            if self._cast["ball"][0].get_position().get_y() == int(constants.MAX_Y - 1):
               self._keep_playing = False
               print("-------------------------")
               print("        GAME OVER")
               print("-------------------------")
            if len(self._cast["brick"]) == 0:
                self._keep_playing = False
                print("You Win!!")
                print("That's rather impressive that you did that.")


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            self._cast = action.execute(self._cast)