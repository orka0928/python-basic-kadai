array = ["水","金","地","火","木","土","天","海", "冥"]

for i in array:
    print(i)


index = 0

while index < len(array):
    print(array[index])

    if array[index] == 8:  
        break

    index += 1
