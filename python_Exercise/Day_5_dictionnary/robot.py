"""Robot simulator."""

# Cardinal directions.
NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

# Direction mappings for robot rotations.
LEFT_TURNS = {
    NORTH: WEST,
    WEST: SOUTH,
    SOUTH: EAST,
    EAST: NORTH,
}

RIGHT_TURNS = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH,
}


class Robot:
    """Represent a robot moving on a two-dimensional grid.

    A robot has a position defined by its x and y coordinates and a
    direction indicating where it is facing. It can move forward and
    rotate according to a sequence of instructions.
    """

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """Initialize a robot.

        Args:
            direction (str): Initial direction the robot is facing.
            x_pos (int): Initial horizontal position.
            y_pos (int): Initial vertical position.
        """
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def coordinates(self):
        """Return the robot's current coordinates."""
        return (self.x_pos, self.y_pos)

    def _advance(self):
        """Move the robot one unit forward."""

        if self.direction == NORTH:
            self.y_pos += 1

        elif self.direction == SOUTH:
            self.y_pos -= 1

        elif self.direction == EAST:
            self.x_pos += 1

        else:  # WEST
            self.x_pos -= 1

    def move(self, instructions):
        """Execute a sequence of robot instructions.

        Supported instructions:
            - A: Advance one unit.
            - L: Turn left.
            - R: Turn right.

        Args:
            instructions (str): Sequence of instructions to execute.
        """

        for instruction in instructions:
            if instruction == "A":
                self._advance()

            elif instruction == "L":
                self.direction = LEFT_TURNS[self.direction]

            elif instruction == "R":
                self.direction = RIGHT_TURNS[self.direction]

            else:
                raise ValueError(f"Invalid instruction: {instruction}")