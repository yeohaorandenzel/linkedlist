############################### 72 chars ###############################

from datastruct import LinkedList

# Maze data file representation
MAZE = {
    "path": "0",
    "wall": "1",
}

# Symbol mapping for maze display
SYMBOLS = {
    "wall": "█",
    "space": " ",
    "here": "H",
    "option": "?",
    "visited": ".",
}


class Maze:
    """Encapsulates a Maze game and its methods.
    
    Arguments
        - filename: str
          The path name of the maze data file.

    Attributes
        - filename: str
          The path name of the maze data file from which maze data was
          imported.
        - start: coord
          The starting coordinate of the maze.
        - end: coord
          The ending coordinate of the maze.
        - x_size: int
          The width of the maze.
        - y_size: int
          The height of the maze.

    Methods
        - display()
          Displays the maze
        - around(coord)
          Returns a list of coordinates around the coordinate
        - 
    """

    def __init__(self, filename: str) -> None:
        self.import_from(filename)

    def __repr__(self) -> str:
        return f"Maze({self.filename})"

    def import_from(self, filename: str) -> None:
        """Import maze data from a file into the instance.

        Arguments
            - filename: str
        """
        self._data: list[str] = []
        with open(filename, "r") as f:
            for line in f:
                self._data.append(line.strip())
        self.filename = filename
        self.y_size = len(self._data)
        self.x_size = len(self._data[0])

        # Determine maze start & end
        start_index = self._data[0].index(MAZE["path"])
        self.start = (0, start_index)

        end_index = self._data[-1].index(MAZE["path"])
        self.end = (self.y_size - 1, end_index)

    def ispath(self, coord: tuple[int, int]) -> bool:
        """Returns True if the coordinate is a valid path.

        Arguments
            - y: int
              The y-coordinate.
            -x: int
              The x-coordinate.

        Returns
            True if the coordinate is a valid path,
            otherwise False.
        """
        y, x = coord
        if not (0 <= x <= self.x_size):
            return False
        if not (0 <= y <= self.y_size):
            return False
        y, x = coord
        return self._data[y][x] == MAZE["path"]

    def around(self, coord: tuple[int, int]) -> list[tuple[int, int]]:
        """Determine possible path coordinates around here.

        Arguments
            - here: tuple[int, int]
              The target coordinate, as a 2-integer tuple.

        Return
            [(y, x), ...]
        """
        y, x = coord
        paths = []
        for adj_y, adj_x in [
            (y - 1, x),
            (y, x - 1),
            (y, x + 1),
            (y + 1, x),
        ]:
            adjacent_coord = (adj_y, adj_x)
            if self.ispath(adjacent_coord):
                paths.append(adjacent_coord)
        return paths

    def display(
            self,
            # Required arguments
            position: tuple[int, int],
            *,  # Optional keyword arguments
            options: LinkedList | None = None,
            visited: list[tuple[int, int]] | None = None,
    ) -> None:
        """Print the maze."""
        for y, row in enumerate(self._data):
            for x, cell in enumerate(row):
                coord = (y ,x)
                if cell == MAZE["wall"]:
                    print(SYMBOLS["wall"], end="")
                elif coord == position:
                    print(SYMBOLS["here"], end="")
                elif options and options.contains(coord):
                    print(SYMBOLS["option"], end="")
                elif visited and coord in visited:
                    print(SYMBOLS["visited"], end="")
                elif cell == MAZE["path"]:
                    print(SYMBOLS["space"], end="")
            print()  # linebreak