import random
import time

s = list("[                  ]")

for i in range(1, 19):
    s[i] = "="
    string = "".join(s)
    print(string)
    time.sleep(random.randint(1, 10))

print("\nJamie is a cunt, fuck you Jamie")
