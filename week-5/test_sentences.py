from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import random
import pytest

def test_get_determiner():

    # 1. Test the single determiners.
    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        determiner = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert determiner in single_determiners

    # 2. Test the plural determiners.
    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        determiner = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert determiner in plural_determiners

def test_get_noun():

    # 1. Test the single nouns.
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_noun function which should return a single noun.
        noun = get_noun(1)

        # Verify that the word returned from get_noun is one of the words in single_nouns list.
        assert noun in single_nouns

    # 2. Test the plural nouns.
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_noun function which should return a plural noun.
        noun = get_noun(2)

        # Verify that the word returned from get_noun is one of the words in plural_nouns list.
        assert noun in plural_nouns

def test_get_verb():

    # 1. Test the past verbs.
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_verb function which should return a past verb.
        verb = get_verb(1, "past")

        # Verify that the word returned from get_verb is on of the words in past_verbs list.
        assert verb in past_verbs

    # 2. Test the single present verbs.
    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_verb function which should return a single present verb.
        verb = get_verb(1, "present")

        # Verify that the word returned from get_verb is on of the words in single_present_verbs list.
        assert verb in single_present_verbs

    # 3. Test the plural present verbs.
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_verb function which should return a plural present verb.
        verb = get_verb(2, "present")

        # Verify that the word returned from get_verb is on of the words in single_present_verbs list.
        assert verb in plural_present_verbs

     # 4. Test the future verbs.
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_verb function which should return a past verb.
        verb = get_verb(1,"future")

        # Verify that the word returned from get_verb is on of the words in past_verbs list.
        assert verb in future_verbs


def test_get_preposition():
     # 1. Test the get_preposition.
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(31):

        # Call the get_verb function which should return a past verb.
        preposition = get_preposition()

        assert preposition in prepositions

def test_get_prepositional_phrase():

    # 1. Test single prepositional phrase
    quantity = 1
    prep = get_prepositional_phrase(quantity)
    prep2 = prep.split()

    # Assert that length of phrase is 3
    assert len(prep2) == 4

    # declare the prepositions, determiniters, and nouns here
    # so they can be used later
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["some", "many", "the"]
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    adjectives = ["tall", "dark", "black", "short", "happy","sad", "crazy", "long", "awesome", "amazing"]

    # Assert that each word is the correct English part of speech
    assert prep2[0] in prepositions
    assert prep2[1] in single_determiners
    assert prep2[2] in adjectives
    assert prep2[3] in single_nouns

    # 2. Test plural prepositional phrase
    quantity = 2
    prep = get_prepositional_phrase(quantity)
    prep2 = prep.split()

    # Assert that the length of the phrase is 3
    assert len(prep2) == 4

    # Assert that each word is the correct English part of speech
    assert prep2[0] in prepositions
    assert prep2[1] in plural_determiners
    assert prep2[2] in adjectives
    assert prep2[3] in plural_nouns

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])