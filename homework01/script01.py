words = []

with open('/usr/share/dict/words','r') as f:
    words = f.read().splitlines()


words.sort(key=len, reverse=True)

for i in range(5):
    print(words[i])



