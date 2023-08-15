import requests

response = requests.get(
    "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-summary.json")
data = response.json()

champions = [i["name"].lower() for i in data]
roles = [i["roles"] for i in data]

role_list = [0, 0, 0, 0, 0, 0]
role_string = ["assassin", "fighter", "mage", "marksman", "support", "tank"]
role_values = [1, 2, 3]


def analyzer():
    while True:
        try:
            champion = input("Analysis champion: ").lower()
            if champion == "q":
                break

            champion_location = champions.index(champion)
            champion_roles = roles[champion_location]

            print(champion_roles)

        except ValueError:
            print("Invalid input.\n"
                  "Enter champion to analyze or 'q' to quit.")

        else:
            break


def finder():
    finder_list = []

    while True:
        try:
            role1 = input("Primary role: ").lower()
            if role1 == "q":
                break

            if role1 not in role_string:
                raise ValueError

            role1v = input("Primary role value: ")
            if role1v == "q":
                break

            role1v = int(role1v)
            if role1v not in role_values:
                raise ValueError

            if role1v == 3:
                counter = 0
                for i in roles:
                    if i == [role1]:
                        champion_found = champions[counter]
                        finder_list.append(champion_found)
                    counter += 1

                print(finder_list)
                break

            role2 = input("Secondary role: ").lower()
            if role2 == "q":
                break

            if role2 not in role_string:
                raise ValueError

            role2v = input("Secondary role value: ")
            if role2v == "q":
                break

            role2v = int(role2v)
            if role2v not in role_values or role1v + role2v != 3:
                raise ValueError

            counter = 0
            for i in roles:
                if len(i) == 2:
                    if role1 in i[role1v-2] and role2 in i[role2v-2]:
                        champion_found = champions[counter]
                        finder_list.append(champion_found)
                counter += 1

            print(finder_list)

        except ValueError:
            print("Invalid input.\n"
                  "Enter 'assassin', 'fighter', 'mage', 'marksman', 'support', or 'tank' for role, '1', '2', or '3' for role value, or 'q' to quit.\n"
                  "Roles cannot be the same, and role values must sum to 3.")

        else:
            break


def selector():
    while True:
        try:
            ban = input("Ban: ").lower()
            while ban != "q":
                ban_location = champions.index(ban)
                del champions[ban_location], roles[ban_location]

                ban = input("Ban: ").lower()

        except ValueError:
            print("Invalid input.\n"
                  "Enter champion to ban or 'q' to quit.")

        else:
            break

    while True:
        try:
            champion = input("Champion: ").lower()
            while champion != "q":
                while champion in ["a", "f", "b"]:
                    if champion == "a":
                        analyzer()

                    elif champion == "f":
                        finder()

                    elif champion == "b":
                        opponent_champion = input("Opponent champion: ").lower()
                        if opponent_champion != "q":
                            oc_location = champions.index(opponent_champion)
                            del champions[oc_location], roles[oc_location]

                    champion = input("Champion: ").lower()

                champion_location = champions.index(champion)
                champion_roles = roles[champion_location]

                for i in champion_roles:
                    role_location = role_string.index(i)
                    if len(champion_roles) == 1:
                        role_list[role_location] += 3

                    else:
                        role_list[role_location] += 2 if champion_roles.index(i) == 0 else 1

                del champions[champion_location], roles[champion_location]

                print(role_list)
                print(role_string)

                champion = input("Champion: ").lower()

        except ValueError:
            print("Invalid input.\n"
                  "Enter champion to select, 'a' to analyze, 'f' to find, 'b' to ban, or 'q' to quit.")

        else:
            break


selector()
