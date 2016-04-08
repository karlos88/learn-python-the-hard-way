from sys import argv

# Added third arg
script, user_name, author = argv

# Changing the prompt
# prompt = '> '
prompt = 'oXo: '

print("Hi %s, I'm the %s script made by author %s." % (user_name, script, author))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(""" Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice. """ % (likes, lives, computer))