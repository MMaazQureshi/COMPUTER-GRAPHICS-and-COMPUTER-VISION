import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos
# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# Configure the OpenGL context.
# If we are planning to use anything above 2.1 we must at least
# request a 3.3 core context to make this work across platforms.
# glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
# glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
# glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
# glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
# # 4 MSAA is a good default with wide support
# glfw.window_hint(glfw.SAMPLES, 4)

# creating the window
window = glfw.create_window(1000, 600, "My OpenGL window", None, None)
# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# Query the actual framebuffer size so we can set the right viewport later
# -> glViewport(0, 0, framebuffer_size[0], framebuffer_size[1])
framebuffer_size = glfw.get_framebuffer_size(window)

# set window's position
# glfw.set_window_pos(window, 400, 200)
glfw.set_window_pos(window, 190, 70)

# make the context current
glfw.make_context_current(window)

glClearColor(0, 0.1, 0.1, 1)
vertices = [-0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0,  0.5, 0.0]

colors = [1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 0.0, 1.0]
vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)
# the main application loop
glEnableClientState(GL_VERTEX_ARRAY)  # this Enable or disable an array
glVertexPointer(3, GL_FLOAT, 0, vertices)
glEnableClientState(GL_COLOR_ARRAY)  # this Enable or disable an array
glColorPointer(3, GL_FLOAT, 0, colors)


while not glfw.window_should_close(window):
    glfw.poll_events()
    glfw.swap_buffers(window)
    glClear(GL_COLOR_BUFFER_BIT)
    ct = glfw.get_time()  # returns elapsed since init was called
    glLoadIdentity()  # loads identity matrix
    glScale(abs(sin(ct)), abs(sin(ct)), 1)
    glRotatef(sin(ct)*45, 0, 0, 1)
    glTranslatef(sin(ct), cos(ct), 0)
    # glRotatef(0.3, 1, 0, 0)
    # ACTUALLY DRAWA ARRAY PARAM: primitive type,starting index of array,number of vertices to render
    glDrawArrays(GL_TRIANGLES, 0, 3)
# terminate glfw, free up allocated resources
glfw.terminate()
