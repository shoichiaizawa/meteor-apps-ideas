import random
import ast

def pop(a,accumulated=None):
    print "type q to move on to verification"
    if accumulated is None:
        accumulated = set()
    v = 'I can put any string here, as long as it is not "q" :-)'
    while v.lower() != 'q':
        b = a.pop(0)
        if b <= 15:
            print 'b', b,
        elif b > 15 and b <=30:
            print 'i', b,
        elif b > 30 and b <=45:
            print 'n', b,
        elif b > 45 and b <=60:
            print 'g', b,
        else:
            print 'o', b,
        accumulated.add(b)
        v = raw_input('')
    return accumulated

def verify(numbers):
    new_nums = raw_input("enter numbers separated by ',': ")
    nums = ast.literal_eval(new_nums)
    assert( len(nums) == 5 ) #Need 5 numbers to win
    result = set(nums).issubset(numbers)
    print "Verified? ",result
    return result
    #alternatively, and probably slightly more efficient
    # print numbers.issuperset(nums)
    #I prefer the other though as `subset` is easier for me to remember


def robust_verify(numbers):
   """
   keep trying to verify the numbers until we succeed
   """
   try:
       verify(numbers)
   except (AssertionError,SyntaxError,TypeError):  #other error conditions might go here too, but these are the ones I can think of right now ...
       robust_verify(numbers)


def play_bingo(game_vals=None,accumulated=None):
    if game_vals is None:
        game_vals = list(range(1,76))  #list strictly not necessary here, but why not?
        random.shuffle(game_vals)

    nums = pop(game_vals,accumulated=accumulated)
    if not robust_verify(nums):
        play_bingo(game_vals=game_vals,accumulated=nums)


play_bingo()
