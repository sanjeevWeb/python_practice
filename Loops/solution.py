
number = 5

for num in range(1, 11):
    if num == 5:
        continue
    print(number," * ", num,"=" ,number * num),


input_str = "teeter"

for char in input_str:
    repeting = input_str.count(char) == 1
    if repeting:
        print(char)
        break

# 07_solution

while True:
    num = int(input("Ente value between 1 and 10: "))
    if 1 <= num <= 10:
        print("Thanks")
        break
    else:
        print("Invalid entry")

# 10 solution

import time

max_retries = 5
attemp = 0
wait_time = 1

while attemp < max_retries:
    print("Attempt ", attemp + 1, "- wait time ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attemp += 1
