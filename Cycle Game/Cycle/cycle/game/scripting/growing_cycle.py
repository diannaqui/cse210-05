import constants
from game.scripting.action import Action


class GrowingCycle(Action):
    """
    An input action that controls the snake.
    
    The responsibility of GrowingCycle is to control the growth of the tail.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self):
        """Constructs a new GrowingCycle using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._counter = 0

    def execute(self, cast, script):
        """Executes the growing cycle action.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        pass

