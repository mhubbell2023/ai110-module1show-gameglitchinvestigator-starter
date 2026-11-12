import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def create_new_game_state(difficulty: str):
    """Return a fresh game state for a selected difficulty."""
    low, high = get_range_for_difficulty(difficulty)
    return {
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
        "secret": random.randint(low, high),
    }


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if isinstance(guess, str):
        guess = guess.strip()
    if isinstance(secret, str):
        secret = secret.strip()

    try:
        guess_value = int(guess)
        secret_value = int(secret)
    except (TypeError, ValueError):
        try:
            guess_value = int(float(guess))
            secret_value = int(float(secret))
        except (TypeError, ValueError) as exc:
            raise ValueError("Guess and secret must be numeric values.") from exc

    if guess_value == secret_value:
        return "Win", "🎉 Correct!"
    if guess_value > secret_value:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
