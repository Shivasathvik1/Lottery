# 🎰 Lottery Game Simulator

A Python terminal-based lottery simulator featuring 4 different lottery-style games. Players can either let the computer pick numbers randomly or choose their own numbers and see if they win!

---

## 📋 Requirements

- Python 3.x
- No external libraries needed (uses built-in `random` module only)

---

## ▶️ How to Run

```bash
python lottery_commented.py
```

---

## 🎮 Games

### 1. Big Ball
Pick 5 numbers from 1 to 59 and try to match the winning draw.

| Matches | Prize |
|---------|-------|
| 0 – 1   | No win |
| 2       | $50 |
| 3       | $500 |
| 4       | $10,000 |
| 5       | 🏆 BIG BALL Jackpot |

---

### 2. Jackpot Million
Same as Big Ball but with an extra prize tier — even 1 match wins!

| Matches | Prize |
|---------|-------|
| 0       | No win |
| 1       | $10 |
| 2       | $50 |
| 3       | $500 |
| 4       | $10,000 |
| 5       | 🏆 Jackpot Million Jackpot |

---

### 3. Choose 3
Pick a 3-digit number from `000` to `999` and try to match the winning draw. Three play styles available:

| Style    | How to Win | Prize |
|----------|------------|-------|
| Straight | Exact digit order match | $250 |
| Box      | Any order match | $40 |
| Wheel    | Any order match (higher payout) | $240 |

---

### 4. Choose 4
Pick a 4-digit number from `0000` to `9999` and try to match the winning draw. Three play styles available:

| Style    | How to Win | Prize |
|----------|------------|-------|
| Straight | Exact digit order match | $2,500 |
| Box      | Any order match | $200 |
| Wheel    | Any order match (higher payout) | $2,400 |

---

## 🕹️ Play Modes

Every game offers two ways to play:

- **Random Pick** — The computer automatically generates your numbers
- **Choose Yourself** — You manually enter your own numbers

---

## 📁 Files

| File | Description |
|------|-------------|
| `lottery_v1.py` | Main game file with full inline comments |
| `README.md` | This file |

---

## 💡 Notes

- For **Choose 3** and **Choose 4**, numbers are zero-padded (e.g. `007`, `0042`) so leading zeros are preserved correctly.
- In **Box** and **Wheel** modes, the digits of your number are sorted and compared to the sorted digits of the winning number — so `123`, `321`, and `213` are all treated as the same entry.
- **Wheel** and **Box** use the same matching logic but Wheel offers a significantly higher payout.
