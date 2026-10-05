# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Answer: Visually, the UI looks just fine. Nothing wrong at first but if you look closer you start to notice bugs. Hints are almost always wrong. Either the new game button is bugged or there is a bug with the red ui element that appears after you've ran out of attempts. The red ui ("Game over. Start a new game to try again") doesn't go away even after pressing "New Game". This might be a mix of a bugged button and ui element. 

- List at least two concrete bugs you noticed at the start  
Answer: 1. After further testing the New Game button is definetly bugged and the red ui game over element is definetly a result of it. The History list also does not clear after pressing the New Game button. Pressing the new game button ALSO adds to the list registering as another "Submit Guess" 2. After seeing the example answer was given, I've noticed that the hint bug is opposite to the hints instead of completely random

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
**Bug Reproduction Log**

| # | Input | Expected Behavior | Actual Behavior | Code Location / Cause |
|---|-------|-------------------|-----------------|-----------------------|
| 1 | New Game after game over | The red game over message should go away and the game should restart. | The red UI ("Game over. Start a new game to try again") doesn't go away even after pressing New Game. | The `new_game` block in `app.py` (around lines 134-138) resets `attempts` and `secret` but never sets `status` back to `"playing"`. |
| 2 | New Game after guesses are in history | The History list should clear and New Game should not count as a guess. | The History list does not clear, and pressing New Game adds to the list like another Submit Guess. | The `new_game` block in `app.py` (around lines 134-138) never resets `st.session_state.history`. |
| 3 | Show hint | The hint should point me toward the right answer. | The hints are opposite of what they should be instead of completely random. | The return messages in `check_guess` in `app.py` (around lines 36-47). |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude to refine Codex (Chatgpt 5.5)
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I used AI to format the bug table above and was accurate because I told it to use my answers above the table instead of generating new observations
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
Over-engineered with the table due to have excessive wording and more than 3 answers that I did not come up with. I had to make answers "simplier"

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Whether the test passed and the UI changes reflect the fixes too
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I ran pytest using Streamlit's AppTest to check the two bugs I fixed. One test loses a game, clicks New Game, and checks that the red "Game over" message is gone and the game is back to "playing". The other submits guesses above and below the secret on odd and even attempts and checks that the hints say Go LOWER and Go HIGHER correctly. When I stashed my fixes both tests failed, and with the fixes back they passed, which showed me the tests were actually catching the bugs and that my changes caused the difference.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
