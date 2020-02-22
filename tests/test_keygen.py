from piccolo_cipher import piccolokeygen

def test_key():
    k80 = piccolokeygen.piccolokeygen(80)
    assert len(k80) == 20
    k128 = piccolokeygen.piccolokeygen(128)
    assert len(k128) == 32