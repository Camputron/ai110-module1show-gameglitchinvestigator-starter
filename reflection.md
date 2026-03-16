# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  - If the user guesses a number greater than the target value, then the program will tell the user to guess higher when in reality, the target is lower.
  - If the user guesses a number lower than the target value, then the program will tell the user to guess lower when in reality, the target is higher.
  - When changing the difficulty and starting a new game, the text on the page doesn't re-render to notify the user to change their respective guessing range.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  - Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  - Copilot suggested using Streamlit's `st.session_state` to persist the secret number across reruns so it wouldn't regenerate every time the user clicked "Submit." I verified this by running the app, opening the Developer Debug Info tab, and confirming the secret number stayed the same between guesses.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  - Copilot initially suggested swapping only one of the hint messages when fixing the higher/lower logic, but both hint conditions were reversed. I verified this by playing the game with the debug panel open — when my guess was above the secret number, the app still said "Go HIGHER" until I fixed both conditions.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  - By re-running the app and testing where the bugs occured.

- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.

  - I ran `pytest` on the tests in `test_game_logic.py`, which includes tests for `check_guess()` — verifying that guessing the correct number returns "Win," guessing too high returns "Too High," and guessing too low returns "Too Low." These tests confirmed that my logic fixes were working correctly and that the hint directions were no longer reversed.

- Did AI help you design or understand any tests? How?

  - Yes, Copilot helped me understand what the test assertions should look like and how `check_guess()` returns a tuple of (outcome, message). It also helped me see that the tests import from `logic_utils.py`, which meant I needed to refactor the game logic out of `app.py` and into that module for the tests to work.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  - Every time you interact with a Streamlit app — clicking a button, typing in a box, changing a slider — Streamlit reruns your entire Python script from top to bottom. This means any regular variable you define gets reset to its initial value on every interaction. To keep data alive between reruns, you use `st.session_state`, which is like a persistent dictionary that Streamlit remembers across clicks. For example, the secret number in our game had to be stored in `st.session_state` so it wouldn't regenerate every time the player submitted a guess.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  - I want to keep the habit of always testing with a debug/info panel open so I can see the internal state of the app while I interact with it. In this project, the Developer Debug Info tab let me see the secret number and verify that hints were correct. Combining that kind of manual testing with automated pytest tests gives me confidence that the code actually works, not just that it looks right.

- What is one thing you would do differently next time you work with AI on a coding task?

  - Next time I would read through the AI-generated code more carefully before running it, rather than just trusting it and debugging after. A quick read would have caught the reversed hint logic and the missing session state immediately, saving time.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  - This project showed me that AI-generated code can look convincing and mostly correct while still containing subtle logic errors that break the app. It reinforced that AI is a useful starting point, but I still need to understand and verify every line it writes and its semtantics.
