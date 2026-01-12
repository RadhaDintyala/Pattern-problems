stg = "Hello World"
temp = ""
rev = ""

for i in stg:
    if i != " ":           # when it's not a space
        temp = i + temp    # reverse the current word
    else:                  # when space is found
        rev = rev + temp +" "# add reversed word + space
        temp = ""               # reset for next word

rev = rev + temp  # add the last reversed word
print(rev)
