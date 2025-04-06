import streamlit as st
import random
import datetime
from utils import get_affirmation, get_breathing_instructions
from exercises import get_grounding_exercise, get_overthinking_questions, get_reframing_exercise
from ai_helper import generate_thought_reframing, generate_custom_affirmation, generate_personalized_advice

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
if 'thought_log' not in st.session_state:
    st.session_state.thought_log = []

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
    
    # Initialize daily message in session state if not exists
    if 'daily_message' not in st.session_state or 'last_message_date' not in st.session_state:
        st.session_state.daily_message = None
        st.session_state.last_message_date = None
    
    # Check if we need a new message (date changed or no message yet)
    current_date = datetime.datetime.now().date()
    if st.session_state.last_message_date != current_date or st.session_state.daily_message is None:
        if st.button("Get today's special message", key="daily_message_btn"):
            with st.spinner("Bean is writing something just for you..."):
                st.session_state.daily_message = generate_custom_affirmation()
                st.session_state.last_message_date = current_date
    
    # Display the message if it exists
    if st.session_state.daily_message:
        st.success(st.session_state.daily_message)
    
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
                    new_entry = {
                        "original": current_thought,
                        "reframed": reframed_thought,
                        "method": "self-guided"
                    }
                    st.session_state.thought_log.append(new_entry)
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
                    new_entry = {
                        "original": current_thought,
                        "reframed": ai_reframing,
                        "method": "ai-suggested"
                    }
                    st.session_state.thought_log.append(new_entry)
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
            st.success(custom_affirmation)
    
    st.markdown("---")
    
    if not st.session_state.thought_log:
        st.info("Your journal is empty. Visit the Thought Reframing page to add entries. Just like we've been dreaming of our future husky, we can fill this page with positive thoughts! 🐺")
    else:
        st.markdown("### Your Journal Entries")
        for i, entry in enumerate(st.session_state.thought_log):
            method_label = "💭 Self-Guided" if entry.get('method') == "self-guided" else "✨ Bean's AI Reframing"
            with st.expander(f"Journal Entry {i+1} - {method_label}"):
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
