#!/usr/bin/env python3
# calc_taup_inspect.py

from obspy.taup import TauPyModel
import numpy as np

import os
from obspy.taup.taup_create import build_taup_model
from obspy.taup.tau_model import TauModel

# 1. Build the model (only provide the .tvel file; the corresponding .nd in the same directory will be loaded automatically)
build_taup_model(
    filename="ak135tt.tvel",
    output_folder=None,    # None → save to the taup/data folder in the ObsPy installation directory
    verbose=True
)

# 2. Load the custom 'ak135tt' model
model = TauPyModel(model="ak135tt")

# 3. Compute travel times for a source depth of 5 km and an epicentral distance of 0.9°
arrivals = model.get_travel_times(source_depth_in_km=5, distance_in_degree=0.9)

print(arrivals)
