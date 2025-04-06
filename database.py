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