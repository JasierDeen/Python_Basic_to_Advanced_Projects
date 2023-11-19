
# Half pyramid pattern with stars(*)

print("\nHalf pyramid pattern with stars(*)\n")

rows = 10

for i in range(0, rows):
    for j in range(0, i+1):
        print("*", end=" ")
    print()
