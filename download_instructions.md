# How to Download and Run Locally

This document contains all the code and instructions to set up the Overthinking Helper app locally.

## Step 1: Create Project Structure

Create the following folders and files on your computer:

```
overthinking-helper/
  ├── app.py
  ├── ai_helper.py
  ├── database.py
  ├── exercises.py
  ├── utils.py
  ├── assets/
  │   └── calm.svg
  └── .streamlit/
      └── config.toml
```

## Step 2: Copy Each File's Contents

### app.py
```python
import streamlit as st
import random
import datetime
from utils import get_affirmation, get_breathing_instructions
from exercises import get_grounding_exercise, get_overthinking_questions, get_reframing_exercise
from ai_helper import generate_thought_reframing, generate_custom_affirmation, generate_personalized_advice
import database as db

# Page configuration
st.set_page_config(
    page_title="Boopie's Calm Space",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if they don't exist
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'breathing_count' not in st.session_state:
    st.session_state.breathing_count = 0

# Calculate days together
relationship_start = datetime.datetime(2024, 6, 27)
today = datetime.datetime.now()
days_together = (today - relationship_start).days

# Function to change pages
def navigate_to(page):
    st.session_state.current_page = page
    st.rerun()

# Sidebar navigation
with st.sidebar:
    st.image("assets/calm.svg", width=100)
    st.markdown(f"## Hey Boopie! 💕")
    st.markdown("##### Tools for when your mind races")
    
    # Navigation buttons
    st.button("Home", on_click=navigate_to, args=('home',), 
              use_container_width=True)
    st.button("Breathing Exercise", on_click=navigate_to, args=('breathing',), 
              use_container_width=True)
    st.button("Grounding Exercise", on_click=navigate_to, args=('grounding',), 
              use_container_width=True)
    st.button("Thought Reframing", on_click=navigate_to, args=('reframing',), 
              use_container_width=True)
    st.button("Thought Journal", on_click=navigate_to, args=('journal',), 
              use_container_width=True)
    
    # Personal touches
    st.markdown("---")
    st.markdown(f"**Bean & Boopie**")
    st.markdown(f"*{days_together} days of adventures together* 💫")
    
    # Affirmation at the bottom of sidebar
    st.markdown("---")
    st.markdown(f"*{get_affirmation()}*")
    
    # Song recommendation
    st.markdown("---")
    st.markdown("**When you need a smile:**")
    st.markdown("Listen to 'ilym' by John K 🎵")
    st.markdown("*Or check out our 'Happy Baby' playlist* 🎧")

# Home page
if st.session_state.current_page == 'home':
    st.title("Hey Hiya! Your Calm Space Awaits 💖")
    
    st.markdown(f"""
    ### From Bean to Boopie with love
    
    This is a special space just for you, for those moments when your beautiful mind 
    is racing too fast. Whether you're in your studio in West Lafayette or anywhere else,
    I'm here with you in spirit.
    
    **How's my Boopie feeling right now?**
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Anxious or worried", use_container_width=True):
            navigate_to('breathing')
    
    with col2:
        if st.button("Stuck in my thoughts", use_container_width=True):
            navigate_to('grounding')
    
    with col3:
        if st.button("Need perspective", use_container_width=True):
            navigate_to('reframing')
    
    # AI Daily Message
    st.markdown("---")
    st.markdown("### Today's Message from Bean 💌")
    
    # Check for today's message in the database
    today_message = db.get_today_message()
    
    # If no message for today, provide option to generate one
    if not today_message:
        if st.button("Get today's special message", key="daily_message_btn"):
            with st.spinner("Bean is writing something just for you..."):
                new_message = generate_custom_affirmation()
                # Save the message to the database
                db.save_daily_message(new_message)
                today_message = new_message
    
    # Display the message if it exists
    if today_message:
        st.success(today_message)
    
    # Creative activity suggestion
    st.markdown("---")
    st.markdown("### Maybe some coloring would help?")
    st.markdown("I know how much you enjoy drawing and coloring when your mind is busy. Maybe take out your art supplies for a bit? 🎨")
    
    st.markdown("---")
    
    st.markdown("""
    ### Just a few reminders from your Bean:
    
    * Your thoughts are just thoughts, not reality - like how Penn State is clearly superior to Purdue 😉
    * This moment will pass, just like our debates about you eating enough
    * You're amazing at working through challenges (except spelling "Porsche" correctly 😘)
    * When in doubt, hug Daisy the bunny tight!
    
    Remember our Paris dream? Balcony, bathrobes, wine, Eiffel Tower view? 
    Keep breathing, we'll get there someday. 🗼✨
    """)
    
    # Add direct link to AI advice
    st.markdown("---")
    st.markdown("### Need Bean's advice right now?")
    if st.button("Get Personalized Advice", use_container_width=True):
        navigate_to('journal')
        # Note: We'll direct to the journal page which has the advice section

# Breathing exercise page
elif st.session_state.current_page == 'breathing':
    st.title("Breathing Exercise")
    
    st.markdown("""
    ### 4-7-8 Breathing Technique
    
    Let those beautiful hazel eyes close for a moment, Boops. This breathing technique
    will help calm your nervous system when your mind is racing too fast.
    """)
    
    # Get breathing instructions
    instruction, duration = get_breathing_instructions(st.session_state.breathing_count)
    
    # Create a large display for the current instruction
    st.markdown(f"## {instruction}")
    
    # Progress bar to visualize the breathing cycle
    progress_bar = st.progress(0)
    
    # Using st.empty() to create placeholders for updating elements
    message_placeholder = st.empty()
    
    # Button to manually advance through the breathing cycle
    if st.button("Next Breath"):
        st.session_state.breathing_count = (st.session_state.breathing_count + 1) % 3
        st.rerun()
    
    # Add a note about us
    st.info("Remember when we watched The Night Agent together and you said the suspense was making your heart race? This breathing exercise helps with exactly that feeling! 💕")
    
    st.markdown("""
    #### Benefits of Deep Breathing:
    
    * Reduces stress and anxiety
    * Lowers heart rate and blood pressure
    * Helps clear your mind - even after staying up too late (you night owl! 🦉)
    * Improves focus and concentration
    
    Try to complete at least 4 full cycles (inhale, hold, exhale) for maximum benefit.
    Then maybe have a Kinder Joy? Everything's better with chocolate 🍫
    """)

# Grounding exercise page
elif st.session_state.current_page == 'grounding':
    st.title("Grounding Exercise")
    
    st.markdown("""
    ### 5-4-3-2-1 Grounding Technique
    
    When your mind gets lost in Purdue vs. Penn State debates (we know which is better 😉) or 
    any other overthinking spirals, this exercise helps bring you back to your cute little 
    studio in West Lafayette by engaging your five senses.
    """)
    
    # Get the grounding exercise
    steps = get_grounding_exercise()
    
    # Display each step with examples with personal touches
    st.markdown(f"### {list(steps.keys())[0]}")  # 5 Things You Can See
    st.markdown(f"{steps[list(steps.keys())[0]]}")
    st.markdown("*(Maybe Daisy the bunny plushie is one of them? Or that katana you got me?)*")
    user_input = st.text_area(f"Write what you notice for {list(steps.keys())[0].lower()}", key=list(steps.keys())[0])
    
    st.markdown(f"### {list(steps.keys())[1]}")  # 4 Things You Can Touch
    st.markdown(f"{steps[list(steps.keys())[1]]}")
    st.markdown("*(Your drawing supplies? The soft fur of Daisy?)*")
    user_input = st.text_area(f"Write what you notice for {list(steps.keys())[1].lower()}", key=list(steps.keys())[1])
    
    st.markdown(f"### {list(steps.keys())[2]}")  # 3 Things You Can Hear
    st.markdown(f"{steps[list(steps.keys())[2]]}")
    st.markdown("*(Maybe put on 'ilym' by John K in the background?)*")
    user_input = st.text_area(f"Write what you notice for {list(steps.keys())[2].lower()}", key=list(steps.keys())[2])
    
    st.markdown(f"### {list(steps.keys())[3]}")  # 2 Things You Can Smell
    st.markdown(f"{steps[list(steps.keys())[3]]}")
    st.markdown("*(The amazing pasta you make? Though maybe not takoyaki since your Bean is vegetarian 😘)*")
    user_input = st.text_area(f"Write what you notice for {list(steps.keys())[3].lower()}", key=list(steps.keys())[3])
    
    st.markdown(f"### {list(steps.keys())[4]}")  # 1 Thing You Can Taste
    st.markdown(f"{steps[list(steps.keys())[4]]}")
    st.markdown("*(Kinder Joy, perhaps?)*")
    user_input = st.text_area(f"Write what you notice for {list(steps.keys())[4].lower()}", key=list(steps.keys())[4])
    
    st.markdown("""
    ### How does my Boopie feel now?
    
    Taking time to notice what's actually around you can help break the cycle of overthinking
    by anchoring you in the present moment. Remember, one day we'll share that view of the 
    Eiffel Tower together - sipping wine in bathrobes from our dream balcony in Paris.
    """)
    
    if st.button("I feel more grounded"):
        st.balloons()
        st.success("Wonderful, Boops! And remember - our future will have a husky too! 🐺")

# Thought reframing page
elif st.session_state.current_page == 'reframing':
    st.title("Thought Reframing for My Boopie")
    
    st.markdown("""
    ### Challenge Your Overthinking
    
    Those beautiful thoughts in your mind sometimes get tangled up in ways that 
    aren't quite true - just like when you worry if you're eating enough (you're not 😉).
    
    Let your Bean help you reframe these thoughts into something more true and kind.
    """)
    
    # Get overthinking reframing exercise
    questions = get_overthinking_questions()
    
    # Add some Lord of the Rings reference
    st.info("As they say in Lord of the Rings: 'Not all those who wander are lost.' And not all thoughts that wander into your mind are true! 🧙‍♂️")
    
    # Current thought input
    current_thought = st.text_area("What thought is my Boopie overthinking about?", 
                                 placeholder="Example: I'm not doing well enough in my studies at Purdue...")
    
    if current_thought:
        # Tabs for different reframing approaches
        tab1, tab2 = st.tabs(["Self-Guided Reframing", "Bean's AI Suggestion"])
        
        with tab1:
            st.markdown("### Let's examine this thought:")
            
            for question in questions:
                st.text_area(question, key=question)
            
            reframing = get_reframing_exercise()
            st.markdown("### Now, try reframing your thought:")
            st.markdown(reframing)
            
            reframed_thought = st.text_area("Write your reframed thought here:", 
                                         placeholder="Example: I'm working hard at Purdue and learning at my own pace. Every day I make progress, even when it's not perfect.")
            
            if reframed_thought:
                if st.button("Save this reframing", key="save_self"):
                    # Save to database
                    db.save_thought_entry(current_thought, reframed_thought, "self-guided")
                    st.success("Your Bean is so proud of you for reframing your thoughts! It's saved to your journal! 💖")
        
        with tab2:
            st.markdown("### Let Bean help you reframe this:")
            st.write("I'll give this thought a fresh perspective, just like how we always talk about our future together. ❤️")
            
            # Add a button to generate AI response
            if st.button("Get Bean's reframing", key="ai_reframe"):
                with st.spinner("Bean is thinking of the perfect words for you..."):
                    ai_reframing = generate_thought_reframing(current_thought)
                    
                # Display AI response in a special format
                st.info(ai_reframing)
                
                # Option to save the AI reframing
                if st.button("Save Bean's reframing to journal", key="save_ai"):
                    # Save to database
                    db.save_thought_entry(current_thought, ai_reframing, "ai-suggested")
                    st.success("Bean's words of wisdom are saved to your journal! 💖")

# Thought journal page
elif st.session_state.current_page == 'journal':
    st.title("Boopie's Thought Journal")
    
    st.markdown(f"""
    ### Your Beautiful Mind's Journey
    
    Just like we're on our journey together (since June 27, 2024!), 
    these are the thoughts you've been working on reframing. Looking back at these
    can show how much your perspective has grown.
    """)
    
    # Add an AI-generated affirmation
    with st.container():
        st.markdown("#### Today's special message from Bean:")
        if st.button("Get a personalized message", key="get_affirmation"):
            with st.spinner("Bean is writing something special for you..."):
                custom_affirmation = generate_custom_affirmation()
                # Save the affirmation to the database
                db.save_daily_message(custom_affirmation)
            st.success(custom_affirmation)
    
    st.markdown("---")
    
    # Load entries from database
    entries = db.get_thought_entries()
    
    if not entries:
        st.info("Your journal is empty. Visit the Thought Reframing page to add entries. Just like we've been dreaming of our future husky, we can fill this page with positive thoughts! 🐺")
    else:
        st.markdown("### Your Journal Entries")
        for i, entry in enumerate(entries):
            method_label = "💭 Self-Guided" if entry['method'] == "self-guided" else "✨ Bean's AI Reframing"
            date_str = datetime.datetime.fromisoformat(entry['created_at']).strftime("%b %d, %Y at %I:%M %p")
            with st.expander(f"Journal Entry {i+1} - {date_str} - {method_label}"):
                st.markdown("**Original thought:**")
                st.markdown(f"*{entry['original']}*")
                st.markdown("**Reframed thought:**")
                st.markdown(f"*{entry['reframed']}*")
    
    # Add a section for personalized advice
    st.markdown("---")
    st.markdown("### Need advice on something specific?")
    st.write("I'm here to help with any particular situation you're facing, Boopie.")
    
    specific_situation = st.text_area("What's on your mind?", 
                                     placeholder="Example: I'm feeling nervous about my upcoming presentation...")
    
    if specific_situation:
        if st.button("Get Bean's advice", key="get_advice"):
            with st.spinner("Bean is thinking of the best advice for you..."):
                personalized_advice = generate_personalized_advice(specific_situation)
            st.info(personalized_advice)
    
    st.markdown("---")
    st.markdown("""
    ### Looking at your journal helps you:
    
    * See patterns in your overthinking (like how cute your nose is, no matter what you think 😉)
    * Remember that you're stronger than trypophobia or any other fear we share
    * Track your growth as you handle challenges
    * Realize you have the wisdom to transform anxious thoughts into peaceful ones
    
    One day I'll buy you that Birkin we talk about, but for now, I hope this helps carry your thoughts in a beautiful way. 👜✨
    """)
```

### ai_helper.py
```python
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
```

### database.py
```python
import sqlite3
import os
import datetime

# Create a directory for the database if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Database connection
def get_db_connection():
    """Get a connection to the SQLite database."""
    conn = sqlite3.connect('data/overthinking_helper.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database with required tables
def init_db():
    """Initialize the database with required tables."""
    conn = get_db_connection()
    try:
        # Create thought_journal table
        conn.execute('''
        CREATE TABLE IF NOT EXISTS thought_journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_thought TEXT NOT NULL,
            reframed_thought TEXT NOT NULL,
            reframing_method TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Create affirmations table to store generated affirmations
        conn.execute('''
        CREATE TABLE IF NOT EXISTS daily_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Create user_preferences table
        conn.execute('''
        CREATE TABLE IF NOT EXISTS user_preferences (
            id INTEGER PRIMARY KEY,
            nickname TEXT DEFAULT 'Boopie',
            last_login TIMESTAMP
        )
        ''')
        
        # Insert default user preferences if not exist
        conn.execute('''
        INSERT OR IGNORE INTO user_preferences (id, nickname, last_login)
        VALUES (1, 'Boopie', ?)
        ''', (datetime.datetime.now(),))
        
        conn.commit()
    finally:
        conn.close()

# Journal entry functions
def save_thought_entry(original_thought, reframed_thought, reframing_method):
    """Save a thought journal entry to the database.
    
    Args:
        original_thought (str): The original overthinking thought
        reframed_thought (str): The reframed positive thought
        reframing_method (str): Either 'self-guided' or 'ai-suggested'
    
    Returns:
        int: The ID of the newly inserted entry
    """
    conn = get_db_connection()
    try:
        cursor = conn.execute('''
        INSERT INTO thought_journal (original_thought, reframed_thought, reframing_method)
        VALUES (?, ?, ?)
        ''', (original_thought, reframed_thought, reframing_method))
        
        entry_id = cursor.lastrowid
        conn.commit()
        return entry_id
    finally:
        conn.close()

def get_thought_entries():
    """Get all thought journal entries from the database.
    
    Returns:
        list: A list of dictionaries containing the thought journal entries
    """
    conn = get_db_connection()
    try:
        cursor = conn.execute('''
        SELECT id, original_thought, reframed_thought, reframing_method, created_at
        FROM thought_journal
        ORDER BY created_at DESC
        ''')
        
        entries = []
        for row in cursor.fetchall():
            entries.append({
                'id': row['id'],
                'original': row['original_thought'],
                'reframed': row['reframed_thought'],
                'method': row['reframing_method'],
                'created_at': row['created_at']
            })
        
        return entries
    finally:
        conn.close()

# Daily message functions
def save_daily_message(message):
    """Save a daily message to the database.
    
    Args:
        message (str): The daily message to save
    
    Returns:
        int: The ID of the newly inserted message
    """
    conn = get_db_connection()
    try:
        cursor = conn.execute('''
        INSERT INTO daily_messages (message)
        VALUES (?)
        ''', (message,))
        
        message_id = cursor.lastrowid
        conn.commit()
        return message_id
    finally:
        conn.close()

def get_latest_daily_message():
    """Get the latest daily message from the database.
    
    Returns:
        str: The latest daily message or None if no messages exist
    """
    conn = get_db_connection()
    try:
        cursor = conn.execute('''
        SELECT message, created_at
        FROM daily_messages
        ORDER BY created_at DESC
        LIMIT 1
        ''')
        
        row = cursor.fetchone()
        if row:
            return {
                'message': row['message'],
                'created_at': row['created_at']
            }
        return None
    finally:
        conn.close()

def get_today_message():
    """Get a message created today if it exists.
    
    Returns:
        str: Today's message or None if no message for today
    """
    conn = get_db_connection()
    try:
        today = datetime.datetime.now().date()
        cursor = conn.execute('''
        SELECT message
        FROM daily_messages
        WHERE date(created_at) = date(?)
        ORDER BY created_at DESC
        LIMIT 1
        ''', (today,))
        
        row = cursor.fetchone()
        return row['message'] if row else None
    finally:
        conn.close()

# Initialize the database when module is imported
init_db()
```

### exercises.py
```python
def get_grounding_exercise():
    """Return instructions for the 5-4-3-2-1 grounding exercise."""
    steps = {
        "5 Things You Can See": "Look around and name 5 things you can see right now.",
        "4 Things You Can Touch": "Find 4 things you can physically touch or feel.",
        "3 Things You Can Hear": "Listen carefully and identify 3 sounds you can hear.",
        "2 Things You Can Smell": "Notice 2 scents in your environment.",
        "1 Thing You Can Taste": "Focus on 1 taste in your mouth right now."
    }
    return steps

def get_overthinking_questions():
    """Return questions to challenge overthinking thoughts."""
    questions = [
        "Is this thought definitely true? What evidence do I have?",
        "Am I confusing a thought with a fact?",
        "What would I tell Krish (Bean) if he had this same thought?",
        "Will this matter in 5 days? 5 weeks? 5 years?",
        "Is this thought helpful to me right now?",
        "What's a more balanced or realistic perspective?"
    ]
    return questions

def get_reframing_exercise():
    """Return instructions for thought reframing."""
    return """
    Take your original thought and transform it into something:
    
    * More balanced and realistic
    * Kind to yourself (like you'd speak to me 💕)
    * Forward-looking rather than stuck
    * Acknowledging your strength (you have so much!)
    
    Remember how you helped me reframe my fears about the future? You're amazing at this!
    """
```

### utils.py
```python
import random

def get_affirmation():
    """Return a random affirmation to help with overthinking."""
    affirmations = [
        "Your thoughts are not facts - just like 'Purdue is better than Penn State' isn't a fact! 😉",
        "You're doing better than you think, Boopie. Bean is always proud of you.",
        "Your hazel eyes deserve to see beauty, not worries.",
        "This feeling is temporary, just like our debates about cats vs. dogs.",
        "Take a deep breath - our Paris dreams are waiting for you.",
        "Daisy the bunny believes in you, and so do I.",
        "One step at a time, just like our plans for getting a husky someday.",
        "Your overthinking mind is powerful - channel it into your amazing art instead.",
        "I love all of you, even the parts that worry too much.",
        "When in doubt, remember our first date and how far we've come.",
        "You've overcome so much already - this is just another mountain you'll conquer.",
        "Our future has too many adventures waiting to be stuck in worries today.",
        "Bean-approved reminder: you're exactly where you need to be right now."
    ]
    return random.choice(affirmations)

def get_breathing_instructions(count):
    """Return instructions for the current step in the breathing exercise."""
    steps = [
        ("Inhale through your nose for 4 seconds", 4),
        ("Hold your breath for 7 seconds", 7),
        ("Exhale through your mouth for 8 seconds", 8)
    ]
    return steps[count]
```

### .streamlit/config.toml
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000
```

### assets/calm.svg
```xml
<svg width="410" height="404" viewBox="0 0 410 404" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M399.641 59.5246L215.643 388.545C211.844 395.338 202.084 395.378 198.228 388.618L10.5817 59.5563C6.38087 52.1896 12.6802 43.2665 21.0281 44.7586L205.223 77.6824C206.398 77.8924 207.601 77.8904 208.776 77.6763L389.119 44.8058C397.439 43.2894 403.768 52.1434 399.641 59.5246Z" fill="url(#paint0_linear)"/>
<path d="M292.965 1.5744L156.801 28.2552C154.563 28.6937 152.906 30.5903 152.771 32.8664L144.395 174.33C144.198 177.662 147.258 180.248 150.51 179.498L188.42 170.749C191.967 169.931 195.172 173.055 194.443 176.622L183.18 231.775C182.422 235.487 185.907 238.661 189.532 237.56L212.947 230.446C216.577 229.344 220.065 232.527 219.297 236.242L201.398 322.875C200.278 328.294 207.486 331.249 210.492 326.603L212.5 323.5L323.454 102.072C325.312 98.3645 322.108 94.137 318.036 94.9228L279.014 102.454C275.347 103.161 272.227 99.746 273.262 96.1583L298.731 7.86689C299.767 4.27314 296.636 0.855181 292.965 1.5744Z" fill="url(#paint1_linear)"/>
<defs>
<linearGradient id="paint0_linear" x1="6.00017" y1="32.9999" x2="235" y2="344" gradientUnits="userSpaceOnUse">
<stop stop-color="#FF7DD3"/>
<stop offset="1" stop-color="#FFB0EE"/>
</linearGradient>
<linearGradient id="paint1_linear" x1="194.651" y1="8.81818" x2="236.076" y2="292.989" gradientUnits="userSpaceOnUse">
<stop stop-color="#FF48C0"/>
<stop offset="1" stop-color="#FFB0EE"/>
</linearGradient>
</defs>
</svg>
```

## Step 3: Set Up Environment

1. Make sure you have Python installed (3.6 or newer)

2. Install the required packages:
```bash
pip install streamlit openai
```

3. Set up your OpenAI API key as an environment variable:
   - Windows Command Prompt: `set OPENAI_API_KEY=your_api_key_here`
   - Windows PowerShell: `$env:OPENAI_API_KEY="your_api_key_here"`
   - Mac/Linux: `export OPENAI_API_KEY=your_api_key_here`

## Step 4: Run the App

Navigate to your project directory in the terminal/command prompt and run:

```bash
streamlit run app.py
```

The app will open in your browser, typically at http://localhost:8501

## Notes

- The SQLite database will be created in a 'data' directory when the app is first run
- All journal entries and daily messages will be stored locally in this database
- You can modify any personal details in the code to customize it further if needed