# CELER: Corpus of Eye movements in Learner and native English Reading

Eye movement recordings of ESL and native English speakers reading Wall Street Journal (WSJ) newswire sentences in English. Each participant reads 156 sentences: 78 sentences shared across participants and 78 unique to each participant. The dataset has two versions v1 (182 participants) and v2 (365 participants).

### Example

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
2. - Copy the `README` file of the PTB-WSJ (starts with "This is the Penn Treebank Project: Release 2 ...") to the folder `ptb_bllip_readmes/PTB/`. 
   - Copy the `README.1st` file of BLLIP (starts with "File:  README.1st ...") to the folder `ptb_bllip_readmes/BLLIP/`
3. Run `python obtain_data.py`. This will download a zipped `data_[version]/` data folder. Extract to the top level of this directory. By default, the script will download v2.0 of the data. To obtain v1.0 run `python obtain_data.py --release v1.0`


<a name="statistics">

## Statistics

</a>

|         |v1            |          |          | v2           |           |        |
| ---     | ---          | ---      | ---      | ---          | ---       | ---    |
|         | Participants | Sentences| Words    | Participants | Sentences | Words  |
| Native  | 37           |  2,964   |   33,519 |  69          | 5,460     | 61,272 |
| ESL     | 145          |  11,388  |  129,892 |  296         | 23,166    | 260,888|
| Total   | 182          |  14,274  | 162,511  |  365         | 28,548    | 321,260 |

<a name="files">

## Directory Structure 

</a>

**`data_[version]/`**

SR DataViewer Interest Area and Fixation Reports, and syntactic annotations. 

- `sent_ia.tsv` Interest Area report.  
- `sent_fix.tsv` Fixations report. 
- `annotations/` Syntactic annotations.

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

**`dataset_analyses.Rmd`**

Analyses for the paper "CELER: A 365 Participants Corpus of Eye Movements in Learner and Native English Reading".
Note that this script requires:
- CELER (in the folder `data_[version]/`) and, 
- GECO Augmented (in the folder `geco/`). Download GECO augmented with frequency and surprisal values from the following url and place `geco/` at the top level of this directory https://drive.google.com/file/d/1sxj21lVdAEmzaM_u8ESuKceLxwOcHUpL/view?usp=sharing
See further documentation in [GECO Augmented](documentation/geco_augmented.md))

## Additional Documentation

</a>

- [Eyetracking Variables](documentation/data_variables.md) Description of the variables in the fixations and interest area reports.
- [Metadata Variables](documentation/metadata_variables.md) Description of the variables in the participants metadata file.
- [Language Models](documentation/language_models.md) Details on langugae models from which surprisal values are extracted.
- [Syntactic Annotations](documentation/syntactic_annotations.md) Details on syntactic annotations (POS, phrase structure trees, dependency trees).
- [GECO Augmented](documentation/geco_augmented.md) Details on new fields added to GECO.
- [Known Issues.md](documentation/known_issues.md) Known issues with the dataset.
