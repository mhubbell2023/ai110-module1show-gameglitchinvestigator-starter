# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Game Purpose
Game Glitch Investigator is a number guessing game built using Python and Streamlit. Players select a difficulty level and try to guess a randomly generated number within a limited number of attempts. The game provides higher or lower hints and tracks the player's score.

### Bugs Found
I identified three bugs while testing the game:
1. The game displayed incorrect higher/lower hints, sometimes telling players to guess lower even when they entered 1.
2. After starting a new game, the Submit button stopped processing guesses because the game state wasn't properly reset.
3. Changing the difficulty didn't update the displayed instructions to match the correct guessing range and attempt limit.

### Fixes Applied
I used GitHub Copilot to fix the first two bugs. I corrected the higher/lower comparison messages and improved how the game handles number types. I also updated the New Game functionality to properly reset the score, attempts, status, and guess history. Additionally, I refactored the game logic into `logic_utils.py` to make the code easier to maintain and test. I used pytest and manual testing to verify the changes.

## 📸 Demo Walkthrough

## Demo Walkthrough

1. User launches the game and selects Normal difficulty.
2. User enters a guess of 40, and the game responds with "Too Low" and tells them to go higher.
3. User enters a guess of 70, and the game responds with "Too High" and tells them to go lower.
4. User continues guessing, and the score updates after each attempt.
5. User guesses the correct number, and the game displays a winning message and final score.
6. User clicks "New Game," which resets the score, attempts, and guess history.
7. User can submit new guesses and receive feedback, confirming that the reset bug has been fixed.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
