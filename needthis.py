import vispy
print(vispy.__version__)

from vispy import app, scene
import numpy as np

canvas = scene.SceneCanvas(title='My Scene', bgcolor='#050510', size=(900, 600), show=True)
view = canvas.central_widget.add_view()
view.camera = scene.TurntableCamera(fov=50, distance=5, elevation=20)

# --- your scene goes here ---

if __name__ == '__main__':
    app.run()