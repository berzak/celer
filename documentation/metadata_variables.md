## Participant Metadata Variables

#`participant_metadata/metadata.tsv` 

- `List` experimental list (unique to each participant).
- `Dataset Version` dataset version in which the participants was first included.
- `ID` participant id.
- `Dominant Eye` the dominant eye of the participant. In nearly all cases this is also the tracked eye.
- `Program` DataViewer program folder. 
- `L1` native language (Arabic / Chinese / English / Japanese / Portuguese / Spanish).
- `L1 Variety` native language variety.
- `Age` age.
- `Gender` gender: female / male / other.
- `Education` level of education: primary / secondary / university.
- `English AoA` English Age of Acquisition. The age at which the participant started learning English.
- `English Speaking Countries` English speaking countries in which the participant lived, and for how long.
- `Languages` languages spoken other than English.   
  - `Language` language name.
  - `Dialect` dialect or country.
  - `Years Learning` number of years learning and/or using the language.
  - `Proficiency` self assessed proficiency level: beginner / intermediate / advanced / native. 
- `MichiganLG` Listening and Grammar sections of the Michigan Placement Test (MPT, Form B). Score range 0-50. Available for all ESL participants.
- `MichiganVR` Vocabulary and Reading comprehension sections of the MPT. Score range 0-50. Available for most participants new to v2.

Latest official standardized English test taken  
- `Test` name of the test.
- `Years Ago` how many years ago was the test taken.
- `Score` overall score.
- `Reading`, `Listening`, `Speaking`, `Writing` individual test section scores.
- `TOEFL-IBT-Converted` score converted to TOEFL-IBT scale (0-120). Currently available only for TOEIC. The `test_scores/test_convetion.tsv` can be used to convert scores from other tests.
- `TOEFL-IBT-Comprehension` listening + reading sections of TOEFL-IBT (0-60). If section scores are not available, they are approximated as TOEFL-IBT-Converted / 2.

#`participant_metadata/languages.tsv` 

- `List` experimental list (unique to each participant).
- `ID` participant id.
- `Language` name of the language.
- `Variety` language variety.
- `AoA` Age of Acquisition. The age at which the participant started learning the language.
- `Years` number of years learning and/or using the language.
- `Proficiency` self assessed proficiency level: beginner / intermediate / advanced / native.
