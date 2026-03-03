import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Set Flo voice (ID 34)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[34].id)

# Test phrases
test_phrases = [
    "Hello, I am Flo, your flexibility test assistant.",
    "Please sit on the edge of the chair.",
    "Extend your right leg straight.",
    "Great job! Test complete."
]

print("Testing Flo voice...")
for phrase in test_phrases:
    print(f"Speaking: {phrase}")
    engine.say(phrase)
    engine.runAndWait()
    
print("Voice test complete!")

