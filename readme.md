# Data Sources
1. [PUPR Directories](https://drive.google.com/drive/folders/1ccn4SaP3iq89j6zRuxNPEMKvFkvVoTBr) - Manual annotation
1. [Crowdsensing-based Road Damage Detection Challenge (CRDDC'2022)](https://github.com/sekilab/RoadDamageDetector/tree/master)
    - Images (.jpg) and annotations (.xml) are provided for the train set. The format of annotations is the same as pascalVOC.
    - To exclude:
        - D43: Cross walk blur
        - D44: White line blur
        - D50: Utility

# Label mapping
## roboflow pupr
0: pothole<br>
1: buaya<br>
2: melintang<br>
3: memanjang<br>

## additional muha
0: retak buaya<br>
1: melintang<br>
2: memanjang<br>
3: pothole<br>

## sekilab
0: retak_memanjang<br>
1: retak_melintang<br>
2: retak_buaya<br>
3: pothole<br>

## mapping 
### (to roboflow)
from sekilab

0:3<br>
1:2<br>
2:1<br>
3:0<br>

from 

### (to sekilab)
from additional muha

0:2<br>
1:1<br>
2:0<br>
3:3<br>
