from hockeyclock.backend.player import Player, PositionType


def test_player_constructor():
    player = Player(number=24)
    assert player.number == 24
    assert player.position == None
    assert player.forename == None
    assert player.surname == None
    assert player.pass_number == None


def test_player_constructor_with_optionals():
    player = Player(number=24, position="C", forename="Kilian", surname="Märkl", pass_number=1234)
    assert player.number == 24
    assert player.position == "C"
    assert player.forename == "Kilian"
    assert player.surname == "Märkl"
    assert player.pass_number == 1234
