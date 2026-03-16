from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # hint should tell the user to go lower


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message  # hint should tell the user to go higher


def test_hard_difficulty_range():
    # Hard mode should have a larger range than Normal (1-100)
    low, high = get_range_for_difficulty("Hard")
    assert high > 100


def test_score_on_win():
    # Winning on attempt 1 should give 90 points (100 - 10*1)
    score = update_score(0, "Win", 1)
    assert score == 90


def test_score_on_wrong_guess():
    # A wrong guess should always subtract 5 points
    score = update_score(50, "Too High", 1)
    assert score == 45
    score = update_score(50, "Too High", 2)
    assert score == 45  # should be consistent regardless of attempt parity


# --- Challenge 1: Advanced Edge-Case Tests ---

def test_parse_negative_number():
    # Negative numbers should be parsed successfully
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None


def test_parse_decimal_input():
    # Decimal input like "3.7" should be truncated to an integer
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3
    assert err is None


def test_parse_extremely_large_number():
    # Very large numbers should still parse without crashing
    ok, value, err = parse_guess("999999999")
    assert ok is True
    assert value == 999999999
    assert err is None


def test_parse_non_numeric_input():
    # Letters and symbols should be rejected gracefully
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_empty_string():
    # Empty string should prompt the user to enter a guess
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_none_input():
    # None input should be handled gracefully
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_check_guess_negative_number():
    # A negative guess against a positive secret should be "Too Low"
    outcome, message = check_guess(-10, 50)
    assert outcome == "Too Low"


def test_score_floor_on_late_win():
    # Winning on attempt 20 should still give at least 10 points (floor)
    score = update_score(0, "Win", 20)
    assert score == 10


def test_unknown_difficulty_returns_default():
    # An unrecognized difficulty should fall back to Normal range (1-100)
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100
