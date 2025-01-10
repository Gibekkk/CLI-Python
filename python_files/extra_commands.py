import random
import datetime

def quote():
    quotes = [
        "yo, life’s a vibe, don’t stress the small stuff.",
        "relax, bro, even the sun takes a break to set.",
        "you can’t rizz the world if you’re not rizzing yourself first.",
        "take it easy, success ain’t ohio—no rush.",
        "even sigma needs a power nap sometimes. recharge, king.",
        "every problem’s just a speed bump on the chill highway.",
        "don’t let the L’s hold you back, they’re just lessons in disguise.",
        "slow down, bro, the grind can wait. vibe first.",
        "your path’s unique, no need to copy someone else’s rizz.",
        "keep it cool, even when life tries to mog you."
    ]
    print(random.choice(quotes))

def time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"yo, current vibe time is {now}. remember, you control the grind, not the clock.")

def encrypt(text):
    encrypted = ''.join(chr(ord(char) + 3) for char in text)
    print(f"encrypted result: {encrypted}")
    
def mood():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        print("morning vibes: wake up, grind slow, and vibe high.")
    elif 12 <= hour < 18:
        print("afternoon vibes: keep chillin', but don't skip the hustle.")
    elif 18 <= hour < 22:
        print("evening vibes: time to slow down and rizz yourself.")
    else:
        print("late night vibes: reflect, recharge, and stay sigma.")
        
def coinflip():
    print(f"coin flip result: {'heads' if random.randint(0, 1) == 0 else 'tails'} (vibes aligned)")


