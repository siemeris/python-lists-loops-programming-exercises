par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
total = 0
#your code go here:
minus = par.lower()
for letter in minus:
    if letter == " ":
        continue
    elif letter in counts:
        counts[letter] +=1
    else:
        counts[letter] = 1

print(counts)

