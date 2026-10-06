# Game introduction and detective setup
print("Welcome to The Missing Necklace")
print("A valuable necklace has mysteriously disappeared from a mansion during a dinner party.")
print("Three people were present when the necklace went missing, and one of them may be responsible.")
print("You are the detective assigned to investigate the case. Your job is to search the mansion, investigate different locations, interview the suspects, and collect clues.")
print("Use the evidence you discover to determine who is responsible for the missing necklace.")
print("Good luck, Detective.")

detective_name = input("What is your name, Detective? ").title()
print(f"Thank you, Detective {detective_name}. Let's get to work.")

print("You arrive at the mansion, where the necklace was last seen.")
print("The mansion has several rooms that may contain evidence.")
print("Where would you like to investigate?")
print("1. The Living Room")
print("2. The Kitchen")
print("3. The Dining Room")

room_names = ["The Living Room", "The Kitchen", "The Dining Room"]
investigated_rooms = []
evidence = []

continue_investigating = True

# User input for room selection
while continue_investigating:
    room_choice = input("What room number would you like to investigate (1, 2, or 3): ")

    if room_choice == "1":
        if room_names[0] in investigated_rooms:
            print("You have already investigated the Living Room. Please choose another room.")
        else:
            evidence.append("CLUE: A muddy footprint near the doorway.")
            print("The footprint suggests that someone came into the mansion from outside.")
            investigated_rooms.append(room_names[0])

            continue_investigating_choice = input(
                "Would you like to investigate another room? (yes/no): "
            ).lower()

            while continue_investigating_choice not in ["yes", "no"]:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                continue_investigating_choice = input(
                    "Would you like to investigate another room? (yes/no): "
                ).lower()

            if continue_investigating_choice == "no":
                continue_investigating = False

    elif room_choice == "2":
        if room_names[1] in investigated_rooms:
            print("You have already investigated the Kitchen. Please choose another room.")
        else:
            evidence.append("CLUE: A half-eaten sandwich on the counter.")
            print("The sandwich may indicate that someone was in a hurry and left in a rush, possibly after taking the necklace.")
            investigated_rooms.append(room_names[1])

            continue_investigating_choice = input(
                "Would you like to investigate another room? (yes/no): "
            ).lower()

            while continue_investigating_choice not in ["yes", "no"]:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                continue_investigating_choice = input(
                    "Would you like to investigate another room? (yes/no): "
                ).lower()

            if continue_investigating_choice == "no":
                continue_investigating = False

    elif room_choice == "3":
        if room_names[2] in investigated_rooms:
            print("You have already investigated the Dining Room. Please choose another room.")
        else:
            evidence.append("CLUE: The necklace's display case is empty, but there are no signs of forced entry.")
            print("This suggests that the case was opened using the proper key or access rather than being broken into.")
            investigated_rooms.append(room_names[2])

            continue_investigating_choice = input(
                "Would you like to investigate another room? (yes/no): "
            ).lower()

            while continue_investigating_choice not in ["yes", "no"]:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                continue_investigating_choice = input(
                    "Would you like to investigate another room? (yes/no): "
                ).lower()

            if continue_investigating_choice == "no":
                continue_investigating = False

    else:
        print("Invalid choice. Please select a valid room number (1, 2, or 3).")

print("You've finished investigating the rooms that you wanted to search. Now it's time to speak with the people who were present when the necklace disappeared.")


# Suspect information
suspects = {
    "Arthur Blackwood"  : {
        "role": "Butler",
        "statement" : "I spent most of the evening moving between the dining room and the hallway, making sure the guests had everything they needed. I didn't enter the living room, and I certainly never went near the necklace. I do have access to several rooms in the mansion because of my duties, but I had no reason to open the display case."
    },
    "Eleanor Hart" : {
        "role": "Chef",
        "statement" : "I was in the kitchen preparing dinner for most of the evening. I did leave briefly to deliver a dish to the dining room, but then I returned to the kitchen. I had nothing to do with the necklace. I was so busy that I barely had time to eat."
    },
    "Daniel Whitmore" : {
        "role": "Guest",
        "statement" : "I spent most of the evening in the dining room talking with the other guests. I never went near the necklace display case, and I didn't leave the dining room until everyone realized the necklace was missing. I certainly didn't have a reason to enter the other rooms."
    }
}

print("Which suspect would you like to interview?")
print("1. Arthur Blackwood (Butler)")
print("2. Eleanor Hart (Chef)")
print("3. Daniel Whitmore (Guest)")
suspect_choice = input("Enter the number of the suspect you want to interview (1, 2, or 3): ")
while suspect_choice not in ["1", "2", "3"]:
    print("Invalid choice. Please select a valid suspect number (1, 2, or 3).")
    suspect_choice = input("Enter the number of the suspect you want to interview (1, 2, or 3): ")

# Interviewing the chosen suspect
continue_interview = True
while continue_interview:  
    if suspect_choice == "1":
        print("Arthur Blackwood")
        print(f"Role: {suspects['Arthur Blackwood']['role']}")
        print(f"Statement: {suspects['Arthur Blackwood']['statement']}")

        if continue_interview:
            continue_choice = input("Would you like to interview another suspect? (yes/no): ").lower()
            while continue_choice not in ["yes", "no"]:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                continue_choice = input("Would you like to interview another suspect? (yes/no): ").lower()


            if continue_choice == "yes":
                suspect_choice = input("Enter the number of the suspect you want to interview (1, 2, or 3): ")
                while suspect_choice not in ["1", "2", "3"]:
                    print("Invalid choice. Please select a valid suspect number (1, 2, or 3).")
                    suspect_choice = input("Enter the number of the suspect you want to interview (1, 2, or 3): ")
            else:
                continue_interview = False


    elif suspect_choice == "2":
        print("Eleanor Hart")
        print(f"Role: {suspects['Eleanor Hart']['role']}")
        print(f"Statement: {suspects['Eleanor Hart']['statement']}")

        if continue_interview:
            continue_choice = input("Would you like to interview another suspect? (yes/no): ").lower()
            while continue_choice not in ["yes", "no"]:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                continue_choice = input("Would you like to interview another suspect? (yes/no): ").lower()


            if continue_choice == "yes":
                suspect_choice = input("Enter the number of the suspect you want to interview (1, 2, or 3): ")
                while suspect_choice not in ["1", "2", "3"]:
                    print("Invalid choice. Please select a valid suspect number (1, 2, or 3).")
                    suspect_choice = input("Enter the number of the suspect you want to interview (1, 2, or 3): ")
            else:
                continue_interview = False


    elif suspect_choice == "3":
        print("Daniel Whitmore")
        print(f"Role: {suspects['Daniel Whitmore']['role']}")
        print(f"Statement: {suspects['Daniel Whitmore']['statement']}")

        if continue_interview:
            continue_choice = input("Would you like to interview another suspect? (yes/no): ").lower()
            while continue_choice not in ["yes", "no"]:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                continue_choice = input("Would you like to interview another suspect? (yes/no): ").lower()


            if continue_choice == "yes":
                suspect_choice = input("Enter the number of the suspect you want to interview (1, 2, or 3): ")
                while suspect_choice not in ["1", "2", "3"]:
                    print("Invalid choice. Please select a valid suspect number (1, 2, or 3).")
                    suspect_choice = input("Enter the number of the suspect you want to interview (1, 2, or 3): ")
            else:
                continue_interview = False


# Evidence comparison and deduction
print("The interviews are complete. Now it's time to review the evidence you collected.")
print("You have the following information:")
print("The muddy footprint near the living room doorway suggests that someone may have entered the mansion from outside.")
print("The half-eaten sandwich in the kitchen suggests that someone may have left the kitchen in a hurry.")
print("Most importantly, the necklace's display case showed no signs of forced entry. This suggests that whoever took the necklace may have had access to the proper key or was otherwise able to open the case without breaking it.")  
print("You now have enough information to compare the suspects' statements with the evidence and determine who may be responsible.")

print("1. Arthur Blackwood (Butler)")
print("2. Eleanor Hart (Chef)")
print("3. Daniel Whitmore (Guest)")
suspect_accused = input("Who do you believe is responsible for the missing necklace? (Enter the number of the suspect: 1, 2, or 3): ")
while suspect_accused not in ["1", "2", "3"]:
    print("Invalid choice. Please select a valid suspect number (1, 2, or 3).")
    suspect_accused = input("Who do you believe is responsible for the missing necklace? (Enter the number of the suspect: 1, 2, or 3): ")


# Final accusation and conclusion
if suspect_accused == "1":
    print("You have identified the culprit! Arthur Blackwood was responsible for stealing the necklace. His access to several rooms and the ability to open the display case without forced entry made him the most likely suspect.")
else:
    print("Your accusation is incorrect. You have accused the wrong person. The evidence points to Arthur Blackwood, who had access to several rooms and could open the display case without forcing it.")