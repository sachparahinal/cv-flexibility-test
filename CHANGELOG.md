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

## [March 3, 2026] - Hinal Sachpara

### Fixed
- **Tkinter Kernel Crash:** Replaced get_user_info() Tkinter dialog with simple input() prompts
  - Root Cause: NSApplication selector crash when called from Jupyter background thread on Mac
  - Fix: Replaced user_name, user_age = get_user_info() with input() prompts in main()
  - Impact: Eliminates kernel crash, test now runs end-to-end successfully

- **Import Error (cv2 not defined):** Documented correct cell execution order
  - Root Cause: Cell 1 (imports) was skipped before Cell 21 (main)
  - Fix: Run cells in order: 0, 1, 2, 4, 9-16, 18, 23, 21

- **Audio Path:** Fixed hardcoded absolute path in Cell 4
  - Before: sys.path.append('/Users/hinalsachpara/Desktop/CO-OP Docs/...')
  - After: sys.path.append('.') — works on any computer

### Added
- **Full End-to-End Test Verified:** Complete test run confirmed working
  - Result: "TEST COMPLETE!" with real measurement (Right leg: 7.6 in short of toes)
  - All 7 stages passed: FULL_BODY_DETECTION → SITTING_CHECK → FOOT_FLAT_CHECK → LEG_EXTENDED_CHECK → HANDS_POSITION_CHECK → FORWARD_REACH → MEASUREMENT
  - Countdown working: 3-2-1-GO audio and visual overlay confirmed

- **New MP3 Audio Files:** Created additional instruction audio files
  - instruction_hands.mp3, instruction_reach.mp3, instruction_complete.mp3
  - Total: 11 MP3s in /audio/ directory

- **.gitignore:** Added to prevent junk files from being tracked

- **Git Config:** Set global user name and email for clean commit attribution

### GitHub Commits
- 006ddc2 — Fix Tkinter crash, full test working
- 3faa12b — Add .gitignore

### To Do (Next Steps)
- [ ] Create instruction_fullbody.mp3 and instruction_foot.mp3
- [ ] Update tts_system to load all new MP3 files
- [ ] Map all 9 states to correct audio keys in Cell 21
- [ ] Test full run with audio at every stage
- [ ] Push final audio changes to GitHub

## [March 11-12, 2026] - Hinal Sachpara

### Added

- **Two-Screen Instruction Flow** — `show_instruction_screen()` — Step 15
  - Screen 1: Text instructions (6 steps) on white background with styled title and footer bar. Stays for 15 seconds or until any key is pressed.
  - Screen 2: Visual image guide (`merged_instruction.png`) for 5 seconds or until any key is pressed.
  - Image path uses `os.getcwd()` to find file automatically in notebook folder, with hardcoded fallback path — works on any computer.
  - Function is called BEFORE `cap = cv2.VideoCapture(0)` — camera does not open until instructions fully complete.
  - `cv2.destroyAllWindows()` + `time.sleep(1.0)` added at end to cleanly close instruction window before camera opens.

- **Error Detection System** — `show_error_message()` — Step 16
  Error messages implemented for all test states shown as a full-width red bar at top of screen:
  - No body detected: `"No body detected! Please step into the camera frame."`
  - FULL_BODY_DETECTION: `"Adjust camera! Make sure your full body is visible."`
  - SITTING_CHECK: `"Wrong position! Please sit on the edge of the chair."`
  - FOOT_FLAT_CHECK: `"Place one foot flat on the floor!"`
  - LEG_EXTENDED_CHECK: `"Extend your leg straight forward!"`
  - HANDS_POSITION_CHECK: `"Place one hand on top of the other!"`
  - FORWARD_REACH: `"Exhale and reach forward toward your toes!"`

- **30-Second Test Timer**
  - Starts when GO! countdown completes.
  - Displays `Time: Xs` at bottom center of screen, counting down from 30 to 0.
  - Green color for 30–10 seconds, switches to red for final 10 seconds.
  - Rendered inside a black background bar for readability on any camera background.

- **End Screen / Result Screen** — `show_result_screen()` — Step 17
  - **Trigger 1:** Fires automatically when `TestState.COMPLETE` is reached (state machine finishes all 9 stages)
  - **Trigger 2:** Fires when 30-second timer hits 0 (safety net if user doesn't complete all states)
  - **Background:** Freezes last live camera frame, applies Gaussian blur `(55,55)` with 65% dark overlay
  - **Layout:** Navy blue header banner, "TEST COMPLETE" label, semi-transparent result card, bottom exit bar
  - **Result Card:** Displays `line1` (measurement in inches, cyan) and `line2` (flexibility feedback, green)
  - **Animation:** 3-pulse green border on entry, then waits for any keypress to exit cleanly
  - **Reset support:** `r` key resets `result_screen_shown = False` so a fresh run works correctly

- **`last_good_frame` tracking in `main()`:** Every frame is copied so result screen always has a fresh frozen image available
- **`result_screen_shown` flag in `main()`:** Prevents result screen from triggering more than once per run

### Changed

- **Removed Name/Age Input Entirely**
  - Removed `get_user_info()` and all `input()` prompts from `main()`.
  - Test now runs fully automatically with no terminal interaction required.

- **Countdown Speed:** Each number now displays for 1.5 seconds (was 1.0 second).

- **Countdown Font:** Increased to size 5, thickness 6 — large centered green text over camera feed.

- **UI Layout — Separated Screen Zones to prevent overlap:**

  | Element | Position |
  |---|---|
  | Warning message | Very top — full width red bar |
  | Instruction text | Top center — black background bar |
  | Status message | Below instruction — centered |
  | Camera feed | Middle of screen |
  | 30-second timer | Bottom center — black background bar |

- **`main()` updated (STEP 18):** Added 4 changes — two new variables, two result screen triggers, and reset flag
- **Cell order renumbered:** `show_result_screen()` inserted as STEP 17, `main()` moved to STEP 18

### Problems Encountered

- **Problem:** Text instruction screen was not showing — app went straight to the image.
  - **Root Cause:** `cv2.waitKey(5000)` does not work on Mac because OpenCV windows do not receive keyboard focus before the timeout fires.
  - **Fix:** Replaced with `while time.time() - start < 15.0: cv2.waitKey(1)` loop — works on Mac, Windows, and Linux.

- **Problem:** Image screen was stuck and would not advance to the countdown.
  - **Root Cause:** Same Mac focus issue with `cv2.waitKey(3000)`.
  - **Fix:** Same loop-based timing approach with key press OR timeout.

- **Problem:** Audio countdown started playing during the image screen. Then when image closed, the visual countdown started from 3 again — completely out of sync.
  - **Root Cause:** `cap = cv2.VideoCapture(0)` was being called before `show_instruction_screen()`, so the countdown loop was already running in the background while instructions were still displayed.
  - **Fix:** Moved camera open to AFTER `show_instruction_screen()` returns. Added `cv2.waitKey(1)` to render the first frame before audio plays, plus `time.sleep(0.5)` buffer before `tts_system.play_audio()`.

- **Problem:** Name/age `input()` prompt appeared in the Python terminal mid-flow after the countdown, forcing the user to switch back to the terminal to enter details before the test could begin.
  - **Root Cause:** `get_user_info()` was being called inside `main()` after the camera opened.
  - **Fix:** Removed name/age input entirely — test runs automatically with no terminal interaction.

- **Problem:** `IndentationError: unindent does not match any outer indentation level` on `time.sleep()` line.
  - **Root Cause:** Mixed tabs and spaces in the Jupyter cell.
  - **Fix:** Deleted the line and retyped it with consistent 4-space indentation.

- **Problem:** Instruction text was getting cut off on the right side of the screen — last few words of each line were missing.
  - **Root Cause:** Font size 3.0 was too large causing text to overflow the window width.
  - **Fix:** Reduced to size 1.5 with dynamic centering using `cv2.getTextSize()`.

- **Problem:** Instructions 5 and 6 were not visible — cut off at the bottom of the screen.
  - **Root Cause:** Font size 2.2 with 120px line spacing caused the last two lines to fall below the 720px window height.
  - **Fix:** Reverted to original font size 1.1 with 80px line spacing.

- **Problem:** Warning message, instruction text, and status text were all overlapping in the top corner.
  - **Root Cause:** All three elements were rendering at the same y-coordinates (0–120px).
  - **Fix:** Redesigned layout with dedicated zones — warning at y=0–75, instruction at y=80–130, status at y=135–180, timer at bottom.

- **Problem:** Step 6 in the instruction image was missing its label text ("6. Hold the position").
  - **Root Cause:** When merging Image 1 and Image 2, the crop coordinates overlapped with the text label area, causing the illustration from Image 2 to cover it.
  - **Fix:** After multiple merge attempts, decided to use Image 1 as the final `merged_instruction.png` — all 6 labels are clearly visible with consistent illustrations.

- **Problem:** Confusion on where to paste code for result screen — provided as individual snippets causing confusion on exact placement inside existing function.
  - **Fix:** Rewrote and provided the entire `main()` cell as one complete block to replace, with syntax verified via Python `ast.parse()` before handing over.

- **Problem:** Cell numbering conflict — adding `show_result_screen()` as a new cell before `main()` shifted the step numbers.
  - **Fix:** Confirmed correct final order: STEP 15 (instructions) → STEP 16 (error message) → STEP 17 (result screen) → STEP 18 (main).

### To Do (Next Steps)
- [ ] Create missing audio files: `instruction_fullbody.mp3`, `instruction_foot.mp3`
- [ ] Update `tts_system` to load all new MP3 files
- [ ] Map all 9 states to correct audio keys in STEP 18 `main()`
- [ ] Test full run with audio playing at every stage
- [ ] Push final changes to GitHub
