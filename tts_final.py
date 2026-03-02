import pygame
import time
import os

class FullMP3TTS:
    def __init__(self):
        # Initialize pygame for MP3 playback
        pygame.mixer.init()
        
        # All audio files
        self.audio_files = {
            # Countdown
            'countdown_3': "audio/3.mp3",
            'countdown_2': "audio/2.mp3", 
            'countdown_1': "audio/1.mp3",
            'countdown_go': "audio/go.mp3",
            
            # Instructions
            'instruction_sit': "audio/instruction_sit.mp3",
            'instruction_extend': "audio/instruction_extend.mp3",
            'instruction_hold': "audio/instruction_hold.mp3",
            'instruction_relax': "audio/instruction_relax.mp3"
        }
    
    def play_audio(self, audio_key):
        """Play specific audio file"""
        try:
            audio_file = self.audio_files[audio_key]
            if os.path.exists(audio_file):
                pygame.mixer.music.load(audio_file)
                pygame.mixer.music.play()
                
                # Wait for playback to finish
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                return True
            else:
                print(f"Audio file not found: {audio_file}")
                return False
                
        except Exception as e:
            print(f"Audio playback error: {e}")
            return False
    
    def play_countdown(self):
        """Play countdown with MP3 files"""
        print("Playing countdown...")
        
        countdown_sequence = ['countdown_3', 'countdown_2', 'countdown_1', 'countdown_go']
        display_text = ['3', '2', '1', 'GO!']
        
        for i, audio_key in enumerate(countdown_sequence):
            # Visual display
            print(f"\n      {display_text[i]}")
            
            # Play audio
            self.play_audio(audio_key)
            
            # Brief pause between counts
            if i < len(countdown_sequence) - 1:
                time.sleep(0.5)
    
    def speak_instruction(self, instruction_type):
        """Speak instruction using MP3 files"""
        instruction_map = {
            'sit': 'instruction_sit',
            'extend': 'instruction_extend', 
            'hold': 'instruction_hold',
            'relax': 'instruction_relax'
        }
        
        if instruction_type in instruction_map:
            audio_key = instruction_map[instruction_type]
            print(f"Instruction: {instruction_type}")
            self.play_audio(audio_key)
        else:
            print(f"Unknown instruction: {instruction_type}")

# Test the complete MP3 system
if __name__ == "__main__":
    print("Testing Complete MP3 TTS System")
    print("=" * 40)
    
    tts = FullMP3TTS()
    
    print("\n1. Testing countdown:")
    tts.play_countdown()
    
    print("\n2. Testing instructions:")
    tts.speak_instruction('sit')
    time.sleep(1)
    tts.speak_instruction('extend')
    time.sleep(1)
    tts.speak_instruction('hold')
    time.sleep(1)
    tts.speak_instruction('relax')
    
    print("\nComplete MP3 TTS test finished!")
