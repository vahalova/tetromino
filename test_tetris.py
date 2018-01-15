import pytest

import tetris1

def test_simple_falling():
    """Test that calling the game's tick() method makes the block fall"""

    game = tetris1.Tetris()
    row1, col1 = game.block_position

    game.tick()
    row2, col2 = game.block_position

    assert col2 == col1  # no movement to the side
    assert row2 == row1 + 1  # the block fell down by 1 pixel


@pytest.mark.parametrize('amount', range(-3, 4))
def test_moving(amount):
    """Test that calling the game's move() method moves the block laterally"""

    game = tetris1.Tetris()
    row1, col1 = game.block_position

    game.move(amount)
    row2, col2 = game.block_position

    assert col2 == col1 + amount  # movement to the side
    assert row2 == row1  # the block didn't fall
