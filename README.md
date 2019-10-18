# phong_lighting
A simple parser and renderer for stanford polygon format files to render in opengl with python, using custom shaders (the most complicated shader included being a Phong Lighting shader).

*NOTE*
This program is written in python 3.6. To run main.py you will first need to install OpenGLContext.
The current pip installation of OpenGLContext does not currently suport python 3.6
Downlaod and install the patch from https://github.com/mckenn0n/OpenGLContext_python3.6_compatable

---How to run---

### Requires
* Parse
* OpenGL
* pygame

Run (cow):

	python3 main.py model0.ply

Run (text):
	
	python3 main.py model1.ply

Run (teapot):
	
	python3 main.py teapot.ply

Enter the name of the vertext shader you would like to use.

Enter the name of the fragment shader you would like to use.

------

Included Vertex Shaders:
	vert.glsl (Phong)
	test_vert.glsl
	pris_vert.glsl

Included Fragment Shaders:
	frag.glsl (Phong)
	test_frag.glsl
	pris_vert.glsl


Add another shader:

To add another shader, simply add the TWO glsl files to the shader directory.


Add another model:

To add a model, simply add the .ply file into the model directory.


Draw outlines:

To draw an outline around the model (make all edges white), press SPACE.


Quit:

Click the x or press ESC.


Rotation:

By default the model will rotate around the x-axis. Pressing p, UP_ARROW, DOWN_ARROW, RIGHT_ARROW, or LEFT_ARROW changes this behavior.

p - Pressing p will stop and start the auto rotation.

UP_ARROW - Holding this key will rotate the model about the y-axis. The model will appear to rotate upwards.

DOWN_ARROW - Holding this key will rotate the model about the y-axis. The model will appear to rotate down.

RIGHT_ARROW - Holding this key will rotate the model about the x-axis. The model will appear to rotate to the right.

LEFT_ARROW - Holding this key will rotate the model about the x-axis. The model will appear to rotate to the left.
