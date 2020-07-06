The experiment was deployed in SR Experiment Builder, in several EB project batches described here.
The EB folders are available upon request.

## v1
| Program | participants |
| --- | --- |
| PTB-FINAL-FINAL | 8 |
| PTB-184-18 | 4 |
| PTB-FINAL | 5 |
| PTB-TESTING | 165 |
| Total | 182 |

Notes:

1. There are some minor differences in between these programs, in particular in the size of the fixation points and the required fixation duration for triggering the text (300ms vs 250ms).
2. Interest Area segmentation was not set correctly in these programs, resulting in interest area boundaries that are only approximately in the middle of the space between two words. This was corrected after data collection by regenerating the interest areas with the correct segmetation setting. The issue was fixed in v2 programs.
3. Note to Data Viewer users: there are extra copies of the runtime files for participants pl2214 and cl2226 in folders jl2214 and jl2226 respectively:
participant pl2214: Dataviewer may look for runtime files in the folder jl2214 
participant cl2226: Dataviewer may look for runtime files in the folder jl2226

## v2

| Program | participants |
| --- | --- |
| BLLIP_185_294 | 71 |
| BLLIP_265_324_Tower | 56 |
| BLLIP_325_385_Tower | 56 |
| Total | 183 |

Change Log from v1:

1. The data for BLLIP_265_324_Tower and BLLIP_325_385_Tower was collected with the eyetracker in Tower mount configuration. All the other data was collected in Desktop configuration.
2. These programs use sentences from the BLLIP corpus instead of the PTB-WJS.
3. Switched screen resolution from 1024 x 768 to 2560 x 1440 (and repositioned and rescaled text accordingly)
4. Correct Interest Area segmentation (precisely in the middle of the space between two words)
5. No recalibration and trial repetition on questions if failed to fixate on "Q" - trigger times out after 4 seconds. 
This was introduced to reduce the number of recalibrations and to address an issue in v1 programs where the entire trial would repeat if recalibration was triggered after reading the sentence and before presenting the corresponding question (i.e. the sentence would be presented again).