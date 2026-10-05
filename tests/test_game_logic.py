from logic_utils import check_guess
from pathlib import Path

from streamlit.testing.v1 import AppTest

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


def _app():
    return AppTest.from_file(APP_PATH)


def _button_by_label(at, label):
    for button in at.button:
        if button.label == label:
            return button
    raise AssertionError(f"Button not found: {label}")


def _submit_guess(at, guess):
    at.text_input(key="guess_input_Normal").input(str(guess))
    return _button_by_label(at, "Submit Guess 🚀").click().run()


def _messages(elements):
    return [element.value for element in elements]


def _set_playing_state(at, secret, attempts=0):
    at.session_state["secret"] = secret
    at.session_state["attempts"] = attempts
    at.session_state["status"] = "playing"
    at.session_state["history"] = []
    at.session_state["score"] = 0


# Covers the New Game status reset after a lost game.
def test_new_game_after_game_over_fix():
    at = _app().run()
    at.session_state["status"] = "lost"
    at = at.run()

    assert any("Game over" in message for message in _messages(at.error))

    at = _button_by_label(at, "New Game 🔁").click().run()

    assert at.session_state["status"] == "playing"
    assert not any("Game over" in message for message in _messages(at.error))
    assert at.text_input(key="guess_input_Normal").label == "Enter your guess:"
    assert _button_by_label(at, "Submit Guess 🚀").label == "Submit Guess 🚀"


# Covers reversed hints and numeric comparisons on odd and even attempts.
def test_hints_point_the_right_way_fix():
    at = _app().run()
    _set_playing_state(at, secret=50, attempts=0)
    at = at.run()

    at = _submit_guess(at, 80)
    assert any("LOWER" in message for message in _messages(at.warning))
    assert not any("HIGHER" in message for message in _messages(at.warning))

    at = _submit_guess(at, 20)
    assert any("HIGHER" in message for message in _messages(at.warning))
    assert not any("LOWER" in message for message in _messages(at.warning))

    _set_playing_state(at, secret=9, attempts=1)
    at = at.run()

    at = _submit_guess(at, 10)
    assert any("LOWER" in message for message in _messages(at.warning))
    assert not any("HIGHER" in message for message in _messages(at.warning))
    assert at.session_state["score"] == 5
