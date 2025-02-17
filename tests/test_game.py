import pytest
from longest_word.game import Game

class TestGame:
    def test_game_initialization(self):
        # Setup
        game = Game()

        # Exercise
        grid = game.grid

        # Verify
        assert isinstance(grid, str), "Grid should be a string"
        assert len(grid) == 9, "Grid should contain exactly 9 characters"
        assert grid.isupper(), "Grid should only contain uppercase letters"

        # Teardown (not needed in this case)

    def test_is_valid_word_valid_case(self):
        # Setup
        game = Game()
        game.grid = "BAROQUEZX"

        # Exercise & Verify
        assert game.is_valid("BAROQUE") == True, "BAROQUE should be valid"

    def test_is_valid_word_invalid_case(self):
        # Setup
        game = Game()
        game.grid = "BAROQUEZX"

        # Exercise & Verify
        assert game.is_valid("BAROQUUE") == False, "BAROQUUE should be invalid due to extra U"

    def test_is_valid_word_partial_match(self):
        # Setup
        game = Game()
        game.grid = "ABCDEFGHI"

        # Exercise & Verify
        assert game.is_valid("JUMP") == False, "JUMP should be invalid as J is not in the grid"

    def test_empty_word_is_invalid(self):
        # Setup
        new_game = Game()
        # Verify
        assert new_game.is_valid('') is False

    def test_is_valid(self):
        # Setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        # Exercise
        new_game.grid = test_grid  # Force the grid to a test case
        # Verify
        assert new_game.is_valid(test_word) is True
        # Teardown
        assert new_game.grid == test_grid  # Make sure the grid remained untouched

    def test_is_invalid(self):
        # Setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        # Exercise
        new_game.grid = test_grid  # Force the grid to a test case
        # Verify
        assert new_game.is_valid(test_word) is False
        # Teardown
        assert new_game.grid == test_grid  # Make sure the grid remained untouched
