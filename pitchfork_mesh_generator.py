"""
This script creates a visualization of a universal unfolding of a pitchfork
bifurcation:

         G(x,lambda; alpha) = x^3 + lambda*x + alpha_1*x^2 - alpha_2

where dx/dt + G(x, lambda; alpha) = 0, lambda is the main parameter, and
alpha_1 and alpha_2 are auxiliary parameters.

This script will output a file pitchforkMesh.vtr. It is intended to be used in
ParaView. Steps to use the visualization in the most satisfying way are
outlined below.

To be able to run this script, you must have the EVTK package installed, which
can be found here:      https://bitbucket.org/pauloh/pyevtk/overview

The purpose of the visualization is to view all of the perturbed and
unperturbed bifurcation diagrams of the pitchfork. For the mathematical theory,
see "Singularities and Group in Bifurcation Theory" by Martin Golubitsky and
David G. Schaeffer.

Steps to create the pipeline and animation:
    1) Add a contour at G = 0. This represents the fixed points. Color it by
       stability.
    2) Create an animation with the isosurface changing from -3 to 3. This
       represents the alpha_2 pertubation parameter. Add 8 keyframes:
           time: 0     value: -3
           time: 0.1   value: -0.6
           time: 0.2   value: -0.296
           time: 0.3   value: -0.296
           time: 0.45  value: 0
           time: 0.55  value: 0
           time: 0.7   value: 0.296
           time: 0.8   value: 0.296
           time: 0.9   value: 0.6
           time: 1     value: 3
    3) Add 3 slices at (-2,0,0), (0,0,0), and (2,0,0) each with normal (1,0,0)
       to the contour.
    4) Add a tube on each slice.
    5) Add a contour to the isosurface at G_x = 0. These set of points are
       where the bifurcations occurs. Add a tube onto the contour and color it
       by a solid color; white works fine.

Steps to make an interesting visualization:
    1) Change the color map to diverging with red to blue; i.e., flip the
       default color map.
    2) Set visibility of all but the tubes and the isosurface at G = 0 to off.
    3) Set the opacity of the isosurface to 0.4.
    4) Press play.

Author:       John Kluesner
Date:         13 Dec, 2013
Email:        stringman45@gmail.com
"""

import numpy as np
from evtk.hl import gridToVTK

# Generate arrays of the values for lambda, alpha, and x. Restructure the grid
# to make more grid points around the origin as this is where a bifurcation
# occurs.
A = np.linspace(-3,3,101)
x_vals = A**3/9
lambdas = A**3/9
alphas = A**3/9

# Create the meshes that will be used to generate the attributes. The purpose
# of these meshes is to make good use of vectorization.
x_grid = x_vals.reshape(1, 1, len(x_vals))
x_grid = x_grid.repeat(len(lambdas), axis=1)
x_grid = x_grid.repeat(len(alphas), axis=0)
lambda_grid = lambdas.reshape(1, len(lambdas), 1)
lambda_grid = lambda_grid.repeat(len(x_vals), axis=2)
lambda_grid = lambda_grid.repeat(len(alphas), axis=0)
alpha_grid = alphas.reshape(len(alphas), 1, 1)
alpha_grid = alpha_grid.repeat(len(x_vals), axis=2)
alpha_grid = alpha_grid.repeat(len(lambdas), axis=1)

# Create the attribute for G = x^3 + lambda*x + alpha_1*x^2. The alpha_2
# auxiliary parameter will be included using animation in ParaView.
G = x_grid**3 + lambda_grid*x_grid + alpha_grid*x_grid**2

# Create the attribute for G_x = 3*x^2 + lambda + 2*alpha*x
# and use the signum function as a test for stability.
Gx = 3*x_grid**2 + lambda_grid + 2*alpha_grid*x_grid
sgn_Gx = np.sign(Gx)

# Use EVTK to create the VTR file.
# The parameters for gridToVtk: (file name, x-coords of mesh, y-coords of mesh,
#                                z-coords of mesh, pointData).
gridToVTK("./pitchforkMesh", alphas, lambdas, x_vals, \
            pointData={"G":G, "stability":sgn_Gx, "G_x":Gx})
