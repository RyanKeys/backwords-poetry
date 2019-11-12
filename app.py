import random
poem = '''
If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!
'''
sentence_list = []
parsed_poem = poem.split("\n")


def lines_printed_backwords():
    parsed_poem.reverse()
    parsed_poem.pop(0)
    print(parsed_poem)


def lines_printed_random():
    random.shuffle(parsed_poem)
    print(parsed_poem)


lines_printed_backwords()
lines_printed_random()
