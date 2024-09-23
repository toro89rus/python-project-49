from brain_games.cli import welcome_user
from io import StringIO


def test_welcome_user(monkeypatch, capfd):
    name = StringIO("Bob")
    monkeypatch.setattr("sys.stdin", name)
    welcome_user()
    out, _ = capfd.readouterr()
    assert out == 'May I have your name? Hello, Bob!\n'
