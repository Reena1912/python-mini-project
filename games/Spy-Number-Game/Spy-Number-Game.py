import random


print("🕵️  SPY NUMBER GAME  🕵️")
print("A secret number between 1–100 has been encrypted.")
print("You have 7 attempts to crack the code.\n")



play_again = True

while play_again:

    # Setup new mission
    secret_number = random.randint(1, 100)
    max_attempts = 7
    previous_guess = None
    cracked = False

    print("━" * 45)
    print("🚨 NEW MISSION STARTED")
    print("━" * 45 + "\n")

    # Game loop
    for attempt in range(1, max_attempts + 1):

        print(f"🎯 Attempt {attempt}/{max_attempts}")

        # Validate user input
        valid_input = False
        while not valid_input:
            try:
                guess = int(input("➡️  Enter your guess (1–100): "))
                if 1 <= guess <= 100:
                    valid_input = True
                else:
                    print("⚠️  Number must be between 1 and 100!\n")
            except ValueError:
                print("⚠️  Please enter a valid number!\n")

        # Check if guess is correct
        if guess == secret_number:
            print("\n🎉 YOU CRACKED THE CODE, AGENT!")
            print(f"✅ The spy number was: {secret_number}")
            print(f"⚡ Solved in {attempt} attempt(s). Mission Success!\n")
            cracked = True
            break

        # Wrong guess — show intel hints
        print("\n❌ Wrong guess! Decrypting intel...\n")

        # Warm/cold hint compared to previous guess
        if previous_guess is not None:
            prev_distance = abs(secret_number - previous_guess)
            curr_distance = abs(secret_number - guess)
            if curr_distance < prev_distance:
                print("  🔥 You're getting WARMER, Agent.")
            elif curr_distance > prev_distance:
                print("  🧊 You're getting COLDER, Agent.")
            else:
                print("  😐 Same distance as your last guess.")

        # High or low hint
        if guess < secret_number:
            print("  📡 The spy number is HIGHER than your guess.")
        else:
            print("  📡 The spy number is LOWER than your guess.")

        # Even or odd hint
        if secret_number % 2 == 0:
            print("  🔎 Intel says: the spy number is EVEN.")
        else:
            print("  🔎 Intel says: the spy number is ODD.")

        # Zone hint
        if secret_number <= 25:
            print("  🗺️  The spy number is hiding in zone 1–25.")
        elif secret_number <= 50:
            print("  🗺️  The spy number is hiding in zone 26–50.")
        elif secret_number <= 75:
            print("  🗺️  The spy number is hiding in zone 51–75.")
        else:
            print("  🗺️  The spy number is hiding in zone 76–100.")

        print()

        previous_guess = guess

    # Mission failed message
    if not cracked:
        print("❌ MISSION FAILED, AGENT.")
        print(f"🔓 The spy number was: {secret_number}")
        print("💪 Train harder and try again!\n")

    # Ask to play again
    again = input("🔄 Start a new mission? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        play_again = False


# Goodbye message
print("\n👋 Thanks for playing Spy Number Game! Stay sharp, Agent!\n")
