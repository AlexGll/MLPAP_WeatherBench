import weatherbench2 
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np


#ERA 5
location = "gs://weatherbench2/datasets/era5/"

fichier_1 = location + "1959-2023_01_10-full_37-1h-0p25deg-chunk-1.zarr"
fichier_2 = location + "1959-2023_01_10-wb13-6h-1440x721_with_derived_variables.zarr"
fichier_3 = location + "1959-2023_01_10-6h-240x121_equiangular_with_poles_conservative.zarr"
fichier_4 = location + "1959-2023_01_10-6h-64x32_equiangular_conservative.zarr"

data = xr.open_zarr(fichier_3)

print("Variables disponibles :", list(data.data_vars))

#sélectionne la température à 2 m (t2m)
t2m = data["2m_temperature"]

# 1er janvier 2020 à 00h
date = "2020-01-01T00:00"
t2m_at_date = t2m.sel(time=date)


#Trace carte
plt.figure(figsize=(10, 6))
t2m_at_date.plot(x="longitude", y="latitude", cmap="coolwarm", cbar_kwargs={"label": "Température à 2 m (K)"})
plt.title(f"Température à 2 m - {date}")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

