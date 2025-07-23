import numpy as np
from obspy.taup import TauPyModel

# Define distance and depth grids
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

# Initialize the travel-time model
model = TauPyModel(model="ak135tt")

# Open output file
with open("travel_times.tbl", "w") as f:
    # Loop over each depth and distance, compute travel times and write to file
    for depth in depths:
        for dist in distances:
            # Convert distance from km to degrees (1° ≈ 111.19 km)
            arr = model.get_travel_times(
                source_depth_in_km=depth,
                distance_in_degree=dist / 111.19,
                phase_list=["P", "S"]
            )
            # Extract P and S arrival times (or 0.0 if not present)
            tP = next((a.time for a in arr if a.name == "P"), 0.0)
            tS = next((a.time for a in arr if a.name == "S"), 0.0)

            # Format output line with fixed-width columns:
            # Columns:
            # 01–01   'P'
            # 02–02   space
            # 03–10   P travel time (8 chars, 3 decimals)
            # 11–11   space
            # 12–12   'S'
            # 13–13   space
            # 14–21   S travel time (8 chars, 3 decimals)
            # 22–22   space
            # 23–25   depth (3-digit integer)
            # 26–27   two spaces
            # 28–32   distance (5-digit integer)
            line = (
                f"P"                            # Col 01
                f" "                            # Col 02
                f"{tP:8.3f}"                   # Col 03–10
                f" "                            # Col 11
                f"S"                            # Col 12
                f" "                            # Col 13
                f"{tS:8.3f}"                   # Col 14–21
                f" "                            # Col 22
                f"{depth:3d}"                  # Col 23–25
                f"  "                           # Col 26–27
                f"{dist:5d}"                   # Col 28–32
            )
            f.write(line + "\n")

print(f"Fixed-width travel-time table 'travel_times.tbl' generated with {len(depths) * len(distances)} points.")
