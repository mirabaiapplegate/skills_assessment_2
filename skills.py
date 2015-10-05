# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    #empty dictionary
    word_count = {}

    # for each item in list of words
    for item in input_string.split():
        # if the item is in the dictionary, increase its' count
        if item in word_count:
            word_count[item] += 1
        # else add the item to the dictionary and set count to 1
        else:
            word_count[item] = 1

    return word_count


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    # empty list
    common_items = []

    # for each item in list1
    for item in list1:
        # for each item in list2
        for item2 in list2:
            # if the item is the same as item2 add the item to the list
            if item == item2:
                common_items.append(item)

    return common_items


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    # empty list
    common_items = []

    # for each item in list1
    for item in list1:
        # for each item in list2
        for item2 in list2:
            # if the item is equal to item2 add it to the list
            if item == item2:
                common_items.append(item)
    # return a set (to eliminate duplicates)
    return set(common_items)


def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    ####This one was really difficult for me.
    # empty list
    sum_zero_pairs = []
    # eliminate duplicates from input_list
    set_input_list = set(input_list)

    #for each number in the list
    for num in set_input_list:
        # empty list for pairs
        pairs = []

        # if the number is less than or equal to 0 and it's positive equivalent
        # is in the list, append the positive and negative to the pairs list.
        if num <= 0 and abs(num) in set_input_list:
            pairs.append(num)
            pairs.append(abs(num))
        # prevent empty lists from being added to the final list
        if pairs != []:
            sum_zero_pairs.append(pairs)

    return sum_zero_pairs


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """
    # empty list
    unique_words = []

    # loop over each word in words
    for item in words:
        # if the word isn't in our list of unique words, add it.
        if item not in unique_words:
            unique_words.append(item)

    return unique_words


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """
    # empty string
    encoded_string = ''

    # for each character in the string check to see if letter should
    # be encoded.
    for char in phrase:
        if char == 'e':
            char = 'p'
        elif char == 'a':
            char = 'd'
        elif char == 't':
            char = 'o'
        elif char == 'i':
            char = 'u'
        encoded_string += char

    return encoded_string



def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    # empty dictionary
    word_dict = {}
    # empty list
    ascending_words = []

    # loop to get index positions
    for i in range(len(words)):
        # count the number of characters in each word
        char_count = len(words[i])
        # set a current word
        current_word = words[i]

        # if the character count is in dictionary add the word associated
        if char_count in word_dict:
            word_dict[char_count].append(current_word)
        # else add the character count and the word associated
        else:
            word_dict[char_count] = [current_word]
    # loop over the character counts in the dictionary and create tuples
    # of the character count and the list of words associated to each count
    for char_count in word_dict:
        word_t = (char_count, word_dict[char_count])
        ascending_words.append(word_t)

    return ascending_words


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    # empty list
    pirate_talk = []
    # pirate translator dictionary
    pirate_transalation = {'sir':'matey','hotel':'fleabag inn','student':'swabbie',
                    'boy':'matey','madam':'proud beauty',
                    'professor':'foul blaggart','restaurant':'galley',
                    'your':'yer','excuse':'arr','students':'swabbies',
                    'are':'be','lawyer':'foul blaggart','the':'th',
                    'restroom':'head','my':'me','hello':'avast',
                    'is':'be','man':'matey'}

    # split the input phrase into list of words
    words = phrase.split()

    # for each word in all the words
    for word in words:
        # if the word is in the pirate translator, translate the word
        if word in pirate_transalation:
            pirate_talk.append(pirate_transalation[word])
        # else keep the word
        else:
            pirate_talk.append(word)

    return (" ".join(pirate_talk))

# # End of skills. See below for advanced problems.
# # To work on them, set ADVANCED=True at the top of this file.
# ############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """
    # empty list for strings of characters
    top_char = []
    count = 0
    count_dict = {}

    for char in input_string:
        if char not in count_dict and char.isalph():
            count_dict[char] = count
        else:
            count_dict[char] += 1

    for i in range(len(count_dict)):
        if count_dict[i] >= count_dict[i + 1]:
            top_char = count_dict[i]
            print top_char
    return top_char
    #### I ran out of time to complete this one!


# def adv_alpha_sort_by_word_length(words):
#     """Given a list of words, return a list of tuples, ordered by word-length.

#     Each tuple should have two items--a number that is a word-length,
#     and the list of words of that word length. In addition to ordering
#     the list by word length, order each sub-list of words alphabetically.
#     Now try doing it with only one call to .sort() or sorted(). What does the
#     optional "key" argument for .sort() and sorted() do?

#     For example:

#         >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
#         [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

#     """

#     return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print