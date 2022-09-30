"""
Table Class
----------

This class represents a table inside the restaurant. 

Each Table has the following static class properties:
    - capacity: The maximum number of people that can sit at the table

Each Table also has the following instance properties:
    - distance: The distance from the table to the door. The closest door is a distance of 1, the next closest is a distance of 2, etc.
    - hobbits: The number of hobbits sitting at the table
    - elves: The number of elves sitting at the table
    - dwarves: The number of dwarves sitting at the table
    - humans: The number of humans sitting at the table 

The class also supports the following functions:
    - __init__(self, distance, **kwargs): Initializes the table with the given distance from the door
    - is_table_full(self): Returns True if the table is full, False otherwise
    - is_elves_only(self): Returns True if the table consists only of elves
    - is_dhe_only(self): Returns True if the table consists of only dwarves, only hobbits or only elves
    - get_total_diners(self): Returns the total number of diners at the table
    - get_elves(self): Returns the number of elves at the table
    - get_distance(self): Returns the distance from the table to the door
    - add_hobbit(self): Adds a hobbit to the table
    - add_elf(self): Adds an elf to the table
    - add_dwarf(self): Adds a dwarf to the table
    - add_human(self): Adds a human to the table

Your task is to complete the following functions which are marked by the TODO comment.
You are free to add properties and functions to the class as long as the given signatures remain identical.
Good Luck!
"""


class Table:
    # This is the defined class property as above. This should not be changed.
    capacity: int = 7

    # These are the defined instance properties as above. Feel free to add any extra properties you need.
    distance: int
    hobbits: int
    elves: int
    dwarves: int
    humans: int
    # 添加一个属性：
    # count: 当前桌子被占据的座位
    count: int

    def __init__(self, distance: int, **kwargs) -> None:
        """
        The constructor for the Table class.
        :param distance: The distance of the table from the door.
        :param kwargs: Any extra arguments to be passed to the constructor.
        """
        # 初始化各个属性
        self.distance = distance
        self.hobbits = 0
        self.elves = 0
        self.dwarves = 0
        self.humans = 0
        self.count = 0

    def is_table_full(self) -> bool:
        """
        Returns whether the table is full or not.
        :return: True if the table is full, False otherwise.
        """
        # 总人数等于容量时，桌子为满
        return self.capacity == self.count

    def is_elves_only(self) -> bool:
        """
        Returns whether the table is only elves or not.
        There must be at least one elf at the table to be considered elves-only.
        :return: True if the table is only elves, False otherwise.
        """
        return self.elves == self.count and self.elves != 0

    def is_dhe_only(self) -> bool:
        """
        Returns whether the table is made up of only dwarves, only hobbits, or only elves.
        Note that at least one of the creatures must be at the table to be considered
        dwarf-only, hobbit-only, or elf-only.
        :return: True if the table is made up of only dwarves, only hobbits, or only elves.
        """
        # 检查桌子不为空，且只由这三种构成
        if self.count == 0:
            return False
        return self.count in [self.dwarves, self.hobbits, self.elves]

    def get_total_diners(self) -> int:
        """
        Returns the total number of diners at the table.
        :return: The total number of diners at the table.
        """
        return self.count

    def get_elves(self) -> int:
        """
        Returns the number of elves at the table.
        :return: The number of elves at the table.
        """
        return self.elves

    def get_distance(self) -> int:
        """
        Returns the distance of the table from the door.
        :return: The distance of the table from the door.
        """
        return self.distance

    def add_hobbit(self) -> None:
        """
        Adds a hobbit to the table.
        If the table is already full, this function should do nothing.
        """
        if self.is_table_full():
            return
        self.hobbits += 1
        self.count += 1

    def add_elf(self) -> None:
        """
        Adds an elf to the table.
        If the table is already full, this function should do nothing.
        """
        if self.is_table_full():
            return
        # 精灵只和精灵坐一起
        # if self.is_elves_only():
        self.elves += 1
        self.count += 1

    def add_dwarf(self) -> None:
        """
        Adds a dwarf to the table.
        If the table is already full, this function should do nothing.
        """
        if self.is_table_full():
            return
        self.dwarves += 1
        self.count += 1

    def add_human(self) -> None:
        """
        Adds a human to the table.
        If the table is already full, this function should do nothing.
        """
        if self.is_table_full():
            return
        # # 只要不是 dhe only, 人类就能加入
        # if not self.is_dhe_only():
        self.humans += 1
        self.count += 1
