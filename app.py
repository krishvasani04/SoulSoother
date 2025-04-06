import streamlit as st
import random
import datetime
from utils import get_affirmation, get_breathing_instructions
from exercises import get_grounding_exercise, get_overthinking_questions, get_reframing_exercise
from ai_helper import generate_thought_reframing, generate_custom_affirmation, generate_personalized_advice
import database as db

# Set page title using HTML (compatible with older Streamlit versions)
st.markdown("<h1 style='text-align: center'>Boopie's Calm Space 🧠</h1>", unsafe_allow_html=True)

# Custom CSS for aesthetics
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
    }
    
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        letter-spacing: 0.5px;
    }
    
    h1 {
        color: #FF4B8B;
        border-bottom: 2px solid #FFD1E0;
        padding-bottom: 10px;
    }
    
    h2 {
        color: #FF6B9D;
    }
    
    h3 {
        color: #FF8BAD;
    }
    
    .stButton>button {
        border-radius: 20px;
        border: 1px solid #FF6B9D;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(255, 107, 157, 0.2);
    }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 10px;
        border: 1px solid #FFD1E0;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border: 1px solid #FF6B9D;
        box-shadow: 0 0 5px rgba(255, 107, 157, 0.3);
    }
    
    .stProgress>div>div>div>div {
        background-color: #FF6B9D;
    }
    
    .stAlert {
        border-radius: 10px;
    }
    
    .stExpander {
        border-radius: 10px;
        border: 1px solid #FFD1E0;
    }
    
    div.stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    div.stTabs [data-baseweb="tab"] {
        border-radius: 5px 5px 0px 0px;
        padding: 10px 20px;
        background-color: #FFE6EF;
    }
    
    div.stTabs [aria-selected="true"] {
        background-color: #FF6B9D;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

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
    
    # Style the sidebar header with custom HTML
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="color: #FF4B8B; margin-bottom: 0;">Hey Boopie! 💕</h2>
        <p style="font-style: italic; color: #9D6381;">Tools for when your mind races</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add subtle spacing between buttons
    st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)
    
    # Navigation buttons with icons
    emoji_dict = {
        'home': '🏠', 
        'breathing': '🌬️', 
        'grounding': '🌿', 
        'reframing': '💭', 
        'journal': '📓'
    }
    
    button_names = ['Home', 'Breathing Exercise', 'Grounding Exercise', 'Thought Reframing', 'Thought Journal']
    button_routes = ['home', 'breathing', 'grounding', 'reframing', 'journal']
    
    for name, route in zip(button_names, button_routes):
        # Check if this is the current page
        is_active = st.session_state.current_page == route
        
        # Different styling for active button
        if is_active:
            st.markdown(f"""
            <div style="background-color: #FFC6D9; border-radius: 15px; padding: 10px; text-align: center; margin: 5px 0;">
                <span style="color: #FF4B8B; font-weight: bold;">{emoji_dict[route]} {name}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            if st.button(f"{emoji_dict[route]} {name}", key=f"nav_{route}", 
                      use_container_width=True, on_click=navigate_to, args=(route,)):
                pass
    
    # Add a decorative divider
    st.markdown("""
    <div style="margin: 20px 0; text-align: center;">
        <div style="height: 2px; background-image: linear-gradient(to right, transparent, #FFB0EE, transparent);"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Personal touches with more elegant styling
    st.markdown(f"""
    <div style="text-align: center; background-color: #FFF0F7; border-radius: 10px; padding: 10px; margin: 10px 0;">
        <div style="font-weight: bold; color: #FF6B9D;">Bean & Boopie</div>
        <div style="font-style: italic; font-size: 0.9em;">{days_together} days of adventures together 💫</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Affirmation with prettier styling
    affirmation = get_affirmation()
    st.markdown("""
    <div style="margin: 20px 0; text-align: center;">
        <div style="height: 2px; background-image: linear-gradient(to right, transparent, #FFB0EE, transparent);"></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="font-style: italic; text-align: center; color: #FF8BAD; padding: 10px; border-radius: 10px; background-color: #FFF8FA;">
        "{affirmation}"
    </div>
    """, unsafe_allow_html=True)
    
    # Song recommendation with elegant styling
    st.markdown("""
    <div style="margin: 20px 0; text-align: center;">
        <div style="height: 2px; background-image: linear-gradient(to right, transparent, #FFB0EE, transparent);"></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; background-color: #FFF0F7; border-radius: 10px; padding: 10px; margin: 10px 0;">
        <div style="font-weight: bold; color: #FF6B9D;">When you need a smile 🎵</div>
        <div style="font-size: 0.9em; margin-top: 5px;">Listen to 'ilym' by John K</div>
        <div style="font-style: italic; font-size: 0.8em;">Or check out our 'Happy Baby' playlist 🎧</div>
    </div>
    """, unsafe_allow_html=True)

# Home page
if st.session_state.current_page == 'home':
    # Styled header with gradient
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h1 style="color: #FF4B8B; margin-bottom: 0.5rem; font-size: 2.5rem;">
            Hey Hiya! Your Calm Space Awaits 💖
        </h1>
        <div style="height: 4px; background-image: linear-gradient(to right, transparent, #FF6B9D, transparent);
                    margin: 0 auto 1rem auto; width: 70%;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Prettier welcome message with card-like styling
    st.markdown(f"""
    <div style="background-color: #FFF0F7; border-radius: 15px; padding: 20px; margin-bottom: 2rem; 
                border-left: 5px solid #FF6B9D; box-shadow: 0 4px 6px rgba(255, 107, 157, 0.1);">
        <h3 style="color: #FF4B8B; margin-top: 0;">From Bean to Boopie with love</h3>
        <p style="margin-bottom: 1rem;">
            This is a special space just for you, for those moments when your beautiful mind 
            is racing too fast. Whether you're in your studio in West Lafayette or anywhere else,
            I'm here with you in spirit.
        </p>
        <p style="font-weight: bold; color: #FF6B9D; font-size: 1.1rem;">
            How's my Boopie feeling right now?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Styled mood selection buttons
    mood_options = [
        {"title": "Anxious or worried", "icon": "😰", "color": "#8AADF4", "route": "breathing"},
        {"title": "Stuck in my thoughts", "icon": "🤔", "color": "#A6DA95", "route": "grounding"},
        {"title": "Need perspective", "icon": "🧐", "color": "#F5BDE6", "route": "reframing"}
    ]
    
    cols = st.columns(3)
    for i, option in enumerate(mood_options):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; cursor: pointer;" onclick="document.getElementById('btn_{option['route']}').click();">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{option['icon']}</div>
                <div style="background-color: {option['color']}; color: white; padding: 10px; 
                            border-radius: 10px; font-weight: bold;">
                    {option['title']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            # Hidden button for the onClick handler
            if st.button(option['title'], key=f"btn_{option['route']}", 
                      use_container_width=True, on_click=navigate_to, args=(option['route'],)):
                pass
    
    # Styled divider
    st.markdown("""
    <div style="margin: 2rem 0; text-align: center;">
        <div style="height: 2px; background-image: linear-gradient(to right, transparent, #FFB0EE, #FF6B9D, #FFB0EE, transparent);"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # AI Daily Message with card styling
    st.markdown("""
    <div style="margin-bottom: 1rem;">
        <h3 style="color: #FF4B8B; display: inline-block; margin-right: 10px;">Today's Message from Bean</h3>
        <span style="font-size: 1.5rem;">💌</span>
    </div>
    """, unsafe_allow_html=True)
    
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
        st.markdown(f"""
        <div style="background-color: #E7F5EB; border-radius: 15px; padding: 20px; margin-bottom: 1.5rem;
                    border-left: 5px solid #8BC0A8; box-shadow: 0 4px 6px rgba(139, 192, 168, 0.1);">
            <p style="font-style: italic; color: #2D7D53; margin: 0; font-size: 1.1rem;">"{today_message}"</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Creative activity suggestion with card styling
    st.markdown("""
    <div style="background-color: #FFF8E1; border-radius: 15px; padding: 20px; margin: 1.5rem 0;
                border-left: 5px solid #FFD54F; box-shadow: 0 4px 6px rgba(255, 213, 79, 0.1);">
        <h3 style="color: #E6A800; margin-top: 0;">Maybe some coloring would help? 🎨</h3>
        <p style="margin: 0;">
            I know how much you enjoy drawing and coloring when your mind is busy. 
            Maybe take out your art supplies for a bit?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Styled divider
    st.markdown("""
    <div style="margin: 2rem 0; text-align: center;">
        <div style="height: 2px; background-image: linear-gradient(to right, transparent, #FFB0EE, #FF6B9D, #FFB0EE, transparent);"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Reminders with nicer styling
    st.markdown("""
    <div style="background-color: #F0F4FF; border-radius: 15px; padding: 20px; margin-bottom: 1.5rem;
                border-left: 5px solid #8BB6FF; box-shadow: 0 4px 6px rgba(139, 182, 255, 0.1);">
        <h3 style="color: #4B77CC; margin-top: 0;">Just a few reminders from your Bean:</h3>
        <ul style="padding-left: 20px; margin-bottom: 0;">
            <li>Your thoughts are just thoughts, not reality - like how Penn State is clearly superior to Purdue 😉</li>
            <li>This moment will pass, just like our debates about you eating enough</li>
            <li>You're amazing at working through challenges (except spelling "Porsche" correctly 😘)</li>
            <li>When in doubt, hug Daisy the bunny tight!</li>
        </ul>
        <p style="margin-top: 15px; color: #4B77CC;">
            Remember our Paris dream? Balcony, bathrobes, wine, Eiffel Tower view? 
            Keep breathing, we'll get there someday. 🗼✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add direct link to AI advice
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0 1rem 0;">
        <h3 style="color: #FF4B8B; margin-bottom: 1rem;">Need Bean's advice right now?</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Get Personalized Advice", use_container_width=True, on_click=navigate_to, args=('journal',)):
            pass

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
