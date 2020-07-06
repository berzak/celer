# CELER: Corpus of English Learner Eye Movements in Reading

Eye movement recordings of ESL and native English speakers reading Wall Street Journal (WSJ) newswire sentences in English. Each participant reads 156 sentences: 78 sentences shared across participants and 78 unique to each participant. The dataset has two versions v1 (182 participants) and v2 (365 participants).

### Example
#TODO: replace with full trial.

![](full_trial.gif)


## Table of Contents

1. [Obtaining the Eye-tracking Data](#obtaining)    
2. [Statistics](#statistics)  
3. [Directory Structure](#files)
4. [Additional Documentation](#docs)

<a name="obtaining">

## Obtaining the Eye-tracking Data 

</a>

The eyetracking data is not made directly available due to licensing restictions of the Penn Treebank (PTB) and the BLLIP datasets from which the reading materials are drawn. In order to obtain the data with the underlying texts please follow these instructions (require Python 3).

1. Obtain the [PTB-WSJ](https://catalog.ldc.upenn.edu/LDC95T7) and [BLLIP](https://catalog.ldc.upenn.edu/LDC2000T43) corpora through LDC.
2. Copy the `README` file of the PTB-WSJ (starts with "This is the Penn Treebank Project: Release 2 ..."), and `README.1st` file of BLLIP (starts with "File:  README.1st ...") to the folder `ptb_bllip_readmes/`
3. Run `python obtain_data.py`. This will download the a zipped folder with the data.

<a name="statistics">

## Statistics

</a>

|         |Participants |       | Words (individual)| |
| ---     | ---         | ---   | ---   | ---       |
|         | v1          | v2    |   v1  | v2        |
| Native  | 37          | 69    |       |           |
| ESL     | 145         | 296   |       |           |
| Total   | 182         | 365   |       |           |

<a name="files">

## Directory Structure 

</a>

**`data_[version]/`**

SR DataViewer Interest Area and Fixation Reports for the latest release. 

- `sent_ia.tsv` Interest Area report.  
- `sent_fix.tsv` Fixations report. 

**`participant_metadata/`**

- `metadata.tsv` metadata on participants.

- `test scores/`
    - `test_conversion.tsv` unofficial conversion table between standardized proficiency tests (used to convert TOEIC to TOEFL scores).  
    - `michigan/` Item level responses for the Michigan Placement Test (MPT).   
    - `comprehension/` Item level responses for the reading comprehension during the eyetracking experiment.  

**`splits/`**

Trial and participant splits.

- `trials/`
    - `all_trials.txt` trial numbers for all the sentences (1-157).
    - `shared_trials.txt` trial numbers of the Shared Text regime.
    - `individual_trials.txt` trial number of the Individual Text regime.
- `participants/[version]/`
    - `random_order.csv` random participant order.
    - `train.csv` train participants.
    - `test.csv` test participants.

<a name="docs">

## Additional Documentation

</a>

- [eyetracking_variables.md](documentation/eyetracking_variables.md) Description of the variables in the fixations and interest area reports.
- [metadata_variables.md](documentation/metadata_variables.md) Description of the variables in the metadata file.
- [programs.md](documentation/EB_programs) Details on the Experiment Builder folders.
- [known_issues.md](documentation/known_issues.md) Known issues with the dataset.
