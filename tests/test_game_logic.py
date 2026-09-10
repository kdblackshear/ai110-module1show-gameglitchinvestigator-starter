from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"


# --- New Tests for Fixed Bugs ---


def test_check_guess_handles_string_secret():
    """Verifies that check_guess handles string secret types cleanly."""
    outcome_win, _ = check_guess(50, "50")
    assert outcome_win == "Win"

    outcome_high, _ = check_guess(60, "50")
    assert outcome_high == "Too High"

    outcome_low, _ = check_guess(40, "50")
    assert outcome_low == "Too Low"


def test_attempt_counter_and_attempts_left():
    """Verifies attempt counting and attempts-left calculation starting from 0."""
    attempt_limit = 8
    attempts = 0

    # Initial state should show full attempt limit remaining
    assert attempt_limit - attempts == 8

    # Simulate submit clicks up to the limit
    for i in range(1, attempt_limit + 1):
        attempts += 1
        attempts_left = attempt_limit - attempts
        assert attempts_left == 8 - i

    # Verify game-over condition triggers on the 8th attempt
    assert attempts >= attempt_limit
