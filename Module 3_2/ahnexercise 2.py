# %% Importing the libraries
import netCDF4 as nc
import matplotlib.pyplot as plt

# %% Read the data
grid = nc.Dataset('mv100.nc')
# Plot using matplotlib.pcolormesh
xx = grid.variables['x'][1000:1500]
yy = grid.variables['y'][500:1000]
zz = grid.variables['depth'][1000:1500, 500:1000]

# %%


fig, ax = plt.subplots(1, 1, figsize=(10, 8))
cmap = plt.get_cmap('terrain')
plt.pcolormesh(xx / 1000, yy / 1000, zz.T, cmap=cmap)
plt.colorbar(label='NAP Height [m]')
ax.axis('equal')
ax.axis('tight')
plt.title('Digital Elevation Model for the Nederlands')
plt.xlabel('X-RD [km]')
plt.ylabel('Y-RD [km]')
plt.clim(-20,150)