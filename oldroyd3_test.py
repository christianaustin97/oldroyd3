"""
	Testing my Python library out so far lol
"""

from fenics import *
from steady_nse_solver import *
from oldroyd3_solver import *

import matplotlib.pyplot as plt
import plotsp

#first thing is to make sure that plugging in l1=mu1=0 does get the Newtonian soln
meshsize = 64

eta = 10.0
l1 = 1e-4
mu1 = 1e-2

x = navier_stokes_bearing(32, r=0.5, ecc=0.25, eta=eta)
u_soln = x.velocity
p_soln = x.pressure

# Plot Newtonian solution
p_newt_plot = plot(p_soln, title="Newtonian Solution Pressure")
plt.colorbar(p_newt_plot)
plt.show()

u_newt_plot = plot(u_soln, title="Newtonian Solution Velocity", units='xy', scale=1)
plt.colorbar(u_newt_plot)
plt.show()

u_newt_plot_mag = plot(sqrt(inner(u_soln,u_soln)), title="Newtonian Solution Magnitude of Velocity")
plt.colorbar(u_newt_plot_mag)
plt.show()


"""
# Call NSE Solver
print("Calling NSE solver...")
nse_results = navier_stokes_ldc(meshsize, eta)
u_nse = nse_results.velocity
p_nse = nse_results.pressure
T_nse = nse_results.stress_tensor

# Call Oldroyd 3 Solver
print("Calling Oldroyd 3 solver...")
o3_results = oldroyd3_ldc(meshsize, eta, 0.0, 0.0, 15, 10e-6, 1.0)
u_o3 = o3_results.velocity
p_o3 = o3_results.pressure
T_o3 = o3_results.stress_tensor

print("L2 difference between velocities: ")
print(errornorm(u_nse, u_o3, norm_type='l2'))

print("L2 difference between stress tensors: ")
print(errornorm(T_nse, T_o3, norm_type='l2'))

# Plot Newtonian solution
p_newt_plot = plot(p_nse, title="Newtonian Solution Pressure")
plt.colorbar(p_newt_plot)
plt.show()

u_newt_plot = plot(u_nse, title="Newtonian Solution Velocity")
plt.colorbar(u_newt_plot)
plt.show()

u_newt_plot_mag = plot(sqrt(inner(u_nse,u_nse)), title="Newtonian Solution Magnitude of Velocity")
plt.colorbar(u_newt_plot_mag)
plt.show()

# Plot Newtonian solution by Oldroyd 3
p_newt_plot = plot(p_o3, title="Newtonian Solution (by O3) Pressure")
plt.colorbar(p_newt_plot)
plt.show()

u_newt_plot = plot(u_o3, title="Newtonian Solution (by O3) Velocity")
plt.colorbar(u_newt_plot)
plt.show()

u_newt_plot_mag = plot(sqrt(inner(u_o3,u_o3)), title="Newtonian Solution Magnitude of Velocity")
plt.colorbar(u_newt_plot_mag)
plt.show()
"""










