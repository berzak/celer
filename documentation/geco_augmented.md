## GECO Augmented

Files from the GECO dataset [Cop et al. 2017](https://link.springer.com/article/10.3758/s13428-016-0734-0), dowloaded from https://expsy.ugent.be/downloads/geco/:
- `SubjectInformation.xlsx`
- `L2ReadingData.xlsx`
- `MonolingualReadingData.xlsx`

The last two files (renamed to end with `Augmented`) have the following additional fields:
- `WORD_NORM` lowercased word, without punctuation. Numbers reprepresented as `NUM`.
- `WORD_LEN` word length, excluding punctuation.
- `FREQ-BLLIP` -log2(word frequency) in BLLIP (Charniak et al. 2000). BLLIP vocabulary size 229,538 words.
- `FREQ-SUBTLEX` -log2(word frequency) based on SUBTLEX-US [Brysbaert and New 2009](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus). SUBTLEX-US vocabulary size 74,286 words.
- `FREQ-WEB` -log2(word frequency) based on the [Kaggle web word frequency list](https://www.kaggle.com/rtatman/english-word-frequency). Kaggle vocabulary size 333,332 words.
- `OOV-BLLIP` 1 if the word out of vocabulary in BLLIP, 0 otherwise. 
- `OOV-SUBTLEX` 1 if the word out of vocabulary in SUBTLEX-US, 0 otherwise. 
- `OOV-WEB` 1 if the word out of vocabulary in Kaggle, 0 otherwise. 
- `SURP-GPT2` word surprisal according to the GPT2 language model [Radford et al. 2019]((http://www.persagen.com/files/misc/radford2019language.pdf)). 

