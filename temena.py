import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backend_bases import PickEvent

tacke = []

def onclick(event):
  global tacke
  if len(tacke) < 7:
    if event.xdata is not None and event.ydata is not None:
      x, y = event.xdata, event.ydata
      tacke.append([int(x), int(y),1])
      if len(tacke) == 7:
        print(f"Odabrane su tacke: {tacke}")
        fig.canvas.mpl_disconnect(cid)



img = mpimg.imread('./kutija2.jpg')

fig, ax = plt.subplots()
ax.imshow(img)
plt.title("Odaberite redom 7 tacaka (preskocite br. 4)")
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
