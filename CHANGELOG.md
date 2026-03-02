# Changelog - Chair Sit-and-Reach Flexibility Test

## [February 11, 2026] - Hinal Sachpara

### Changed
- **Leg Extension Threshold:** Updated `ANGLE_THRESHOLD` from 80° to 155°
  - **Rationale:** The previous 80° threshold was too permissive and allowed significantly bent knees to pass validation. A straight leg should be approximately 160-180°. The new 155° threshold ensures proper leg extension per Rikli & Jones protocol requirements.
  - **File modified:** `chair_sit_and_reach_final_working_Hinal.ipynb`
  - **Function:** `check_leg_extended()`
  - **Impact:** High - Ensures measurement validity by requiring proper leg positioning

### To Do (Next Steps)
- [ ] TTS replacement research (pyttsx3 vs gTTS vs Web Speech API)
- [ ] Implement cross-platform TTS
- [ ] Add foot dorsiflexion validation (90° angle check)
- [ ] Enhance hand position check (vertical stacking verification)

## [February 18, 2026] - Hinal Sachpara

### Added
- **Complete TTS Implementation:** Full MP3-based text-to-speech system
  - **Countdown Audio:** 3.mp3, 2.mp3, 1.mp3, go.mp3 (TTSMaker neural voice)
  - **Instruction Audio:** instruction_sit.mp3, instruction_extend.mp3, instruction_hold.mp3, instruction_relax.mp3
  - **Voice Quality:** Consistent American female voice throughout (soft, natural)
  - **Cross-platform:** Pure MP3 playback works on Mac/Windows/Linux
  - **Storage:** 92KB total (well under 100KB requirement)
  - **Cost:** $0 (100% free solution)
  - **File:** tts_final.py (complete implementation)
  - **Testing:** Successfully tested and verified working
  - **Impact:** Eliminates win32com.client dependency, enables web deployment

### Changed
- **TTS Architecture:** Moved from hybrid (pyttsx3 + MP3) to pure MP3 system
  - **Rationale:** Better voice consistency, eliminates audio routing issues, universal compatibility
  - **Benefit:** Same beautiful voice for countdown and instructions

## [February 19, 2026] - Hinal Sachpara

### Added
- **Complete TTS Integration into Main Notebook:** Successfully integrated cross-platform MP3 TTS system
  - **Replaced:** Windows-only win32com.client SpeechManager with FullMP3TTS class
  - **Integration:** Imported tts_final.py into chair_sit_and_reach_final_working_Hinal.ipynb
  - **Testing:** Confirmed TTS system loads and functions correctly in notebook environment
  - **Audio Verification:** All MP3 files (3.mp3, 2.mp3, 1.mp3, go.mp3) playing successfully

- **Video Countdown Integration Logic:** Implemented countdown display system for camera feed
  - **Countdown Variables:** Added countdown_phase, countdown_start_time, countdown_step to main() function
  - **Visual Display:** Created countdown text overlay logic with green text (matching demo requirements)
  - **Audio Synchronization:** Integrated MP3 playback with visual countdown timing
  - **Phase Management:** Added countdown phase before existing flexibility test phases

### Changed
- **TTS Architecture:** Migrated from Windows-specific to cross-platform audio system
  - **Function Replacement:** Updated speak() function to use FullMP3TTS instead of SpeechManager
  - **Dependency Removal:** Eliminated win32com.client requirement
  - **Compatibility:** Enabled Mac and Windows operation with same codebase
