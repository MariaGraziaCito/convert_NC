import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt

# Path to your NetCDF file
nc_file = 'example.nc'

# Using netCDF4
print("Using netCDF4:")
ds_nc = nc.Dataset(nc_file, 'r')

# Print variables
print("Variables:", list(ds_nc.variables.keys()))

# Print dimensions
print("Dimensions:", list(ds_nc.dimensions.keys()))

# Example of accessing and printing a variable's data
# Replace 'variable_name' with the name of a variable in your file
variable_name = 'variable_name'  # Change this to your specific variable name
if variable_name in ds_nc.variables:
    var_data = ds_nc.variables[variable_name][:]
    print(f"Data for {variable_name}:", var_data)

# Close the dataset
ds_nc.close()

# Using xarray
print("\nUsing xarray:")
ds_xr = xr.open_dataset(nc_file)

# Print dataset structure
print(ds_xr)

# Access and print a variable's data using xarray
# This uses .sel() to select data; modify or remove selection as needed
if variable_name in ds_xr:
    data_xr = ds_xr[variable_name].sel()  # Add selection criteria as needed
    print(f"Data for {variable_name} using xarray:", data_xr)

    # Plotting example (uncomment the next line to enable plotting)
    # data_xr.plot()

# Close the dataset
ds_xr.close()
