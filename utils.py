import random

def get_affirmation():
    """Return a random affirmation to help with overthinking."""
    affirmations = [
        "You are stronger than your anxious thoughts, Boopie.",
        "This moment of overthinking will pass - just like our Night Agent binge-watching.",
        "You've gotten through difficult moments before. Remember how brave you are?",
        "Your thoughts are not facts - just like 'Purdue is better than Penn State' isn't a fact! 😉",
        "You are doing the best you can right now, and that's all that matters.",
        "Take a breath. Your Bean loves you exactly as you are.",
        "You are capable of finding calm in the storm, just like you're capable of making amazing pasta.",
        "This feeling is temporary. One day we'll have our husky and laugh about today's worries.",
        "Your worth is not determined by your thoughts - it's in those beautiful hazel eyes.",
        "Breathe in peace, breathe out worry. I'm always here for you.",
        "You are safe in this moment. Daisy the bunny is watching over you.",
        "One thought at a time, one moment at a time. We'll get to Greece for our honeymoon someday.",
        "Your beautiful mind is a tool, not your master.",
        "I love your cute nose and everything about you, even when you don't.",
        "It's okay to stay up late sometimes, my night owl. Your thoughts will be clearer in the morning."
    ]
    return random.choice(affirmations)

def get_breathing_instructions(count):
    """Return instructions for the current step in the breathing exercise."""
    steps = [
        ("Inhale slowly through your nose", 4),
        ("Hold your breath", 7),
        ("Exhale completely through your mouth", 8)
    ]
    return steps[count]
