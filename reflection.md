# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

    When I played the game, I noticed that the hint suggestions were incorrect. While the secret number was 79, I was told to "go lower" when my input was 23. Also, I noticed that when my input was 1 or 0, it told me to "go lower" even though the value of 1 is an endpoint. To go along with that, the user is told that they have 8 attempts, but the program ends at 7. Lastly, when selecting "new game" after completing the previous one, the program no longer executes. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input      | Expected Behavior | Actual Behavior | Console Output / Error |
|------------|-------------------|-----------------|------------------------|
| guess of 0 | "Too Low" hint    | "Go Lower" hint | n/a                    |
| guess of 23| "Go Higher" hint  | "Go Lower" hint | n/a                    |
| "New Game" | reset game        | game doesn't run| n/a                    |
| 7th attempt| 1 attempt left    | game ends       | n/a                    |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

    I used Gemini as my AI tool on this project. After explaining the context of the program to Gemini and one of the problems I was encountering, it recognized an error in the code's logic for text feedback after numeric comparison. Gemini sugggested to swap the feedback message and change the numeric conversion method from str() to int() for secret in the function check_guess() in app.py. I verified this result simply by re-running the program and testing it by playing the game myself. 

    When trying to fix the number of attempts the player gets, Gemini did give me an incorrect suggestion. Gemini suggested that I fix the number the attempts start at from 1 to 0, which was correct, but it suggested to update the "Attempts left" text calculation to 'f"Attempts left: {attempt_limit - st.session_state.attempts}"', the same at it was before. This did not reflect the correct number of attempts at the start. I verified this result simply by re-running the program and testing it by playing the game myself. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

    I decided whether a bug was really fixed by manually testing the code. Everytime I would implement a change, I would re-run the program and test the game under the condition needed to revel the errors. For example, when fixing the numerical comparison and feedback test logic, I re-ran the code after changes and played the game as normal, while also entering values above and below the endpoint numbers. Whne the program functioned correctly or incorrectly, it showed me that either I have made the correct fix or that more work needs to be done. Since I opted to manually test the program, AI did not help me design any tests, but when I ran into logic issues, it did help me understand why my tests failed. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

    One habit/strategy I would continue to use is making use of GitHub Desktop in order to edit code in VS Code. It is something I have never done and make the process much easier. I don't think I would do anything differently when I comes to using AI on a coding task. I found it to be very helpful in its suggestions and that when it may have been incorrect, starting a new chat or light prompting was sufficient to reach the correct answer. 

    In terms of how my thinking has changed about AI generated code, I think it took away some of the negative connotation it holds. Naturally, it may feel like cheating, but I found that it is a really great tool to make coding much faster and more efficient. 