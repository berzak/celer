**`participant_metadata/`**

- `metadata.tsv` Several missing values for Gender and Age.
- `test_scores/michigan/item-scores-MichiganLG` 5 missing values for MichiganLG answers (counted as incorrect answers). These occured at an early stage of the experiment when it was possible to submit the test without answering all the questions.

**`data_[version]`**

*v1 issues*
- In v1, when failed to fixate on "Q" target (preceding the presentation of the question) recalibration is triggered and the entire trial is repeated. As a result, in trials where this happened the sentence was read more than once. In such cases, in the eye-tracking reports we have only the first presentation of the sentence (and discard subsequent presentations). This issue was fixed for participants new to v2, where recalibration occurs only on sentence triggers. See [programs.md](documentation/EB_programs) for further changes between versions 1 and 2.

*v2 issues*
- The following lists (from the program BLLIP_265_324_Tower) have each a trial in the individual portion that was removed because the sentence was accidentally replaced with #NAME? in the data file (the data file was passed through excel for this batch).
    - list 231 trial 41
    - list 267 trial 55
    - list 268 trial 94
    - list 279 trial 30
    - list 281 trial 116
    - list 305 trial 28
    - list 308 trial 153
    
- Differently from the PTB sentences which are available in raw form, BLLIP materials had to be detokenized. This was done heuristicaly and unfortunately resulted in seveal issues.
    - "'d" apppearing as a separate token (e.g. "I 'd" instead of "I'd"). 66 cases.
    - "cann't" instead of "can't". 1249 cases.
    - opening single quotes are attached to the preceding word (e.g. "It's called' eyetracking'.", instead of "It's called 'eyetracking'.")
Note that the ngram and LSTM language models are trained on a versions of the BLLIP sentences in which these issues were fixed.

*missing trials*
- The following lists have a missing trial because the participant pressed on the proceed button before reading the sentence.
    - list 37 trial 45
    - list 89 trial 10
    - list 127 trial 27
    - list 169 trial 1
    - list 178 trial 1
    - list 183 trial 1
    - list 277 trial 40
    - list 289 trial 47
    - list 308 trial 138
    - list 317 trial 106
    - list 355 trial 141
