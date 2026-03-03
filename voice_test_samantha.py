import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Try Samantha (ID 132) - more reliable on Mac
engine.setProperty('voice', voices[132].id)

print("Testing Samantha voice...")
engine.say("Hello, I am Samantha. Can you hear me?")
engine.runAndWait()
print("Test complete!")
