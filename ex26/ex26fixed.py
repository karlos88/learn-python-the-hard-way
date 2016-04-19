from ex25 import ex25

# Removed function definitions; no need to have them here if we import ex25
# Moved "secret_formula" function definition to beginning of file for better readibility
# Removed unnecessary blank lines where possible


def secret_formula(started):
    # Renamed function local variables so that they do not shadow variables of the same names
    # from main part of code
    int_jelly_beans = started * 500
    int_jars = int_jelly_beans / 1000
    int_crates = int_jars / 100
    return int_jelly_beans, int_jars, int_crates

print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

# replaced with shorthand assignment
start_point /= 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


sentence = "All good things come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

ex25.print_first_word(words)
ex25.print_last_word(words)
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
