from logic_utils import check_guess, get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# New tests for Bug Fix 1: Hint messages should point the correct direction
def test_too_high_message_says_lower():
    """When guess is too high, the message should say LOWER."""
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message


def test_too_low_message_says_higher():
    """When guess is too low, the message should say HIGHER."""
    outcome, message = check_guess(30, 50)
    assert "HIGHER" in message


# New test for Bug Fix 2: Hard mode should be harder than Normal
def test_hard_range_is_harder_than_normal():
    """Hard mode should have a larger range than Normal."""
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high