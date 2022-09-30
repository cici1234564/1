from Table import Table
from Restaurant import Restaurant

from unittest import TestCase


def assert_equal(got, expected, msg):  # type: ignore
    """
    Simple assert helper
    """
    assert expected == got, "[{}] Expected: {}, got: {}".format(msg, expected, got)  # type: ignore


class TableRestaurantTestSuite(TestCase):
    def test_table_sample(self):
        # Initialise a table with distance 1
        table = Table(1)
        assert_equal(table.get_distance(), 1, "Table distance is incorrect")

        # Add 5 hobbits to the table
        for _ in range(5):
            table.add_hobbit()

        # Check that the table has been updated correctly
        assert_equal(table.is_table_full(), False, "Table is not currently full")
        assert_equal(table.is_dhe_only(), True, "Table is currently DHE only")
        assert_equal(table.is_elves_only(), False, "Table is not currently elves only")
        assert_equal(table.get_total_diners(), 5, "Table total diners count is incorrect")
        assert_equal(table.get_elves(), 0, "Table elves count is incorrect")
        assert_equal(table.get_distance(), 1, "Table distance is incorrect")

        # Add an elf and a human to the table
        table.add_elf()
        table.add_human()

        # Check that the table has been updated correctly
        assert_equal(table.is_table_full(), True, "Table is currently full")
        assert_equal(table.is_dhe_only(), False, "Table is not currently DHE only")
        assert_equal(table.is_elves_only(), False, "Table is not currently elves only")
        assert_equal(table.get_total_diners(), 7, "Table total diners count is incorrect")
        assert_equal(table.get_elves(), 1, "Table elves count is incorrect")
        assert_equal(table.get_distance(), 1, "Table distance is incorrect")

    def test_restaurant_sample(self):
        # Initialise the restaurant and start a new table
        restaurant = Restaurant()
        restaurant.start_new_table()

        # Check that the restaurant has been initialised correctly
        assert_equal(restaurant.get_number_tables(), 1, "Restaurant number of tables is incorrect")
        assert_equal(restaurant.get_number_diners(), 0, "Restaurant number of diners is incorrect")
        assert_equal(restaurant.get_number_hobbits(), 0, "Restaurant number of hobbits is incorrect")
        assert_equal(restaurant.get_number_elves(), 0, "Restaurant number of elves is incorrect")
        assert_equal(restaurant.get_number_dwarves(), 0, "Restaurant number of dwarves is incorrect")
        assert_equal(restaurant.get_number_humans(), 0, "Restaurant number of humans is incorrect")
        assert_equal(
            restaurant.get_least_crowded_table().get_distance(),
            1,
            "Restaurant least crowded table distance is incorrect",
        )
        assert_equal(
            restaurant.get_least_crowded_table().get_elves(),
            0,
            "Restaurant least crowded table elves count is incorrect",
        )

        # Let's add some diners to the restaurant
        restaurant.add_dwarf()
        restaurant.add_hobbit()
        restaurant.add_elf()

        # The restaurant should look something like this:
        """
        Table 1   Table 2
        --------  -------
        | D Ho |  | E   |
        |      |  |     |
        |      |  |     |
        |      |  |     |
        --------  -------
        """

        # Check that the restaurant has been updated correctly
        assert_equal(restaurant.get_number_tables(), 2, "Restaurant number of tables is incorrect")
        assert_equal(restaurant.get_number_diners(), 3, "Restaurant number of diners is incorrect")
        assert_equal(restaurant.get_number_hobbits(), 1, "Restaurant number of hobbits is incorrect")
        assert_equal(restaurant.get_number_elves(), 1, "Restaurant number of elves is incorrect")
        assert_equal(restaurant.get_number_dwarves(), 1, "Restaurant number of dwarves is incorrect")
        assert_equal(restaurant.get_number_humans(), 0, "Restaurant number of humans is incorrect")
        assert_equal(
            restaurant.get_least_crowded_table().get_distance(),
            2,
            "Restaurant least crowded table distance is incorrect",
        )
        assert_equal(
            restaurant.get_least_crowded_table().get_elves(),
            1,
            "Restaurant least crowded table elves count is incorrect",
        )

        # Let's add some more diners to the restaurant
        restaurant.add_human()
        restaurant.add_hobbit()
        restaurant.add_elf()
        restaurant.add_dwarf()

        # The restaurant should look something like this:
        """
        Table 1   Table 2   Table 3
        --------  -------  -------
        | D Ho |  | E Ho|  | E   |
        | Hu D |  |     |  |     |
        |      |  |     |  |     |
        |      |  |     |  |     |
        --------  -------  -------
        """

        # Check that the restaurant has been updated correctly
        assert_equal(restaurant.get_number_tables(), 3, "Restaurant number of tables is incorrect")
        assert_equal(restaurant.get_number_diners(), 7, "Restaurant number of diners is incorrect")
        assert_equal(restaurant.get_number_hobbits(), 2, "Restaurant number of hobbits is incorrect")
        assert_equal(restaurant.get_number_elves(), 2, "Restaurant number of elves is incorrect")
        assert_equal(restaurant.get_number_dwarves(), 2, "Restaurant number of dwarves is incorrect")
        assert_equal(restaurant.get_number_humans(), 1, "Restaurant number of humans is incorrect")
        assert_equal(
            restaurant.get_least_crowded_table().get_distance(),
            3,
            "Restaurant least crowded table distance is incorrect",
        )
        assert_equal(
            restaurant.get_least_crowded_table().get_elves(),
            1,
            "Restaurant least crowded table elves count is incorrect",
        )
