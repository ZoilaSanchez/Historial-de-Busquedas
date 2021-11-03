import pandas as pd
import matplotlib.pyplot as plt

speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
em = [2, 8, 70, 1.5, 25, 12, 28]
index = ['snail', 'pig', 'elephant',
         'rabbit', 'giraffe', 'coyote', 'horse']
df = pd.DataFrame({'speed': speed,
                   'lifespan': lifespan,
                   'em': em}, index=index)


axes = df.plot.bar(rot=0, subplots=True)
axes[1].legend(loc=3)

plt.show()