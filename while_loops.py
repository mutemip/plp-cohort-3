# syntax:
# while condition:
#     action


colors = ["blue", "white", "black", "grey"]

# print(colors[0])
# index     0       1         2        3

color_i_want = "black"

list_length = len(colors) # 4
index = 0

while index < list_length:
    print(colors[index])

    if colors[index] == color_i_want: # black
        print("Got it!")
        continue
    index += 1