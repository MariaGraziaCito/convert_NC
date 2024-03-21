import xarray as xr

# Load the dataset
nc_file = '/path/to/your/file.nc'  # Update this to the path of your NetCDF file
ds = xr.open_dataset(nc_file)

# Select the variable of interest
data_variable = ds['day-good-hci-month-proj']

# Optionally, perform any necessary reductions or selections on the data
# For example, to average over the 'time' dimension if it makes sense for your data:
# data_variable_mean_time = data_variable.mean(dim='time')

# Convert to a pandas DataFrame
df = data_variable.to_dataframe().reset_index()

# Save the DataFrame to CSV
csv_file = '/path/to/save/your_data.csv'  # Specify your desired CSV file path
df.to_csv(csv_file, index=False)

print(f"Data saved to {csv_file}")

# Close the dataset
ds.close()
