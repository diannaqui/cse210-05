import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # if not self._is_game_over:
        #     self._handle_segment_collision(cast)
        #     self._handle_game_over(cast)
        self._handle_segment_collision(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """

        cycles = cast.get_actors("cycles")
        scores = cast.get_actors("scores")

        cycle_1 = cycles[0]
        cycle_2 = cycles[1]

        head_1 = cycle_1.get_head()
        head_2 = cycle_2.get_head()
        segments_1 = cycle_1.get_segments()[1:]
        segments_2 = cycle_2.get_segments()[1:]

        for segment in segments_1:
            if head_2.get_position().equals(segment.get_position()):
                # self._is_game_over = True
                scores[0].add_points(1)
                cycle_2.reset()
        for segment in segments_2:
            if head_1.get_position().equals(segment.get_position()):
                # self._is_game_over = True
                scores[1].add_points(1)
                cycle_1.reset()


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            for cycle in cycles:
                segments = cycle.get_segments()

                for segment in segments:
                    segment.set_color(constants.WHITE)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)