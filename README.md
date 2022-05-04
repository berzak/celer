# CELER: A 365-Participant Corpus of Eye Movements in L1 and L2 English Reading

Eye movement recordings of 69 native English speakers and 296 English learners reading Wall Street Journal (WSJ) newswire sentences. Each participant reads 156 sentences: 78 sentences shared across participants and 78 unique to each participant.

### Example

![](full_trial.gif)


## Table of Contents

1. [Obtaining the Eye-tracking Data](#obtaining)    
2. [Statistics](#statistics)  
3. [Directory Structure](#files)
4. [Additional Documentation](#docs)
5. [Citation](#cite)

<a name="obtaining">

## Obtaining the Eye-tracking Data 

</a>

The eyetracking data is not made directly available due to licensing restictions of the Penn Treebank (PTB) and the BLLIP datasets from which the reading materials are drawn. In order to obtain the data with the underlying texts please follow these instructions (require Python 3).

1. Obtain the [PTB-WSJ](https://catalog.ldc.upenn.edu/LDC95T7) and [BLLIP](https://catalog.ldc.upenn.edu/LDC2000T43) corpora through LDC.
2. - Copy the `README` file of the PTB-WSJ (starts with "This is the Penn Treebank Project: Release 2 ...") to the folder `ptb_bllip_readmes/`. 
   - Copy the `README.1st` file of BLLIP (starts with "File:  README.1st ...") to the folder `ptb_bllip_readmes/`.
3. Run `python obtain_data.py`. This will download a zipped `data_v2.0/` data folder. Extract to the top level of this directory.

<a name="statistics">

## Statistics (v2.0)

</a>

|         | Participants | Sentences | Words   |
| ---     | ---          | ---       | ---     |
| Native  | 69           | 5,460     | 61,272  |
| ESL     | 296          | 23,166    | 260,888 |
| Total   | 365          | 28,548    | 321,260 |

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
- `languages.tsv` information on languages spoken besides English.
- `test_scores/`
    - `test_conversion.tsv` unofficial conversion table between standardized proficiency tests (used to convert TOEIC to TOEFL scores).
    - `michigan-cefr.tsv` conversion table between form B and the newer forms D/E/F, as well as to CEFR levels.
    - `michigan/` item level responses for the Michigan Placement Test (MPT).   
    - `comprehension/` item level responses for the reading comprehension during the eyetracking experiment.  

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

Analyses for the paper "CELER: A 365-Participant Corpus of Eye Movements in L1 and L2 English Reading".
Note that this script requires:
- CELER (in the folder `data_v2.0/`) and, 
- GECO Augmented (in the folder `geco/`). Download [GECO augmented](https://drive.google.com/file/d/1T4qgbwPkdzYmTvIqMUGJlvY-v22Ifinx/view?usp=sharing) with frequency and surprisal values and place `geco/` at the top level of this directory.

## Documentation

</a>

- [Eyetracking Variables](documentation/data_variables.md) Description of the variables in the fixations and interest area reports.
- [Metadata Variables](documentation/metadata_variables.md) Description of the variables in the participants metadata and languages files.
- [Language Models](documentation/language_models.md) Details on language models for surprisal values.
- [Syntactic Annotations](documentation/syntactic_annotations.md) Details on syntactic annotations (POS, phrase structure trees, dependency trees).
- [GECO Augmented](documentation/geco_augmented.md) Details on new fields added to GECO.
- [Experiment Builder Programs](documentation/EB_programs.md) Information on the EB experiment.
- [Known Issues](documentation/known_issues.md) Known issues with the dataset.

<a name="cite">

## Citation
Paper: [CELER: A 365-Participant Corpus of Eye Movements in L1 and L2 English Reading](https://direct.mit.edu/opmi/article/doi/10.1162/opmi_a_00054/110717/CELER-A-365-Participant-Corpus-of-Eye-Movements-in)
   
```
@article{celer2022,
    author = {Berzak, Yevgeni and Nakamura, Chie and Smith, Amelia and Weng, Emily and Katz, Boris and Flynn, Suzanne and Levy, Roger},
    title = "{CELER: A 365-Participant Corpus of Eye Movements in L1 and L2 English Reading}",
    journal = {Open Mind},
    pages = {1-10},
    year = {2022},
    month = {04},
    issn = {2470-2986},
    doi = {10.1162/opmi_a_00054},
    url = {https://doi.org/10.1162/opmi\_a\_00054},
    eprint = {https://direct.mit.edu/opmi/article-pdf/doi/10.1162/opmi\_a\_00054/2012324/opmi\_a\_00054.pdf},
}
```

## License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work, with the exception of the underlying PTB-WSJ and BLLIP texts, is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

</a>
