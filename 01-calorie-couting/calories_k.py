import sys

def calories_max_k(elfes, k=3):
    max_elfes = [0] * k

    def insert_at(elf, i):
        if i >= k:
            return
        current = max_elfes[i]
        if elf > current:
            max_elfes[i] = elf
            insert_at(current, i+1)
        else:
            insert_at(elf, i+1)

    for elf in elfes:
        calories = sum(elf)
        insert_at(calories, 0)
    return sum(max_elfes)


data = sys.stdin.read()
elfes = [list(map(int, x.split())) for x in data.split("\n\n")]
max_calories = calories_max_k(elfes)
print(max_calories)
