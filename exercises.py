def get_grounding_exercise():
    """Return instructions for the 5-4-3-2-1 grounding exercise."""
    exercise = {
        "5 Things You Can See": "Look around and notice five things you can see. Focus on details you might not usually notice.",
        "4 Things You Can Touch": "Notice four things you can physically feel - the texture of your clothes, the surface you're sitting on, etc.",
        "3 Things You Can Hear": "Listen for three distinct sounds around you, near or far.",
        "2 Things You Can Smell": "What two scents can you detect? If you can't smell anything right now, think of two scents you enjoy.",
        "1 Thing You Can Taste": "What can you taste right now? Or think of one favorite taste you enjoy."
    }
    return exercise

def get_overthinking_questions():
    """Return questions to challenge overthinking thoughts."""
    questions = [
        "What evidence supports this thought?",
        "What evidence contradicts this thought?",
        "Is there another way to look at this situation?",
        "What would I tell a friend who had this thought?",
        "Will this matter as much in 6 months? A year?",
        "Am I confusing a thought with a fact?",
        "Am I assuming I know what others are thinking?",
        "Am I expecting perfection from myself?"
    ]
    return questions

def get_reframing_exercise():
    """Return instructions for thought reframing."""
    instructions = """
    To reframe your thought, consider:
    
    1. Identifying the cognitive distortion (all-or-nothing thinking, catastrophizing, mind reading, etc.)
    2. Looking for the factual evidence (not assumptions or fears)
    3. Considering a more balanced or compassionate perspective
    4. Focusing on what you can control or influence
    5. Acknowledging uncertainty while not assuming the worst
    
    Your reframed thought should be both realistic and helpful.
    """
    return instructions
