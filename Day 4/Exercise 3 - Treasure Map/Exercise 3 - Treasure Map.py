row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

separate_numbers = list(position)
map[int(separate_numbers[1]) - 1][int(separate_numbers[0]) - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")