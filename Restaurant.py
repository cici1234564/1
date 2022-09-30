from Table import Table
import heapq

"""
Restaurant Class
----------

This class represents the entire restaurant which manages the tables and incoming customers. 

The Restaurant has no properties attached to it - you are free to add any properties you need.
Remember that the data structure backing the restaurant must be able to satisfy the
time requirements of the functions given below. Think about which data structure is best.

The class also supports the following functions:
    - __init__(self): Initializes the restaurant
    - start_new_table(self) -> Table: Starts a new table at the restaurant
    - add_hobbit(self): Adds a hobbit to the restaurant, following the requirements for seating
    - add_elf(self): Adds an elf to the restaurant, following the requirements for seating
    - add_dwarf(self): Adds a dwarf to the restaurant, following the requirements for seating
    - add_human(self): Adds a human to the restaurant, following the requirements for seating
    - get_least_crowded_table(self) -> Table: Returns the least crowded table in the restaurant. Should run in O(1) time.
    - get_number_tables(self) -> int: Returns the number of tables in the restaurant. Should run in O(1) time.
    - get_number_diners(self) -> int: Returns the number of diners in the restaurant. Should run in O(1) time.
    - get_number_hobbits(self) -> int: Returns the number of hobbits in the restaurant. Should run in O(1) time.
    - get_number_elves(self) -> int: Returns the number of elves in the restaurant. Should run in O(1) time.
    - get_number_dwarves(self) -> int: Returns the number of dwarves in the restaurant. Should run in O(1) time.
    - get_number_humans(self) -> int: Returns the number of humans in the restaurant. Should run in O(1) time.

Your task is to complete the following functions which are marked by the TODO comment.
You are free to add properties and functions to the class as long as the given signatures remain identical.
Good Luck!
"""


class Restaurant:
    tables = []

    def __init__(self):
        """
        The constructor for the Restaurant class.
        """
        self.number_diners = 0
        self.number_dwarves = 0
        self.number_hobbits = 0
        self.number_elves = 0
        self.number_humans = 0
        # 维护一个堆，可以每次以 O(1) 复杂度，求得 least_crowded_table
        self.q = []

    def start_new_table(self) -> Table:
        """
        Starts a new table at the restaurant.
        :return: The new table created.
        """
        distance = len(self.tables) + 1
        table = Table(distance)
        self.tables.append(table)
        self.add_q_table(table)
        return table

    def add_hobbit(self) -> None:
        """
        Adds a hobbit to the least crowded table in the restaurant.
        If there are multiple tables with the same number of diners,
        add the hobbit to the table closest to the door. If all the
        tables are full, start a new table.
        """
        self.number_hobbits += 1
        self.number_diners += 1
        table = self.get_least_crowded_table()
        # 如果这张桌子满了，需要新开一张桌子
        if table.is_table_full():
            table = self.start_new_table()

        self.del_q_table(table)
        table.add_hobbit()
        self.add_q_table(table)

    def add_elf(self) -> None:
        """
        Adds an elf to the first table closest to the door that consists
        solely of elves. If such a table does not exist, start a new table
        """
        self.number_elves += 1
        self.number_diners += 1
        # 首先检查是否有没有满的、只有精灵的桌子
        for table in self.tables:
            if not table.is_table_full() and table.is_elves_only():
                # table 发生变动，需要更新堆中的元素
                self.del_q_table(table)
                table.add_elf()
                self.add_q_table(table)
                break
        else:
            # 没有的话就新开一桌
            table = self.start_new_table()
            self.del_q_table(table)
            table.add_elf()
            self.add_q_table(table)

    def add_dwarf(self) -> None:
        """
        Adds a dwarf to the table with the fewest elves. If multiple tables have
        an equal amount of elves, the one closest to the door is chosen. If no such
        table can be found or all the tables are full, start a new table.
        """
        self.number_dwarves += 1
        self.number_diners += 1
        # 尝试找到最少精灵的桌子
        found = False
        m = float('inf')
        table = None
        for t in self.tables:
            if not t.is_table_full() and t.get_elves() < m:
                m = t.get_elves()
                table = t
                found = True
        # 如果没有找到，需要新建桌子
        if not found:
            table = self.start_new_table()
        self.del_q_table(table)
        table.add_dwarf()
        self.add_q_table(table)

    def add_human(self) -> None:
        """
        Adds a human to the closest table that is not dwarf-only,
        elf-only or hobbit-only. If no such table exists, start a new table.
        """
        self.number_humans += 1
        self.number_diners += 1
        for table in self.tables:
            if not table.is_table_full() and table.is_dhe_only():
                self.del_q_table(table)
                table.add_dwarf()
                self.add_q_table(table)
                break
        else:
            table = self.start_new_table()
            self.del_q_table(table)
            table.add_human()
            self.add_q_table(table)

    def get_least_crowded_table(self) -> Table:
        """
        Returns the least crowded table in the restaurant.
        If there are multiple tables with the same number of diners,
        return the table closest to the door.
        This should run in O(1) time.
        :return: The least crowded table in the restaurant. If there are no tables, return None.
        """
        if not self.q:
            return None
        # 堆的第一个元素，是最符合条件的
        return self.q[0][2]

    def get_number_tables(self) -> int:
        """
        Returns the number of tables in the restaurant.
        This should run in O(1) time.
        :return: The number of tables in the restaurant.
        """
        return len(self.tables)

    def get_number_diners(self) -> int:
        """
        Returns the total number of diners in the restaurant.
        This should run in O(1) time.
        :return: The total number of diners in the restaurant.
        """
        return self.number_diners

    def get_number_hobbits(self) -> int:
        """
        Returns the total number of hobbits in the restaurant.
        This should run in O(1) time.
        :return: The total number of hobbits in the restaurant.
        """
        return self.number_hobbits

    def get_number_elves(self) -> int:
        """
        Returns the total number of elves in the restaurant.
        This should run in O(1) time.
        :return: The total number of elves in the restaurant.
        """
        return self.number_elves

    def get_number_dwarves(self) -> int:
        """
        Returns the total number of dwarves in the restaurant.
        This should run in O(1) time.
        :return: The total number of dwarves in the restaurant.
        """
        return self.number_dwarves

    def get_number_humans(self) -> int:
        """
        Returns the total number of humans in the restaurant.
        This should run in O(1) time.
        :return: The total number of humans in the restaurant.
        """
        return self.number_humans

    # TODO :Add any other functions that you need
    def del_q_table(self, table):
        """
        从堆中删除 table 对应元素
        """
        self.q.remove((table.count, table.distance, table))

    def add_q_table(self, table):
        """
        往堆中添加 table 对应元素
        """
        heapq.heappush(self.q, (table.count, table.distance, table))
