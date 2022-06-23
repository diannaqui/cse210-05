import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.

    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction_1 = Point(0, constants.CELL_SIZE * -1)
        self._direction_2 = Point(0, constants.CELL_SIZE * -1)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # Controls for 1st cycle
        cycle_1 = cast.get_actors("cycles")[0]

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction_1 = Point(-constants.CELL_SIZE, 0)
            cycle_1.grow_tail()

        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction_1 = Point(constants.CELL_SIZE, 0)
            cycle_1.grow_tail()
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction_1 = Point(0, -constants.CELL_SIZE)
            cycle_1.grow_tail()
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction_1 = Point(0, constants.CELL_SIZE)
            cycle_1.grow_tail()
        cycle_1.turn_head(self._direction_1)


        # Controls for 2nd snake
        cycle_2 = cast.get_actors("cycles")[1]

        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction_2 = Point(-constants.CELL_SIZE, 0)
            cycle_2.grow_tail()
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction_2 = Point(constants.CELL_SIZE, 0)
            cycle_2.grow_tail()
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction_2 = Point(0, -constants.CELL_SIZE)
            cycle_2.grow_tail()
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction_2 = Point(0, constants.CELL_SIZE)
            cycle_2.grow_tail()
        cycle_2.turn_head(self._direction_2)