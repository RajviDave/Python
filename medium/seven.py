#Given
#"math": 80, "science": 90, "english": 85
#calculate average marks.

import numpy as np

marks={"math": 80, "science": 90, "english": 85}

avg=marks["math"]+marks["science"]+marks["english"] / 3
print(avg)