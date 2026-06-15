# 🕵️ Spy Number Game

A spy-themed number guessing game where you act as an agent trying to crack a secret encrypted number using intel hints.

## 🎮 How to Play

- A secret number between **1 and 100** is chosen by the computer
- You have **7 attempts** to guess it
- After every wrong guess, you receive **spy-style intel hints**:
  - 🔥 Warmer / 🧊 Colder — compared to your previous guess
  - 📡 Higher or Lower direction
  - 🔎 Whether the number is Even or Odd
  - 🗺️ Which zone (1–25, 26–50, 51–75, 76–100) it's hiding in
- Guess correctly → **Mission Success!**
- Run out of attempts → **Mission Failed**

## ▶️ How to Run

```bash
cd games/Spy-Number-Game
python Spy-Number-Game.py
```

## 🖥️ Sample Output

```

       🕵️  SPY NUMBER GAME  🕵️

Agent, a secret number between 1 and 100
has been encrypted by the enemy.
You have 7 attempts to crack the code.


🎯 Attempt 1/7
Enter your guess: 50

❌ Wrong guess! Decrypting intel...

  🧊 You're getting COLDER, Agent.
  📡 The spy number is HIGHER than your guess.
  🔎 Intel says: the spy number is ODD.
  🗺️  The spy number is hiding in zone 51–75.
```

## 🧠 Concepts Used

- `random` module
- Functions and loops
- Input validation
- Conditional logic
