import os
import openai
from openai import OpenAI

# Initialize the OpenAI client
openai_api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
MODEL = "gpt-4o"

def generate_thought_reframing(original_thought):
    """Generate an AI-powered reframing of an overthinking thought.
    
    Args:
        original_thought (str): The original thought to reframe
        
    Returns:
        str: A supportive reframing of the thought
    """
    try:
        if not original_thought.strip():
            return ""
            
        prompt = f"""
        As Krish (Bean) talking to your girlfriend Hiya (Boopie), provide a kind, thoughtful reframing of this overthinking thought. 
        She attends Purdue University, while you go to Penn State. You often joke that Penn State is better.
        She lives in West Lafayette. You both want to travel to Paris and Greece someday.
        Her favorite song is "ilym" by John K. You gave her a bunny plushie named Daisy.
        She gave you a bat plushie named Drax. You started dating on June 27, 2024.
        
        Use personal details, inside jokes, and warm reassurance. Speak as if you're talking directly to her.
        Keep your response to 3-4 sentences maximum. Be warm, loving, and supportive.
        
        Her overthinking thought: "{original_thought}"
        
        Your reframing as Bean:
        """
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a supportive, loving boyfriend helping your girlfriend reframe anxious thoughts."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"I had trouble generating a response right now. But know that I'm here for you, Boopie. ❤️ Error: {str(e)}"

def generate_custom_affirmation():
    """Generate an AI-powered personalized affirmation from Bean to Boopie.
    
    Returns:
        str: A personalized affirmation
    """
    try:
        prompt = """
        Create a single personalized affirmation from Krish (Bean) to his girlfriend Hiya (Boopie).
        Include a specific personal detail, like the fact that they both have trypophobia, 
        they want a husky in the future, her hazel eyes, she loves Kinder Joy,
        she loves Lord of the Rings, they started dating June 27, 2024, or her long beautiful hair.
        
        Make it affirming, supportive, and loving with a touch of humor or playfulness.
        Keep it short (15-25 words maximum).
        """
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a supportive, loving boyfriend creating affirming messages for your girlfriend."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60,
            temperature=0.8
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Your Bean loves you, Boopie. Always and forever. ❤️"

def generate_personalized_advice(situation):
    """Generate personalized advice for a specific situation.
    
    Args:
        situation (str): The situation or feeling to address
        
    Returns:
        str: Personalized advice
    """
    try:
        if not situation.strip():
            return ""
            
        prompt = f"""
        As Krish (Bean) talking to your girlfriend Hiya (Boopie), provide personalized advice for this situation.
        She attends Purdue University, while you go to Penn State. You often joke that Penn State is better.
        She lives in West Lafayette. You both want to travel to Paris and Greece someday.
        Her favorite song is "ilym" by John K. You gave her a bunny plushie named Daisy.
        She gave you a bat plushie named Drax. You started dating on June 27, 2024.
        
        Use personal details, inside jokes, and warm reassurance. Speak as if you're talking directly to her.
        Give practical, helpful advice while being supportive. Keep your response to 3-5 sentences.
        
        Situation: "{situation}"
        
        Your advice as Bean:
        """
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a supportive, loving boyfriend giving personalized advice."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"I had trouble generating advice right now. But I'm here for you, Boopie. ❤️ Error: {str(e)}"