rating = [9, 8, 7, 7, 6, 5, 4, 3, 3, 3, 2, 1]
new = int(input('Enter some number'))

if new in rating:
    rating.reverse()
    index = rating.index(new)
    rating.insert(index, new)
    rating.reverse()
else:
    if min(rating) > new:
        rating.extend([new])
    else:
        for i in range(len(rating)):
            if rating[i] < new:
                rating.insert(i, new)
                break
print(rating)

