import xarray as xr
import matplotlib.pyplot as plt

# Load the dataset
nc_file = 'C3S422Lot2TEC_day-good-hci-month-proj_mean_monthly_1986_2005_v1.nc'  # Adjust this to the path of your NetCDF file
ds = xr.open_dataset(nc_file)

# Select a variable and time index to visualize
variable = 'day-good-hci-month-proj'
time_index = 0  # Adjust this index to select different months

# Extract the specific time slice from the dataset
data_slice = ds[variable].isel(time=time_index)

# Plotting
plt.figure(figsize=(10, 6))
data_slice.plot(x='rlon', y='rlat', cmap='viridis')

plt.title(f"{variable} for time index {time_index}")
plt.xlabel('Rotated Longitude')
plt.ylabel('Rotated Latitude')
plt.show()

# Close the dataset
ds.close()
