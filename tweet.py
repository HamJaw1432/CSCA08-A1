"""
Assignment 1.
Jawad Arshad
Student # 1006280917

"""

import math

# Maximum number of characters in a valid tweet.
MAX_TWEET_LENGTH = 3

# The first character in a hashtag.
HASHTAG_SYMBOL = '#'

# The first character in a mention.
MENTION_SYMBOL = '@'

# Underscore is the only non-alphanumeric character that can be part
# of a word (or username) in a tweet.
UNDERSCORE = '_'

SPACE = ' '


def is_valid_tweet(text: str) -> bool:
    """Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False

    """
    return 1 <= len(text) <= MAX_TWEET_LENGTH
    # Complete the body of this function.



# Now define the other functions described in the handout.

def compare_tweet_lengths(tweet_one: str, tweet_two: str) -> int:
    """Return an interger 1, 0, -1, to indicate if tweet_one is 
    longer or tweet_two. 
    
    If the first tweet_one is longer than the tweet_two return 1, 
    if the first tweet_one is shorter than the tweet_two return -1, 
    if they are the same size return 0
    
    Precondition:
    tweet_one and tweet_two are valid tweets
    
    >>> compare_tweet_lengths('hello', 'bye')
    1
    >>> compare_tweet_lengths('ok', 'hi')
    0
    >>> compare_tweet_lengths('bye', 'hello')
    -1
    """
    if len(tweet_one) > len(tweet_two):
        return 1
    elif len(tweet_one) < len(tweet_two):
        return -1
    return 0
    
    
    
def add_symbol(tweet: str, tweet_word: str, symbol: str) -> str:
    """Return a string new tweet that combines the original 
    tweet with a symbol and the tweet_word
    
    Precondition:
    tweet is s valid tweet
    tweet_word is a valid tweet word
    
    >>>add_symbol('I like', 'CSCA08', HASHTAG_SYMBOL)
    'I like #CSCA08'
    >>>add_symbol('working on', 'assignment1', MENTION_SYMBOL)
    'working on @assignment1'
    """
    potential_tweet = tweet + SPACE + symbol + tweet_word
    if len(potential_tweet) <= MAX_TWEET_LENGTH:
        return potential_tweet 
    return tweet    
    
    
    
def add_hashtag(tweet: str, tweet_word: str) -> str:
    """ Return a string new tweet that combines the original 
    tweet with a hashtag and the tweet_word
    
    Precondition:
    tweet is s valid tweet
    tweet_word is a valid tweet word
    
    >>> add_hashtag('I like', 'CSCA08')
    'I like #CSCA08'
    >>> add_hashtag('working on', 'assignment1')
    'working on #assignment1'
    >>> add_hashtag('this is a test to see if the fuction works if the tweet is longer than the MAX_TWEET_LENGTH', 'oof')
    'this is a test to see if the fuction works if the tweet is longer than the MAX_TWEET_LENGTH'
    """
    return add_symbol(tweet, tweet_word, HASHTAG_SYMBOL)
    
    
    
def contains_hashtag(full_tweet: str, hashtag_word: str) -> bool:
    """Retruns a true or false depending on if the full_tweet contains 
    the hashtag_word, and the the hashtag_word is in fact a hashtag.
    
    Precondition:
    full_tweet is s valid tweet
    hashtag_word is a valid tweet word
    
    >>>contains_hashtag('I like #CSCA08', 'CSCA08')
    True
    >>>contains_hashtag('I like #cscA08, #mat137, and #phl101', 'cscA08')
    True
    >>>contains_hashtag('I like cscA08', 'cscA08')
    False
    >>>contains_hashtag('I like #cscA08', 'csc')
    False
    >>>contains_hashtag('I like #csc&A%0!8', 'cscA08')
    False
    """ 
    return tweet_contains(HASHTAG_SYMBOL, hashtag_word, full_tweet)



def tweet_contains(symbol: str, tweet_word: str, full_tweet: str) -> bool:
    """Retruns a true or false depending on if the full_tweet contains 
    the symbol followed by the tweet_word.
    
    Precondition:
    tweet is s valid tweet
    tweet_word is a valid tweet word

    >>>tweet_contains(HASHTAG_SYMBOL, 'cscA08', 'I like #cscA08')
    True
    >>>tweet_contains(HASHTAG_SYMBOL, 'I like #csc&A%0!8', 'cscA08')
    False
    """
    return (symbol + tweet_word + SPACE) in (clean(full_tweet) + SPACE)



def is_mentioned(full_tweet: str, mention_word: str) -> bool:
    """Retruns a true or false depending on if the full_tweet contains 
    the mention_word, and the the mention_word is in fact a mention.
    
    Precondition:
    full_tweet is s valid tweet
    mention_word is a valid tweet word
    
     >>>is_mentioned('I like @CSCA08', 'CSCA08')
    True
    >>>is_mentioned('I like @cscA08, @mat137, and @phl101', 'cscA08')
    True
    >>>is_mentioned('I like cscA08', 'cscA08')
    False
    >>>is_mentioned('I like @cscA08', 'csc')
    False
    >>>is_mentioned('I like @csc&A%0!8', 'cscA08')
    False
    >>>is_mentioned('I like #cscA08', 'cscA08')
    False
    """
    return tweet_contains(MENTION_SYMBOL, mention_word, full_tweet)



def add_mention_exclusive(full_tweet: str, tweet_word: str) -> str:
    """Return a string that adds a mention to a tweet_word which combines with 
    the full_tweet
    
    >>>add_mention_exclusive('Hello its me', 'me')
    'Hello its @me'
    >>>add_mention_exclusive('Hello its @me', 'me')
    'Hello its @me'
    >>>add_mention_exclusive('#AB', 'AB')
    #AB
    """
    if tweet_contains(MENTION_SYMBOL, tweet_word, full_tweet):
        return full_tweet
    if tweet_contains(SPACE, tweet_word, full_tweet):
        return add_symbol(full_tweet, tweet_word, MENTION_SYMBOL) 
    return full_tweet
    


def num_tweets_required(message: str) -> int:
    """Return the minimum number of tweets that would be required to 
    communicate the entire message.
     
    >>>num_tweets_required('hello')
    1
    >>>num_tweets_required('this is a test to see if the fuction works if the tweet is longer than the MAX_TWEET_LENGTH') 
    2
    """
    return math.ceil((len(message)/MAX_TWEET_LENGTH))


def get_nth_tweet(message: str, num: int) -> str:
    """Return the num string as message may be broken up in to several tweets 
    meet the criteria valid tweet criteria.
    
    Precondition:
    num >= 0 
    
    >>>get_nth_tweet('Hello', 7)
    ''
    >>>get_nth_tweet('this is a test to see if the fuction works if the tweet is longer than the MAX_TWEET_LENGTH', 2) 
    'weet is longer than the MAX_TWEET_LENGTH'
    """
    return message[((num) * MAX_TWEET_LENGTH):((num + 1) * MAX_TWEET_LENGTH)]




# A helper function.  Do not modify this function, but you are welcome
# to call it.

def clean(text: str) -> str:
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str
