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


def test_l_edge_rotation():
    """Test an example of rotation near the edge"""

    # Start with L
    game = tetris1.Tetris()
    game.block = tetris1.L_BLOCK
    game.block_rotation = 1

    # print out the game (shows up when the test fails)
    print('Start:')
    tetris1.draw(game)

    # Move to the edge
    for i in range(game.width):
        game.move(1)

    edge_row, edge_col = game.block_position

    # print out the game again
    print('Edge:')
    tetris1.draw(game)

    # Rotate!
    game.rotate()

    rotated_row, rotated_col = game.block_position

    # print out the game again
    print('Rotated:')
    tetris1.draw(game)

    assert game.block_rotation == 2
    assert rotated_row == edge_row
    assert rotated_col == edge_col - 1
