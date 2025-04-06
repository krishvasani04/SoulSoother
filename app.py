import streamlit as st
import random
from utils import get_affirmation, get_breathing_instructions
from exercises import get_grounding_exercise, get_overthinking_questions, get_reframing_exercise

# Page configuration
st.set_page_config(
    page_title="Overthinking Helper",
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

# Function to change pages
def navigate_to(page):
    st.session_state.current_page = page
    st.rerun()

# Sidebar navigation
with st.sidebar:
    st.image("assets/calm.svg", width=100)
    st.markdown("## Calm Mind")
    st.markdown("##### Tools for overthinking")
    
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
    
    # Affirmation at the bottom of sidebar
    st.markdown("---")
    st.markdown(f"*{get_affirmation()}*")

# Home page
if st.session_state.current_page == 'home':
    st.title("Welcome to Your Calm Space")
    
    st.markdown("""
    ### When overthinking takes over, this space is here for you.
    
    Overthinking often happens when our minds get stuck in loops of worry or rumination.
    These tools can help you break those cycles and find your way back to the present moment.
    
    **How are you feeling right now?**
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
    
    st.markdown("---")
    
    st.markdown("""
    ### Quick reminder:
    
    * Your thoughts are not facts
    * This moment will pass
    * You've overcome difficult moments before
    * You're not alone in experiencing overthinking
    
    Take a deep breath. You're going to be okay.
    """)

# Breathing exercise page
elif st.session_state.current_page == 'breathing':
    st.title("Breathing Exercise")
    
    st.markdown("""
    ### 4-7-8 Breathing Technique
    
    This simple breathing exercise can help calm your nervous system and bring your attention to the present moment.
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
    
    st.markdown("""
    #### Benefits of Deep Breathing:
    
    * Reduces stress and anxiety
    * Lowers heart rate and blood pressure
    * Helps clear your mind
    * Improves focus and concentration
    
    Try to complete at least 4 full cycles (inhale, hold, exhale) for maximum benefit.
    """)

# Grounding exercise page
elif st.session_state.current_page == 'grounding':
    st.title("Grounding Exercise")
    
    st.markdown("""
    ### 5-4-3-2-1 Grounding Technique
    
    When overthinking pulls you away from the present, this exercise helps bring you back
    by engaging your five senses.
    """)
    
    # Get the grounding exercise
    steps = get_grounding_exercise()
    
    # Display each step with examples
    for sense, instructions in steps.items():
        st.markdown(f"### {sense}")
        st.markdown(instructions)
        user_input = st.text_area(f"Write what you notice for {sense.lower()}", key=sense)
    
    st.markdown("""
    ### How do you feel now?
    
    Taking time to notice what's actually around you can help break the cycle of overthinking
    by anchoring you in the present moment.
    """)
    
    if st.button("I feel more grounded"):
        st.balloons()
        st.success("Wonderful! You can return to this exercise anytime you need to reconnect with the present.")

# Thought reframing page
elif st.session_state.current_page == 'reframing':
    st.title("Thought Reframing")
    
    st.markdown("""
    ### Challenge Your Overthinking
    
    Overthinking often involves cognitive distortions - ways our mind convinces us of things
    that aren't really true. Let's examine and reframe some of those thoughts.
    """)
    
    # Get overthinking reframing exercise
    questions = get_overthinking_questions()
    
    # Current thought input
    current_thought = st.text_area("What thought are you overthinking about?", 
                                 placeholder="Example: I made a mistake in my presentation, everyone must think I'm incompetent.")
    
    if current_thought:
        st.markdown("### Let's examine this thought:")
        
        for question in questions:
            st.text_area(question, key=question)
        
        reframing = get_reframing_exercise()
        st.markdown("### Now, try reframing your thought:")
        st.markdown(reframing)
        
        reframed_thought = st.text_area("Write your reframed thought here:", 
                                     placeholder="Example: I made a mistake, which is something everyone does. This doesn't define my overall performance or ability.")
        
        if reframed_thought:
            if st.button("Save this reframing"):
                new_entry = {
                    "original": current_thought,
                    "reframed": reframed_thought
                }
                st.session_state.thought_log.append(new_entry)
                st.success("Your reframed thought has been saved to your journal!")

# Thought journal page
elif st.session_state.current_page == 'journal':
    st.title("Thought Journal")
    
    st.markdown("""
    ### Your Reframing Journey
    
    Below are the thoughts you've worked on reframing. Revisiting these can remind you
    of your progress and reinforce healthier thinking patterns.
    """)
    
    if not st.session_state.thought_log:
        st.info("Your journal is empty. Visit the Thought Reframing page to add entries.")
    else:
        for i, entry in enumerate(st.session_state.thought_log):
            with st.expander(f"Journal Entry {i+1}"):
                st.markdown("**Original thought:**")
                st.markdown(f"*{entry['original']}*")
                st.markdown("**Reframed thought:**")
                st.markdown(f"*{entry['reframed']}*")
    
    st.markdown("""
    ### Reviewing your journal can help you:
    
    * Recognize patterns in your overthinking
    * Remember that you can shift your perspective
    * See your growth over time
    * Build confidence in your ability to manage difficult thoughts
    """)
