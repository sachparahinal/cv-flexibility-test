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

## [March 17, 2026] - Hinal Sachpara

### Added
- **End Screen / Result Screen:** Built `show_result_screen()` as STEP 17
  - Frozen last camera frame as background with Gaussian blur + 65% dark overlay
  - Navy blue header, "TEST COMPLETE" label, semi-transparent result card
  - Displays measurement result (cyan) and flexibility feedback (green)
  - 3-pulse green border animation on entry, waits for any keypress to exit
  - Trigger 1: fires when `TestState.COMPLETE` is reached
  - Trigger 2: fires when 30-second timer hits 0 (safety net)
  - `result_screen_shown` flag prevents double trigger
  - `r` key reset also resets the flag

- **Pre-Countdown Full Body Detection Phase:**
  - Camera opens immediately after instruction screens
  - Shows "Position yourself fully in the camera frame" until full body detected
  - Green "Perfect! Get ready..." message for 2 seconds then countdown fires
  - `FULL_BODY_DETECTION` state removed from test loop — handled here instead

- **`HOLD_POSITION` State Wired in `main()`:**
  - Was defined in state machine but never validated
  - Reuses `check_forward_reach()` — shows "Hold still! Measuring..."
  - 2-second hold required before advancing to MEASUREMENT

- **`INHALE_PREPARATION` State Added Back:**
  - Was missing from validation block in `main()`
  - Added back using existing `check_inhale()` function

- **Visual Instruction Image Recreated:**
  - New `visual_instruction.png` with clearer step illustrations
  - Step 3 — large teal arrow clearly pointing to flat foot
  - Step 4 — hands visibly stacked on lap
  - All 6 headings aligned consistently
  - Image resized to 1280x680 leaving room for bottom bar

### Changed
- **Countdown Audio/Visual Sync Fixed:**
  - Audio was playing before number appeared on screen
  - Fixed — `play_audio()` now fires once when step starts, text drawn once per frame
  - Also fixed double-draw bug causing overlapping/garbled countdown text

- **Countdown Double-Draw Bug Fixed:**
  - Text was being drawn twice per frame causing "GetGReady" overlap and cutoff
  - Removed duplicate `putText` + `imshow` + `waitKey` calls from countdown block

- **Instruction Text Size Increased:**
  - Font scale `1.5 → 2.0`, thickness `2 → 3`
  - Banner zone expanded from `(80-130)` to `(75-145)`
  - Status message zone nudged down to `(150-195)`

- **Preview/Instruction Phase Delays Removed:**
  - Old: preview 3s + instruction 3s + hold 2s = 64s minimum per state
  - New: straight to validation immediately = ~8s total minimum
  - `HOLD_POSITION` keeps 2s hold, all other states reduced to 1s

- **`check_hands_position()` Completely Rewritten:**
  - Old 3D distance threshold `0.1` was impossible to reach (actual values 0.50-0.72)
  - Rewritten based on Rikli & Jones protocol — "middle fingers even, palms down"
  - Now checks wrist Y-diff `< 0.08`, wrist X-diff `< 0.25`, wrists below shoulders
  - 3 specific feedback messages instead of one generic message

- **`check_forward_reach()` Fixed:**
  - `below_knee` check always returned False due to side-view camera angle
  - Removed — now only checks horizontal alignment `x_diff < 0.2` with extended ankle

- **`show_instruction_screen()` Updated (STEP 15):**
  - Step order corrected to match code: foot flat (2) → extend leg (3)
  - Font size reduced `1.6 → 1.4` to prevent text cut-off on screen
  - Image filename updated from `merged_instruction.png` to `visual_instruction.png`
  - Bottom bar repositioned to `y=660` to avoid covering illustrations

- **Cell order renumbered:**
  - `show_result_screen()` inserted as STEP 17
  - `main()` moved to STEP 18
  - Duplicate `main()` cell deleted

### Problems Encountered
- **Countdown text overlapping/garbled:** Text was drawn twice per frame — once in the initialization block and again in the main loop. Fixed by removing the duplicate draw from the initialization block and keeping only the per-frame draw.
- **`check_hands_position()` never passing:** Threshold of `0.1` was physically impossible — all positions gave 0.50-0.72. Discovered through debug testing. Completely rewrote the function.
- **`check_forward_reach()` always failing:** `below_knee` check was unreliable from side-view camera angle. Confirmed via debug output showing `below_knee=False` across all 50 readings. Removed the check entirely.
- **Instruction image covering legs:** Bottom black bar at y=640 was covering the bottom row illustrations. Fixed by resizing image to 1280x680 and moving bar to y=660.

### To Do (Next Steps)
- [ ] Implement 30-second timer measurement logic (pending Sanal's reply)
- [ ] Record demo video after above 2 tasks complete

## [March 18, 2026] - Hinal Sachpara

### Added
- **Fullscreen Display:** Test window now opens in fullscreen automatically
  - Added `cv2.setWindowProperty` with `cv2.WINDOW_FULLSCREEN` in `main()`
  - Added same fullscreen property to instruction screens in `show_instruction_screen()`

### Changed
- **Result Message Wording:** Updated measurement result text for clarity
  - Before: `"Right leg: 3.9 in past toes."` — ambiguous "in"
  - After: `"Right leg: fingertips reached 3.9 inches beyond toes."` — clear and descriptive
  - Before: `"Right leg: 3.9 in short of toes."` — ambiguous "in"
  - After: `"Right leg: fingertips 3.9 inches short of toes."` — clear and descriptive

- **Instruction Screen — Fullscreen Fix:**
  - Removed keypress detection from both instruction screens — does not work in Mac fullscreen
  - Both screens now exit purely on time — 15s for text screen, 5s for image screen
  - Bottom bar text changed from `"Press any key..."` to `"Starting in 5 seconds..."` — accurate for fullscreen

- **Countdown Sync Fix:**
  - Countdown text is now drawn on frame BEFORE audio plays
  - Added `cv2.imshow` + `time.sleep(0.3)` before `play_audio()` for both first step and step changes
  - Eliminates audio playing before number appears on screen

- **Countdown Double-Draw Bug Fixed:**
  - Removed duplicate `putText` calls that caused overlapping/garbled text
  - Text is now drawn once per frame loop only

### Problems Encountered
- **Fullscreen instruction screen hanging forever:** `cv2.waitKey()` stops responding in Mac fullscreen mode — macOS won't give keyboard focus to OpenCV window. Fixed by removing all keypress detection and using time-based exit only.
- **`ccv2` typo in main():** `cv2.namedWindow` was accidentally typed as `ccv2.namedWindow` causing `NameError`. Fixed by removing the extra `c`.
- **`cv2.setWindowProperty` indentation error:** Line was placed outside `main()` function causing it to run at module level. Fixed by adding correct 4-space indentation.

### To Do (Next Steps)
- [ ] Implement 30-second timer measurement logic (pending Sanal's reply)
- [ ] Wire 9 audio instruction texts to test states
- [ ] Record demo video after above 2 tasks complete

## [March 19, 2026][time:2:30 PM] - Hinal Sachpara

### Changed
- **Result Screen — Hide Raw Inches:**
  - Raw measurement (inches) no longer displayed to user on result screen
  - Raw inches now printed to terminal only for debugging: `[DEBUG] Right leg: 3.9 inches | Category: Average`
  - Result screen now shows plain English category and motivational message only

- **measure_flexibility() — Updated Category Logic:**
  - Removed old `sit_and_reach_flexibility` variable
  - New 3-category system based on Rikli & Jones protocol:
    - Above Average: fingertips past toes by more than 4 inches
    - Average: fingertips within 4 inches either side of toes
    - Below Average: fingertips short of toes by more than 4 inches
  - New motivational messages per category:
    - Above Average: "Amazing! Your flexibility is Above Average — keep up the great work!"
    - Average: "Great effort! Your flexibility is Average — keep stretching daily to improve!"
    - Below Average: "Don't give up! Your flexibility is Below Average — daily stretching will help you improve!"

- **show_result_screen() — Updated Display:**
  - Line 1 now shows category (e.g. "Above Average") in large cyan
  - Line 2 now shows motivational message in green
  - Label changed from "Your Result:" to "Your Flexibility Result:"

### To Do (Next Steps)
- [ ] Fix timer logic — pause and reset when user breaks position (Task 6)
- [ ] UI/UX improvements after next meeting
- [ ] Wire 9 audio instruction texts to test states
- [ ] Send final update to Sanal with all changes
