from collections import defaultdict
# Count how many times colors appear and display only the top 3
colors = ["blue","green","red","blue","blue","green","red","yellow"]


colors_counted = defaultdict(int)
for color in colors:
    if color in colors_counted.keys():
        colors_counted[color] += 1
    else:
        colors_counted[color] = 1

top_3 = {}
while len(top_3) < 3:
    top_color = max(colors_counted, key=lambda x: colors_counted[x])
    top_3[top_color] = colors_counted.pop(top_color)

print(top_3)


