# Same as in ex06 - assigning strings to variables, also using formatting
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?  ->> Multiplied this char by 10 times and we got a string o 10 dots

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens - doesn't matter in Python3
# but we can use "end" argument not to break line, just as we would have used comma in Python2.
# Removing comma in Python2 causes line to break
print(end1 + end2 + end3 + end4 + end5 + end6, end = " ")
print(end7 + end8 + end9 + end10 + end11 + end12)