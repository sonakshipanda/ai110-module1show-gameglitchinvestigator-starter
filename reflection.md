# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- When I first ran the game, it looked like a simple number guessing game built with Streamlit. It had a sidebar for difficulty settings, a text input for guesses, and a submit button. 
- Bug 1 — The hints were backwards. When I guessed a number higher than the secret, the game told me "Go HIGHER!" instead of telling me to go lower. And when I guessed too low, it said "Go LOWER!" The hints actively pushed me in the wrong direction.
Hard mode was actually easier than Normal. The difficulty ranges were wrong — Hard only went from 1 to 50, while Normal went from 1 to 100. A smaller range means fewer numbers to guess from, making Hard the easiest non-Easy mode.
The game always says "Guess a number between 1 and 100" no matter what difficulty you pick. When I switched to Easy mode, the sidebar correctly showed "Range: 1 to 20," but the main game area still said "Guess a number between 1 and 100." This is confusing because you don't know which range to trust, and you might waste guesses on numbers outside the actual range.

---

## 2. How did you use AI as a teammate?

- I used Claude to help me identify and fix bugs in this project. I also used VS Code Copilot's Agent mode to help with refactoring and test generation.
- I asked Claude to help me identify bugs in app.py. It correctly pointed out that the hint messages in check_guess() were reversed  "Go HIGHER!" was showing when the guess was too high, and "Go LOWER!" when the guess was too low. I verified this by playing the game, guessing a number I knew was above the secret (using the debug panel), and confirming that the hint now pointed me in the right direction after the fix.
- hen I first asked Claude about the bugs, it flagged the secret number's type changing on even attempts as something I'd notice while playing. In reality, that bug is invisible to the player  you'd only catch it by reading the code. The symptoms (unreliable hints) overlap with the reversed hints bug, so it was misleading to list it as a separately observable issue. I verified this by playing the game and realizing I couldn't distinguish this bug from the reversed hints.


---

## 3. Debugging and testing your fixes

- I decided a bug was fixed by doing two things: running pytest to check the logic programmatically, and playing the game manually to confirm the experience felt right.
- I wrote a test called test_too_high_message_says_lower() that calls check_guess(60, 50) and asserts that the message contains "LOWER." Before the fix, the message would have said "HIGHER," so this test specifically targets the reversed hints bug. All 6 tests passed after the fix.
- AI helped me partially design the tests by suggesting what to assert  not just checking the outcome string ("Too High") but also checking that the player-facing message contained the correct directional word. This made the tests more thorough.

---

## 4. What did you learn about Streamlit and state?

- The secret number kept changing in the original app because Streamlit reruns the entire script from top to bottom every time the user interacts with the page. If the secret number was generated outside of st.session_state, it would get a new random value on every rerun.
- Streamlit is like a whiteboard that gets erased and redrawn every time you click a button. If you want something to not disappear between redraws, you have to put it in a special storage box called session_state. Otherwise it gets wiped clean every time.
- The fix that gave the game a stable secret number was the if "secret" not in st.session_state check  this only generates a new random number on the very first run, and keeps the same value for every rerun after that.

---

## 5. Looking ahead: your developer habits

- One habit I want to reuse is writing targeted tests before moving on. Running pytest after each fix gave me immediate confidence that the change actually worked, rather than just hoping it did.

- Next time I work with AI on a coding task, I would ask it to explain the bug before giving me a fix. In this project I sometimes got a fix without fully understanding the root cause first, which made it harder to verify.

- This project changed how I think about AI-generated code. it showed me that AI can write code that looks clean and functional but still has subtle logic errors. You can't just trust it blindly; you need to read the code, test it, and verify the behavior yourself.