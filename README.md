pitchfork_visualization
=======================

An animated visualization that shows all the perturbed and unperturbed
bifurcation diagrams of the pitchfork.

Specifically, a visualization of the bifurcation diagrams of a universal unfolding of the pitchfork
bifurcation:

         G(x,lambda; alpha) = x^3 + lambda*x + alpha_1*x^2 - alpha_2

where dx/dt + G(x, lambda; alpha) = 0, lambda is the main parameter, and
alpha_1 and alpha_2 are auxiliary parameters.

projectStateFile
----------------

This is a ParaView state file. When paraview prompts you for the filename
for it XMLRectilinearGridReader, choose pitchforkMesh.vtr.

finalReport.pdf
---------------

This is the report I handed in for my Scientific Visualization class. It
could help in understanding some of the theory. The mathematics is based
off the work of Martin Golubitsky and David Schaeffer in "Singularities
and Groups in Bifurcation Theory".


pitchfork_mesh_generator.py
---------------------------

This is a python file that generates the dataset, pitchforkMesh.vtr. See
the docstring for further details.

To run this, you need the external libraries PyEVTK and NumPy. These can be downloaded
at the following links:

Numpy - http://sourceforge.net/projects/numpy/files/

PyEVTK - https://bitbucket.org/pauloh/pyevtk


pitchforkMesh.vtr
-----------------

This is the dataset. It is meant to be loaded into ParaView.


visualization_animation.dvi
----------------------------

This an animation showing the final visualization at 5 frames per second.

It's rather limited as it's only 1 camera angle, but it could be useful if you don't have ParaView
installed.
