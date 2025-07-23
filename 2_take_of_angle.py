import numpy as np
from obspy.taup import TauPyModel

# 1. Define distance and depth grids (same as in the travel-time table)
distances = np.unique(np.concatenate([
    np.arange(0,   50.1, 2),    # 0–50 km, 2 km grid
    np.arange(50,  200.1, 5),   # 50–200 km, 5 km grid
    np.arange(200, 2000.1, 10)  # 200–2000 km, 10 km grid
])).astype(int)

depths = np.unique(np.concatenate([
    np.arange(0,   50.1, 2),    # 0–50 km, 2 km grid
    np.arange(50,  200.1, 5),   # 50–200 km, 5 km grid
    np.arange(200, 700.1, 10)   # 200–700 km, 10 km grid
])).astype(int)

# 2. Initialize the TauPyModel
model = TauPyModel(model="ak135tt")

# 3. Open output file
with open("takeoff_angles.tbl", "w") as f:
    # 4. Loop over each point and compute/write results
    for depth in depths:
        for dist in distances:
            # Compute P-wave take-off angle, converting distance from km to degrees
            arrivals = model.get_travel_times(
                source_depth_in_km=depth,
                distance_in_degree=dist / 111.19,
                phase_list=["P"]
            )
            # Use the first P phase take-off angle (in degrees), or 0.0 if none found
            angle = arrivals[0].takeoff_angle if arrivals else 0.0

            # Format line with fixed-width columns:
            # Columns:
            # 01–06: F6.1  take-off angle
            # 07–08: blank
            # 09–11: I3    depth
            # 12–13: blank
            # 14–18: I5    distance
            line = (
                f"{angle:6.1f}"  # Col 01–06
                f"  "            # Col 07–08 (2 spaces)
                f"{depth:3d}"    # Col 09–11
                f"  "            # Col 12–13 (2 spaces)
                f"{dist:5d}"     # Col 14–18
            )
            f.write(line + "\n")

print(f"Fixed-width take-off angle table 'takeoff_angles.tbl' generated with {len(depths) * len(distances)} points.")
