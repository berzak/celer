## Interest Area and Fixation Reports Variables 

Interest Period (IP) for sentence reading: start message "DISPLAY_SENTENCE" (-2ms), end message "KEYBOARD_SENTENCE".     

### Custom Variables
- `list`: experimental list number.
- `dataset_version`: the dataset version in which the subject was first introduced.
- `trial`: trial number (2-156).
- `shared_text`: 1 if the trial is in the Shared Text regime (appears in all the lists), 0 if it`s in the Individual Text regime (unique to current list).
- `sentenceid`: sentence identifyer. 
- `correct_answer`: the correct answer to the reading comprehension question (1 or 0).
- `key_pressed`: participant`s answer to the reading comprehension question (1 or 0).
- `answered_correctly`: whether the participant`s answer to the reading comprehension question was correct (1 if yes, 0 if no).
- `sentence`: the sentence presented in the trial.
- `question`: the reading comprehension question about the sentence.
- `FREQ-BLLIP`: -log2(word frequency) in BLLIP.
- `FREQ-SUBTLEX`: -log2(word frequency) based on SUBTLEX-US (Brysbaert and New 2009) https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus
- `OOV-BLLIP`: 1 if the word out of vocabulary in BLLIP, 0 otherwise. BLLIP vocabulary size 229,538 words.
- `OOV-SUBTLEX`: 1 if the word out of vocabulary in SUBTLEX-US, 0 otherwise. SUBTLEX-US vocabulary size 74,286 words.
- `SURP-GPT2`: word surprisal according to the GPT2 language model (off-the-shelf). 
- `SURP-LSTM`: word surprisal according to an LSTM language model trained on BLLIP.
- `SURP-KENLM`: word suprisal according to a 5-gram language model (KenLM) trained on BLLIP.
- `WORD_LEN`: word length in characters, excluding punctuation.
- `WORD_NORM`: lowercased word, without punctuation. Numbers reprepresented as `NUM`.

### Data Viewer Variables in Interest Area Reports

See Data Viewer manual for detailed descriptions.

- `DATA_FILE`
- `EYE_USED`
- `IA_DWELL_TIME`
- `IA_DWELL_TIME_%`
- `IA_FIRST_FIXATION_DURATION`
- `IA_FIRST_FIXATION_INDEX`
- `IA_FIRST_FIXATION_PREVIOUS_FIX_IA`
- `IA_FIRST_FIXATION_PREVIOUS_IAREAS`
- `IA_FIRST_FIX_PROGRESSIVE`
- `IA_FIRST_FIXATION_RUN_INDEX`
- `IA_FIRST_FIXATION_VISITED_IA_COUNT`
- `IA_FIRST_FIXATION_X`
- `IA_FIRST_RUN_DWELL_TIME`
- `IA_FIRST_RUN_FIXATION_COUNT`
- `IA_FIRST_RUN_LANDING_POSITION` - (angular distance)
- `IA_FIRST_RUN_LAUNCH_SITE`
- `IA_FIRST_SACCADE_ANGLE`
- `IA_FIXATION_COUNT`
- `IA_ID`
- `IA_LABEL`
- `IA_LEFT`
- `IA_REGRESSION_IN`
- `IA_REGRESSION_IN_COUNT`
- `IA_REGRESSION_OUT`
- `IA_REGRESSION_OUT_COUNT`
- `IA_REGRESSION_OUT_FULL`
- `IA_REGRESSION_OUT_FULL_COUNT`
- `IA_REGRESSION_PATH_DURATION`
- `IA_RIGHT`
- `IA_RUN_COUNT`
- `IA_SKIP`
- `IP_START_TIME`
- `IP_END_TIME`
- `TRIAL_FIXATION_COUNT`
- `TRIAL_DWELL_TIME`
- `TRIAL_IA_COUNT`

### Data Viewer Variables in Fixation Reports

- `CURRENT_FIX_BLINK_AROUND`
- `CURRENT_FIX_DURATION`
- `CURRENT_FIX_INDEX`
- `CURRENT_FIX_INTEREST_AREA_DWELL_TIME`
- `CURRENT_FIX_INTEREST_AREA_FIX_COUNT`
- `CURRENT_FIX_INTEREST_AREA_ID`
- `CURRENT_FIX_INTEREST_AREA_LABEL`
- `CURRENT_FIX_INTEREST_AREA_LEFT` : derived from CURRENT_FIX_INTEREST_AREA_DATA
- `CURRENT_FIX_INTEREST_AREA_NEAREST_INTEREST_AREA`
- `CURRENT_FIX_INTEREST_AREA_NEAREST_INTEREST_AREA_DISTANCE`
- `CURRENT_FIX_INTEREST_AREA_NEAREST_INTEREST_AREA_LABEL`
- `CURRENT_FIX_INTEREST_AREA_RIGHT`: derived from CURRENT_FIX_INTEREST_AREA_DATA
- `CURRENT_FIX_INTEREST_AREA_RUN_ID`
- `CURRENT_FIX_PUPIL`
- `CURRENT_FIX_X`
- `CURRENT_FIX_Y`
- `DATA_FILE`
- `EYE_USED`
- `NEXT_FIX_INTEREST_AREA_ID`
- `NEXT_FIX_INTEREST_AREA_LABEL`
- `NEXT_SAC_AMPLITUDE`
- `NEXT_SAC_AVG_VELOCITY`
- `NEXT_SAC_DIRECTION`
- `NEXT_SAC_DURATION`
- `NEXT_SAC_END_X`
- `NEXT_SAC_INDEX`
- `NEXT_SAC_PEAK_VELOCITY`
- `NEXT_SAC_START_X`
- `PREVIOUS_FIX_INTEREST_AREA_ID`
- `PREVIOUS_FIX_INTEREST_AREA_LABEL`
- `PREVIOUS_SAC_AMPLITUDE`
- `PREVIOUS_SAC_AVG_VELOCITY`
- `PREVIOUS_SAC_DIRECTION`
- `PREVIOUS_SAC_DURATION`
- `PREVIOUS_SAC_END_X`
- `PREVIOUS_SAC_INDEX`
- `PREVIOUS_SAC_PEAK_VELOCITY`
- `PREVIOUS_SAC_START_X`