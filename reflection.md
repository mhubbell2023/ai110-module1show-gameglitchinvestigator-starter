# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.


| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Enter a guess of 1 | Game should say "Too Low" or indicate a correct guess | Game always says "Go Lower" even though 1 is the minimum | None observed |
| Start a new game and submit a guess | Submit button should process the guess and display feedback | Submit button is visible but clicking it does nothing | Not checked |
| Change the difficulty setting | Instructions should update to show the correct range and attempts | Instructions still say "Guess a number between 1 and 100. Attempts left: 6" | None observed |


## 2. How did you use AI as a teammate?

Which AI tools did you use on this project?

I used ChatGPT and GitHub Copilot throughout this project. ChatGPT helped me understand the assignment requirements, identify potential causes of bugs, and plan my debugging process. I used GitHub Copilot in VS Code to make changes to my code, refactor functions, and generate automated tests.

Give one example of an AI suggestion that was correct.

One correct suggestion was to move the check_guess() function from app.py into logic_utils.py and fix the reversed higher/lower hints. Copilot updated the comparisons and corrected the messages displayed to the player. I verified the fix by manually testing the game with different guesses and checking that the hints matched the secret number.

Give one example of an AI suggestion you did not accept as written.

One suggestion I changed was Copilot's approach to handling different data types in the check_guess() function. It included a fallback that compared guesses and secret numbers as strings if a type error occurred. I noticed that this was unnecessarily complicated and could produce incorrect comparisons. I asked Copilot to simplify the function so it consistently uses integer comparisons instead. I verified the updated approach by running my pytest tests and checking that the guessing hints still worked correctly in the game.

---

## 3. Debugging and testing your fixes

How did you decide whether a bug was really fixed?

I determined whether a bug was fixed by testing the game again and comparing its behavior to what I originally expected. I checked that the higher/lower hints were correct and that starting a new game properly reset the game state. I also reviewed the code changes Copilot made to understand how the fixes worked.

Describe at least one test you ran and what it showed you about your code.

One test involved checking the check_guess() function using pytest. I tested a guess of 60 against a secret number of 50 to verify that the game returned "Too High" and instructed the player to guess lower. I also tested the reset functionality to check that the game correctly resets its status, score, attempts, and guess history. These tests helped verify that the updated functions behaved as expected.

Did AI help you design or understand any tests? How?

Yes, I used GitHub Copilot to help generate pytest tests for the bugs I fixed. It helped me easily identify different scenarios to test, including guesses that were too high, too low, or correct. ChatGPT also helped me understand why wach test was important and why automated testing is useful. This showed me how AI can speed up testing while still allowing me to review and verify the results myself.

---

## 4. What did you learn about Streamlit and state?

How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the Python script from top to bottom whenever a user interacts with the app, such as clicking a button or entering a value. Normally, variables would reset each time the script runs, but session state allows the app to remember important information between reruns. For example, in my guessing game, session state keeps track of the secret number, score, attempts, and game status. Without it, the game would lose its progress every time the player submitted a guess. Session state makes it possible to create interactive apps that remember what the user has already done.

---

## 5. Looking ahead: your developer habits

What is one habit or strategy from this project that you want to reuse in future labs or projects?

One strategy I want to continue using is writing automated tests with pytest after making changes to my code. This helped me verify that the bugs were actually fixed instead of just assuming the code worked. I also liked separating the game logic from the UI because it made the functions easier to understand and test.

What is one thing you would do differently next time you work with AI on a coding task?

Next time, I would be more specific with my prompts to hopefully get the ouput i expect easier and limit having to give further instructions. 

In one or two sentences, describe how this project changed the way you think about AI-generated code.

This project showed me that even when AI-generated code looks correct and runs without errors, it can still contain logical bugs. I learned that AI is a useful tool for speeding up development, but it's important to understand, review, and test its suggestions instead of blindly trusting them.
