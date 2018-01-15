import tetris1

def test_simple_falling():
    """Test that calling the game's tick() method makes the block fall"""

    game = tetris1.Tetris()
    x1, y1 = game.block_position

    game.tick()
    x2, y2 = game.block_position

    assert x2 == x1  # no movement to the side
    assert y2 == y1 + 1  # the block fell down by 1 pixel
