seasons_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December"]
season = int(input("Enter the month number - "))

for i in range(len(seasons_list)):
    if season == i + 1:
        if 3 <= season <= 5:
            print(f"This is Spring, month - {seasons_list[i]}")
        elif 6 <= season <= 8:
            print(f"This is Summer, month - {seasons_list[i]}")
        elif 9 <= season <= 11:
            print(f"This is Autumn, month - {seasons_list[i]}")
        else:
            print(f"This is Winter, month - {seasons_list[i]}")


