# Game data
room_names = [
    "The Living Room",
    "The Kitchen",
    "The Dining Room"
]

investigated_rooms = []
evidence = []

suspects = {
    "Arthur Blackwood": {
        "role": "Butler",
        "statement": (
            "I spent most of the evening moving between the dining room and "
            "the hallway, making sure the guests had everything they needed. "
            "I didn't enter the living room, and I certainly never went near "
            "the necklace. I do have access to several rooms in the mansion, "
            "but I had no reason to open the display case."
        )
    },

    "Eleanor Hart": {
        "role": "Chef",
        "statement": (
            "I was in the kitchen preparing dinner for most of the evening. "
            "I did leave briefly to deliver a dish to the dining room, but "
            "then I returned to the kitchen. I had nothing to do with the "
            "necklace. I was so busy that I barely had time to eat."
        )
    },

    "Daniel Whitmore": {
        "role": "Guest",
        "statement": (
            "I spent most of the evening in the dining room talking with "
            "the other guests. I never went near the necklace display case, "
            "and I didn't leave the dining room until everyone realized the "
            "necklace was missing. I certainly didn't have a reason to enter "
            "the other rooms."
        )
    }
}

# Functions

def ask_to_continue(prompt):
    answer = input(prompt).lower()

    while answer not in ["yes", "no"]:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        answer = input(prompt).lower()

    return answer == "yes"


def choose_suspect():
    suspect_choice = input(
        "Enter the number of the suspect (1, 2, or 3): "
    )

    while suspect_choice not in ["1", "2", "3"]:
        print("Invalid choice. Please select 1, 2, or 3.")
        suspect_choice = input(
            "Enter the number of the suspect (1, 2, or 3): "
        )

    return suspect_choice


def show_suspect(suspect_name):
    print(suspect_name)
    print(f"Role: {suspects[suspect_name]['role']}")
    print(f"Statement: {suspects[suspect_name]['statement']}")


def get_suspect_name(suspect_choice):
    if suspect_choice == "1":
        return "Arthur Blackwood"
    elif suspect_choice == "2":
        return "Eleanor Hart"
    else:
        return "Daniel Whitmore"


# Game introduction
print("Welcome to The Missing Necklace")
print(
    "A valuable necklace has mysteriously disappeared from a mansion "
    "during a dinner party."
)
print(
    "Three people were present when the necklace went missing, "
    "and one of them may be responsible."
)
print(
    "You are the detective assigned to investigate the case. "
    "Your job is to search the mansion, investigate different locations, "
    "interview the suspects, and collect clues."
)
print(
    "Use the evidence you discover to determine who is responsible "
    "for the missing necklace."
)
print("Good luck, Detective.")


# Detective setup

detective_name = input("What is your name, Detective? ").title()

print(
    f"Thank you, Detective {detective_name}. Let's get to work."
)

print("You arrive at the mansion, where the necklace was last seen.")
print("The mansion has several rooms that may contain evidence.")



# Room investigation
print("Where would you like to investigate?")
print("1. The Living Room")
print("2. The Kitchen")
print("3. The Dining Room")

continue_investigating = True

while continue_investigating:

    room_choice = input(
        "What room number would you like to investigate (1, 2, or 3): "
    )

    if room_choice == "1":

        if room_names[0] in investigated_rooms:
            print(
                "You have already investigated the Living Room. "
                "Please choose another room."
            )
        else:
            evidence.append(
                "CLUE: A muddy footprint was found near the Living Room doorway."
            )

            print(
                "The footprint suggests that someone came into the mansion "
                "from outside."
            )

            investigated_rooms.append(room_names[0])

    elif room_choice == "2":

        if room_names[1] in investigated_rooms:
            print(
                "You have already investigated the Kitchen. "
                "Please choose another room."
            )
        else:
            evidence.append(
                "CLUE: A half-eaten sandwich was found on the kitchen counter."
            )

            print(
                "The sandwich suggests that someone may have been interrupted "
                "while eating."
            )

            investigated_rooms.append(room_names[1])

    elif room_choice == "3":

        if room_names[2] in investigated_rooms:
            print(
                "You have already investigated the Dining Room. "
                "Please choose another room."
            )
        else:
            evidence.append(
                "CLUE: The necklace's display case was opened without "
                "any signs of forced entry."
            )

            print(
                "The case appears to have been opened using the proper key "
                "or authorized access."
            )

            investigated_rooms.append(room_names[2])

    else:
        print(
            "Invalid choice. Please select a valid room number (1, 2, or 3)."
        )
        continue

    # Check whether every room has been investigated.
    if len(investigated_rooms) == len(room_names):
        print("You have investigated every room in the mansion.")
        continue_investigating = False

    # Only ask whether to continue if there are rooms left.
    elif room_choice in ["1", "2", "3"] and room_choice:
        if room_choice == "1" and room_names[0] in investigated_rooms:
            if room_names[1] not in investigated_rooms or room_names[2] not in investigated_rooms:
                continue_investigating = ask_to_continue(
                    "Would you like to investigate another room? (yes/no): "
                )

        elif room_choice == "2" and room_names[1] in investigated_rooms:
            if room_names[0] not in investigated_rooms or room_names[2] not in investigated_rooms:
                continue_investigating = ask_to_continue(
                    "Would you like to investigate another room? (yes/no): "
                )

        elif room_choice == "3" and room_names[2] in investigated_rooms:
            if room_names[0] not in investigated_rooms or room_names[1] not in investigated_rooms:
                continue_investigating = ask_to_continue(
                    "Would you like to investigate another room? (yes/no): "
                )


print(
    "You've finished investigating the rooms that you wanted to search. "
    "Now it's time to speak with the people who were present when "
    "the necklace disappeared."
)

# Interview suspects
print("Which suspect would you like to interview?")
print("1. Arthur Blackwood (Butler)")
print("2. Eleanor Hart (Chef)")
print("3. Daniel Whitmore (Guest)")

suspect_choice = choose_suspect()

continue_interview = True

while continue_interview:

    suspect_name = get_suspect_name(suspect_choice)

    show_suspect(suspect_name)

    continue_interview = ask_to_continue(
        "Would you like to interview another suspect? (yes/no): "
    )

    if continue_interview:
        suspect_choice = choose_suspect()


# Evidence comparison
print(
    "The interviews are complete. Now it's time to review "
    "the evidence you collected."
)

print("You have the following information:")

for clue in evidence:
    print(clue)

print(
    "You now have enough information to compare the suspects' "
    "statements with the evidence and determine who may be responsible."
)


# Final accusation
print("Who do you believe is responsible?")
print("1. Arthur Blackwood (Butler)")
print("2. Eleanor Hart (Chef)")
print("3. Daniel Whitmore (Guest)")

suspect_accused = choose_suspect()


# Final conclusion

if suspect_accused == "1":
    print(
        "You have identified the culprit!"
    )

    print(
        "Arthur Blackwood was responsible for stealing the necklace. "
        "The display case showed no signs of forced entry, meaning the "
        "necklace was likely taken by someone with authorized access. "
        "Arthur admitted that he had access to several rooms in the mansion "
        "because of his duties, making him the most likely suspect."
    )

else:
    print(
        "Your accusation is incorrect."
    )

    print(
        "The evidence points to Arthur Blackwood. "
        "The necklace display case was opened without forced entry, "
        "and Arthur admitted that he had access to several rooms in "
        "the mansion because of his duties."
    )


# Goodbye

print(
    "Thank you for playing The Missing Necklace. "
    "Your detective skills have been put to the test, "
    "and we hope you enjoyed the investigation. "
    "Until next time, Detective!"
)