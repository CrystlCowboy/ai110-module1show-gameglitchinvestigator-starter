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

- [ To guess the right number and give you hints along the way ] Describe the game's purpose.
- [ I found three bugs. After a game over, pressing New Game doesn't clear the red "Game over" message because the `new_game` block in `app.py` resets `attempts` and `secret` but never sets `status` back to `"playing"`, and it also never clears the History list. The hints are also wrong: the messages in `check_guess` are reversed, so a guess that's too high says "Go HIGHER" and a guess that's too low says "Go LOWER". ] Detail which bugs you found.
- [ I fixed two bugs in app.py with Codex's help. The first was New Game after game over. When I lost, the game set status to "lost" and stored it in session state. Pressing New Game reset the attempts and the secret number, but it never set status back to "playing". So when Streamlit reran the app, it saw "lost" was still there and showed the red game over message again. I fixed it by resetting status to "playing" inside the New Game block. The second was the hints. In check_guess, the messages were backwards: a guess that was too high said "Go HIGHER" and a guess that was too low said "Go LOWER". There was also a second problem where the secret number was turned into a string on every other attempt, which made the game compare text instead of numbers, so hints were wrong in a different way. I swapped the messages so they point the right direction and stopped converting the secret to a string, so guesses are always compared as numbers. I left the History not clearing on New Game alone for now, since that is a separate bug. ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Guessed and entered 2 (Says to go HIGHER)
2. Guessed and entered 20 (Says to go HIGHER)
3. Guessed and entered 50 (Says to go HIGHER)
4. Guessed and entered 70 (Says to go LOWER)
5. Guessed and entered 60 (Says to go LOWER)
6. Guessed and entered 55 (Says to go HIGHER)
7. Guessed and entered 57 (I got it correct and had a nice balloon animation)

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
python -m pytest tests/test_game_logic.py -k fix -v
================================================================================================ test session starts =================================================================================================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\Justin\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Justin\OneDrive\Desktop\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 5 items / 3 deselected / 2 selected                                                                                                                                                                         

tests/test_game_logic.py::test_new_game_after_game_over_fix PASSED                                                                                                                                              [ 50%]
tests/test_game_logic.py::test_hints_point_the_right_way_fix PASSED                                                                                                                                             [100%]

========================================================================================== 2 passed, 3 deselected in 1.86s ===========================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
