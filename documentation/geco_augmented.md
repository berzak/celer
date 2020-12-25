## GECO Augmented

Files from the GECO dataset (Cop et al. 2017), dowloaded from https://expsy.ugent.be/downloads/geco/:
- `SubjectInformation.xlsx`
- `L2ReadingData.xlsx`
- `MonolingualReadingData.xlsx`

The last two files (renamed to end with `Augmented`) have the following additional fields:
- `WORD_NORM`: lowercased word, without punctuation. Numbers reprepresented as `NUM`.
- `FREQ-BLLIP`: -log2(word frequency) in BLLIP (Charniak et al. 2000).
- `FREQ-SUBTLEX`: -log2(word frequency) based on SUBTLEX-US (Brysbaert and New 2009, https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus).
- `FREQ-WEB`: -log2(word frequency) based on the kagle web word frequency list (https://www.kaggle.com/rtatman/english-word-frequency).
- `OOV-BLLIP`: 1 if the word out of vocabulary in BLLIP, 0 otherwise. BLLIP vocabulary size 229,538 words.
- `OOV-SUBTLEX`: 1 if the word out of vocabulary in SUBTLEX-US, 0 otherwise. SUBTLEX-US vocabulary size 74,286 words.
- `OOV-WEB`: 1 if the word out of vocabulary in kaggle, 0 otherwise. kaggle vocabulary size 333,332 words.
- `SURP-GPT2`: word surprisal according to the GPT2 language model (Radford et al. 2019). 

