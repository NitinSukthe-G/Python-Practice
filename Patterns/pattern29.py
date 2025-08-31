# *                       *
#   *                   *
#     *               *
#       *           *
#         *       *
#           *   *
#             *

rows = 7
cols = 13 

for i in range(rows):
    for j in range(cols):
        if j == i:
            print("*", end=" ")
        elif j == cols - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
