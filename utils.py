import random

def get_affirmation():
    """Return a random affirmation to help with overthinking."""
    affirmations = [
        "You are stronger than your anxious thoughts.",
        "This moment of overthinking will pass.",
        "You've gotten through difficult moments before.",
        "Your thoughts are not facts.",
        "You are doing the best you can right now.",
        "Take a breath. You are exactly where you need to be.",
        "You are capable of finding calm in the storm.",
        "This feeling is temporary. You will not feel this way forever.",
        "Your worth is not determined by your thoughts.",
        "Breathe in peace, breathe out worry.",
        "You are safe in this moment.",
        "One thought at a time, one moment at a time.",
        "Your mind is a tool, not your master.",
        "You don't have to believe everything you think.",
        "Progress isn't always perfect, and that's okay."
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
