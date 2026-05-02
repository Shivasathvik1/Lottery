import random

# ─────────────────────────────────────────────
# MAIN MENU — Display available games
# ─────────────────────────────────────────────
print("""Choose which Game You like to play
      1.Big Ball
      2.Jackpot Million
      3.choose 3
      4.choose 4""")

user_input = int(input("choose One Option :"))

# ═══════════════════════════════════════════════════════════════
# GAME 1: BIG BALL
# Player picks 5 numbers from 1 – 60 and tries to match the draw
# Prize tiers: 2 match=$50 | 3=$500 | 4=$10,000 | 5=Jackpot
# ═══════════════════════════════════════════════════════════════
if user_input == 1:
    # Generate and sort 5 winning numbers from 1 to 60
    bb_W_numbers = random.sample(range(1, 60), 5)
    bb_W_numbers.sort()

    print("""Welcome to the Big ball Choose how do you like to play
          1.Random pick
          2.Choose by your self""")
    bb_choose = int(input("choose One Option :"))

    # --- Option 1: Computer randomly picks 5 numbers for the player ---
    if bb_choose == 1:
        bb_random = random.sample(range(1, 60), 5)
        print(bb_W_numbers)   # Show winning numbers
        print(bb_random)       # Show player's random numbers

        # Count how many numbers match between player and winning draw
        m = len(set(bb_random) & set(bb_W_numbers))
        print(f"You have only {m} matched numbers out of 5")

        # Determine prize based on number of matches
        if m == 0 or m == 1:
            print("Sorry Not A winner 😩! Better Luck Next time")
        elif m == 2:
            print("You Won! $50 🥳🥳")
        elif m == 3:
            print("You Won! $500 🥳🥳")
        elif m == 4:
            print("You Won! $10,000 🥳🥳")
        else:
            print("""Congrats 
                  You Won the "BIG BALL" Jackpot""")

    # --- Option 2: Player manually enters their 5 numbers ---
    elif bb_choose == 2:
        a = []
        # Read space-separated numbers from user input and convert to integers
        a.extend([int(x) for x in input("Choose 5 numbers from 1 to 60: ").split()])

        # Count matches between player's numbers and winning draw
        m = len(set(a) & set(bb_W_numbers))
        print(bb_W_numbers)   # Reveal the winning numbers
        print(f"You have only {m} matched numbers out of 5")

        # Determine prize based on number of matches
        if m == 0 or m == 1:
            print("Sorry Not A winner 😩! Better Luck Next time")
        elif m == 2:
            print("You Won! $50 🥳🥳")
        elif m == 3:
            print("You Won! $500 🥳🥳")
        elif m == 4:
            print("You Won! $10,000 🥳🥳")
        else:
            print("""Congrats 
                  You Won the "BIG BALL" Jackpot""")
    else:
        print("Invalid Input")

# ═══════════════════════════════════════════════════════════════
# GAME 2: JACKPOT MILLION
# Same format as Big Ball but with an extra prize tier for 1 match
# Prize tiers: 1 match=$10 | 2=$50 | 3=$500 | 4=$10,000 | 5=Jackpot
# ═══════════════════════════════════════════════════════════════
elif user_input == 2:
    # Generate and sort 5 winning numbers from 1 to 60
    jm_W_numbers = random.sample(range(1, 60), 5)
    jm_W_numbers.sort()

    print("""Welcome to the Jackpot Million Choose how do you like to play
              1.Random pick
              2.Choose by your self""")
    jm_choose = int(input("choose One Option :"))

    # --- Option 1: Computer randomly picks 5 numbers for the player ---
    if jm_choose == 1:
        jm_random = random.sample(range(1, 60), 5)
        print(jm_W_numbers)   # Show winning numbers
        print(jm_random)       # Show player's random numbers

        # Count how many numbers match
        m = len(set(jm_random) & set(jm_W_numbers))
        print(f"You have only {m} matched numbers out of 5")

        # Determine prize — note: even 1 match wins $10 here
        if m == 0:
            print("Sorry Not A winner 😩! Better Luck Next time")
        elif m == 1:
            print("You Won! $10 🥳🥳")
        elif m == 2:
            print("You Won! $50 🥳🥳")
        elif m == 3:
            print("You Won! $500 🥳🥳")
        elif m == 4:
            print("You Won! $10,000 🥳🥳")
        else:
            print("""Congrats 
                      You Won the "Jackpot Million" Jackpot""")

    # --- Option 2: Player manually enters their 5 numbers ---
    elif jm_choose == 2:
        jm_W_numbers.sort()   # Already sorted, kept for safety
        a = []
        # Read space-separated numbers from user input and convert to integers
        a.extend([int(x) for x in input("Choose 5 numbers from 1 to 60: ").split()])

        # Count matches between player's numbers and winning draw
        m = len(set(a) & set(jm_W_numbers))
        print(jm_W_numbers)   # Reveal the winning numbers
        print(f"You have only {m} matched numbers out of 5")

        # Determine prize
        if m == 0:
            print("Sorry Not A winner 😩! Better Luck Next time")
        elif m == 1:
            print("You Won! $10 🥳🥳")
        elif m == 2:
            print("You Won! $50 🥳🥳")
        elif m == 3:
            print("You Won! $500 🥳🥳")
        elif m == 4:
            print("You Won! $10,000 🥳🥳")
        else:
            print("""Congrats 
                      You Won the "Jackpot Million" Jackpot""")
    else:
        print("Invalid Input")

# ═══════════════════════════════════════════════════════════════
# GAME 3: CHOOSE 3
# Player picks a 3-digit number (000–999) and tries to match the draw
# Three play styles:
#   Straight — exact order match → $250
#   Box      — any order match   → $40
#   Wheel    — any order match   → $240 (higher payout variant)
# ═══════════════════════════════════════════════════════════════
elif user_input == 3:
    # Generate a random 3-digit winning number (000–999)
    c3_w_number = random.randint(000, 999)

    print("""Welcome to the "Choose 3" Choose how do you like to play
    1.Straight
    2.Box
    3.Wheel
    """)
    c3_choose = int(input("Choose 1 Option :"))

    # ── STRAIGHT: digits must match in exact order ──
    if c3_choose == 1:
        print("""Choose how How do you like to play
        1.Random pick
        2.Choose by your self""")
        user_choose = int(input("choose 1 Option :"))

        # --- Random pick ---
        if user_choose == 1:
            c3_str_ran = random.randint(000, 999)

            # Compare as zero-padded 3-digit strings (e.g. 007 == 007)
            if f'{c3_str_ran:03d}' == f"{c3_w_number:03d}":
                print(f'{c3_w_number:03d}')
                print(f'{c3_str_ran:03d}')
                print("You Won! $ 250 🥳🥳")
            else:
                print(f'{c3_w_number:03d}')
                print(f'{c3_str_ran:03d}')
                print("Sorry Not a Winner! 😩 ")

        # --- Player picks their own number ---
        elif user_choose == 2:
            c3_str_user = int(input("choose 1 3-digit Number from 000:999 : "))

            # Compare as zero-padded 3-digit strings
            if f'{c3_str_user:03d}' == f"{c3_w_number:03d}":
                print(f'{c3_w_number:03d}')
                print(f'{c3_str_user:03d}')
                print("You Won! $ 250 🥳🥳")
            else:
                print(f'{c3_w_number:03d}')
                print(f'{c3_str_user:03d}')
                print("Sorry Not a Winner! 😩 ")
        else:
            print("Invalid Input")

    # ── BOX: digits can match in any order → $40 ──
    elif c3_choose == 2:
        print("""Choose how How do you like to play
               1.Random pick
               2.Choose by your self""")
        user_choose = int(input("choose 1 Option :"))

        # --- Random pick ---
        if user_choose == 1:
            c3_box_ran = random.randint(000, 999)
            print(f'{c3_w_number:03d}')
            print(f'{c3_box_ran:03d}')

            # Sort both numbers' digits and compare — order doesn't matter
            b = [int(d) for d in str(f'{c3_box_ran:03d}')]
            b.sort()
            c = [int(d) for d in str(f'{c3_w_number:03d}')]
            c.sort()
            if b == c:
                print("Congrats You Won! $40🥳🥳")
            else:
                print("Sorry Not a Winner")

        # --- Player picks their own number ---
        elif user_choose == 2:
            c3_box_user = int(input("choose 1 3-digit Number from 000:999 : "))
            print(f'{c3_w_number:03d}')
            print(f'{c3_box_user:03d}')

            # Sort both numbers' digits and compare
            b = [int(d) for d in str(f'{c3_box_user:03d}')]
            b.sort()
            c = [int(d) for d in str(f'{c3_w_number:03d}')]
            c.sort()
            if b == c:
                print("Congrats You Won! $40🥳🥳")
            else:
                print("Sorry Not a Winner")
        else:
            print("Invalid Input")

    # ── WHEEL: digits can match in any order → $240 (higher payout) ──
    elif c3_choose == 3:
        print("""Choose how How do you like to play
        1.Random pick
        2.Choose by your self""")
        user_choose = int(input("choose 1 Option :"))

        # --- Random pick ---
        if user_choose == 1:
            c3_box_ran = random.randint(000, 999)
            print(f'{c3_w_number:03d}')
            print(f'{c3_box_ran:03d}')

            # Sort both numbers' digits and compare — same logic as Box but higher prize
            b = [int(d) for d in str(f'{c3_box_ran:03d}')]
            b.sort()
            c = [int(d) for d in str(f'{c3_w_number:03d}')]
            c.sort()
            if b == c:
                print("Congrats You Won! $240 🥳🥳")
            else:
                print("Sorry Not a Winner")

        # --- Player picks their own number ---
        elif user_choose == 2:
            c3_box_user = int(input("choose 1 3-digit Number from 000:999 : "))
            print(f'{c3_w_number:03d}')
            print(f'{c3_box_user:03d}')

            # Sort both numbers' digits and compare
            b = [int(d) for d in str(f'{c3_box_user:03d}')]
            b.sort()
            c = [int(d) for d in str(f'{c3_w_number:03d}')]
            c.sort()
            if b == c:
                print("Congrats You Won! $240 🥳🥳")
            else:
                print("Sorry Not a Winner")
        else:
            print("Invalid Input")

# ═══════════════════════════════════════════════════════════════
# GAME 4: CHOOSE 4
# Player picks a 4-digit number (0000–9999) and tries to match the draw
# Three play styles:
#   Straight — exact order match → $2500
#   Box      — any order match   → $200
#   Wheel    — any order match   → $2400 (higher payout variant)
# ═══════════════════════════════════════════════════════════════
elif user_input == 4:
    # Generate a random 4-digit winning number (0000–9999)
    c4_w_number = random.randint(0000, 9999)

    print("""Welcome to the "Choose 4" Choose how do you like to play
        1.Straight
        2.Box
        3.Wheel
        """)
    c4_choose = int(input("Choose 1 Option :"))

    # ── STRAIGHT: digits must match in exact order → $2500 ──
    if c4_choose == 1:
        print("""Choose how How do you like to play
            1.Random pick
            2.Choose by your self""")
        user_choose = int(input("choose 1 Option :"))

        # --- Random pick ---
        if user_choose == 1:
            c4_str_ran = random.randint(0000, 9999)

            # Compare as zero-padded 4-digit strings
            if f'{c4_str_ran:04d}' == f"{c4_w_number:04d}":
                print(f'{c4_w_number:04d}')
                print(f'{c4_str_ran:04d}')
                print("You Won! $ 2500 🥳🥳")
            else:
                print(f'{c4_w_number:04d}')
                print(f'{c4_str_ran:04d}')
                print("Sorry Not a Winner! 😩 ")

        # --- Player picks their own number ---
        elif user_choose == 2:
            c4_str_user = int(input("choose 1 3-digit Number from 0000:9999 : "))

            # Compare as zero-padded 4-digit strings
            if f'{c4_str_user:04d}' == f"{c4_w_number:04d}":
                print(f'{c4_w_number:04d}')
                print(f'{c4_str_user:04d}')
                print("You Won! $ 2500 🥳🥳")
            else:
                print(f'{c4_w_number:04d}')
                print(f'{c4_str_user:04d}')
                print("Sorry Not a Winner! 😩 ")
        else:
            print("Invalid Input")

    # ── BOX: digits can match in any order → $200 ──
    elif c4_choose == 2:
        print("""Choose how How do you like to play
                   1.Random pick
                   2.Choose by your self""")
        user_choose = int(input("choose 1 Option :"))

        # --- Random pick ---
        if user_choose == 1:
            c4_box_ran = random.randint(0000, 9999)
            print(f'{c4_w_number:04d}')
            print(f'{c4_box_ran:04d}')

            # Sort both numbers' digits and compare — order doesn't matter
            b = [int(d) for d in str(f'{c4_box_ran:04d}')]
            b.sort()
            c = [int(d) for d in str(f'{c4_w_number:04d}')]
            c.sort()
            if b == c:
                print("Congrats You Won! $200 🥳🥳")
            else:
                print("Sorry Not a Winner")

        # --- Player picks their own number ---
        elif user_choose == 2:
            c4_box_user = int(input("choose 1 3-digit Number from 0000:9999 : "))
            print(f'{c4_w_number:04d}')
            print(f'{c4_box_user:04d}')

            # Sort both numbers' digits and compare
            b = [int(d) for d in str(f'{c4_box_user:04d}')]
            b.sort()
            c = [int(d) for d in str(f'{c4_w_number:04d}')]
            c.sort()
            if b == c:
                print("Congrats You Won! $200 🥳🥳")
            else:
                print("Sorry Not a Winner")
        else:
            print("Invalid Input")

    # ── WHEEL: digits can match in any order → $2400 (higher payout) ──
    elif c4_choose == 3:
        print("""Choose how How do you like to play
            1.Random pick
            2.Choose by your self""")
        user_choose = int(input("choose 1 Option :"))

        # --- Random pick ---
        if user_choose == 1:
            c4_wheel_ran = random.randint(0000, 9999)
            print(f'{c4_w_number:04d}')
            print(f'{c4_wheel_ran:04d}')

            # Sort both numbers' digits and compare — same logic as Box but higher prize
            b = [int(d) for d in str(f'{c4_wheel_ran:04d}')]
            b.sort()
            c = [int(d) for d in str(f'{c4_w_number:04d}')]
            c.sort()
            if b == c:
                print("Congrats You Won! $2400 🥳🥳")
            else:
                print("Sorry Not a Winner")

        # --- Player picks their own number ---
        elif user_choose == 2:
            c4_wheel_user = int(input("choose 1 3-digit Number from 0000:9999 : "))
            print(f'{c4_w_number:04d}')
            print(f'{c4_wheel_user:04d}')

            # Sort both numbers' digits and compare
            b = [int(d) for d in str(f'{c4_wheel_user:04d}')]
            b.sort()
            c = [int(d) for d in str(f'{c4_w_number:04d}')]
            c.sort()
            if b == c:
                print("Congrats You Won! $2400 🥳🥳")
            else:
                print("Sorry Not a Winner")
        else:
            print("Invalid Input")

else:
    print("invalid input")