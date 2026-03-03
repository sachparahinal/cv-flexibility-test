import pyttsx3
import pygame
import time
import os

class HybridTTS:
    def __init__(self):
        # Initialize pyttsx3 for instructions
        self.engine = pyttsx3.init()
        self._configure_voice()
        
        # Initialize pygame for MP3 playback
        pygame.mixer.init()
        
        # Countdown files
        self.countdown_files = {
            3: "audio/3.mp3",
            2: "audio/2.mp3", 
            1: "audio/1.mp3",
            0: "audio/go.mp3"
        }
    
    def _configure_voice(self):
        """Configure American female voice for pyttsx3"""
        try:
            voices = self.engine.getProperty('voices')
            print("Available voices:")
            for i, voice in enumerate(voices):
                print(f"{i}: {voice.name}")
            
            # Try to find female English voice
            for voice in voices:
                name_lower = voice.name.lower()
                if ('female' in name_lower or 'zira' in name_lower) and \
                   ('english' in name_lower or 'en' in voice.id.lower()):
                    self.engine.setProperty('voice', voice.id)
                    print(f"Selected voice: {voice.name}")
                    return
            
            print("Using default voice")
            
        except Exception as e:
            print(f"Voice configuration error: {e}")
    
    def play_countdown(self):
        """Play countdown with MP3 files"""
        print("Playing countdown...")
        
        for count in [3, 2, 1, 0]:
            # Visual display
            if count > 0:
                print(f"\n      {count}")
            else:
                print(f"\n     GO!")
            
            # Play audio file
            try:
                audio_file = self.countdown_files[count]
                if os.path.exists(audio_file):
                    pygame.mixer.music.load(audio_file)
                    pygame.mixer.music.play()
                    
                    # Wait for playback to finish
                    while pygame.mixer.music.get_busy():
                        time.sleep(0.1)
                else:
                    print(f"Audio file not found: {audio_file}")
                    
            except Exception as e:
                print(f"Audio playback error: {e}")
            
            time.sleep(0.5)  # Brief pause between counts
    
    def speak_instruction(self, text):
        """Speak instruction using pyttsx3"""
        print(f"Instruction: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"TTS error: {e}")

# Test the hybrid TTS
if __name__ == "__main__":
    print("Testing Hybrid TTS System")
    print("=" * 30)
    
    tts = HybridTTS()
    
    print("\n1. Testing countdown (MP3 files):")
    tts.play_countdown()
    
    print("\n2. Testing instruction speech (pyttsx3):")
    tts.speak_instruction("Please sit on the edge of the chair")
    
    print("\n3. Testing another instruction:")
    tts.speak_instruction("Extend your right leg straight")
    
    print("\nTest complete!")


