
import re

st = "hello!@#$%^& ^&*()world"

res = re.search(r"\W+", st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")
