from logic_utils import check_guess, create_new_game_state, get_range_for_difficulty


def test_guess_too_high_when_secret_is_lower():
    # If the secret is 50 and the guess is 60, the player should be told to go lower.
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")


def test_guess_too_low_when_secret_is_higher():
    # If the secret is 50 and the guess is 30, the player should be told to go higher.
    result = check_guess(30, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_winning_guess():
    # If the secret is 50 and the guess is 50, the round should be marked as a win.
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high_when_secret_is_string_number():
    # If the secret is stored as a string like "50", the comparison should still work.
    result = check_guess(60, "50")
    assert result == ("Too High", "📉 Go LOWER!")


def test_new_game_state_resets_attempts_score_and_status():
    # A fresh game should start with no attempts, a zero score, an active status,
    # and an empty guess history to match the reset behavior in the app.
    state = create_new_game_state("Normal")

    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []


def test_new_secret_is_within_selected_difficulty_range():
    # Each new game should generate a secret number inside the range for the chosen
    # difficulty, so the reset remains valid for Easy, Normal, and Hard modes.
    for difficulty in ["Easy", "Normal", "Hard"]:
        low, high = get_range_for_difficulty(difficulty)
        state = create_new_game_state(difficulty)

        assert low <= state["secret"] <= high
