## Participant Metadata Variables

`participant_metadata/metadata.tsv` 

- `List` Experimental list.
- `Data Version` Dataset version in which the participants was first included.
- `Dominant Eye` The dominant eye of the participant. In the large majority of cases this is also the tracked eye.
- `Program` DataViewer program folder. 
- `L1` Native language.
- `Age` Age.
- `Gender` Gender: male / female / other.
- `Education` Level of education: primary / secondary / university.
- `Age Learned English` Age at which the participant started learning English.
- `English Speaking Countries` English speaking countries in which the participant lived, and for how long.
- `Languages` Languages spoken other than English.   
  - `Language` Language name.
  - `Dialect` Dialect or country.
  - `Years Learning` Number of years learning and/or using the the language.
  - `Proficiency` self assessed proficiency level: beginner / intermediate / advanced / native.
Michigan Placement Test (MPT, Form B) taken in lab.  
- `MichiganLG` Listening and Grammar sections of the MPT (score range 0-50).
- `MichiganVR` Vocabulary and Reading comprehension sections of the MPT (score range 0-50). Available for most participants new to v2.
Latest official standardized English test taken  
- `Test` Name of the test.
- `Years Ago` How many years ago was the test taken.
- `Score` Overall score.
- `Reading`, `Listening`, `Speaking`, `Writing` Individual test section scores.
- `TOEFL-IBT-Converted` Score converted to TOEFL-IBT scale (0-120). Currently available only for TOEIC. The `test_scores/test_convetion.tsv` can be used to convert scores from other tests.
- `TOEFL-IBT-Comprehension` Listening + Reading sections of TOEFL-IBT (0-60). If section scores are not available, approximated as TOEFL-IBT-Converted / 2.