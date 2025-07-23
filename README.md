
# TauP-Based Travel Time and Take-Off Angle Calculation

This simple set of scripts is used to calculate **take-off angles** and **travel times**.  
It is designed to generate files in the same structure and format as the **JMA2001** dataset.

## Directory Structure

A typical JMA2001 dataset contains three folders:

```
JMA2001/
├── take_off_angle/
├── travel_time/
└── velocity_structure/
```

This workflow allows you to construct similar file types for other regions based on a known velocity model.

## Steps

### 0. Prepare the Velocity Model

Edit a `.tvel` file to include your regional velocity model.  
You can start from one of the standard models provided in TauP (`StdModels`) and modify the velocity structure in the top 0–50 km to match your regional model.

### 1. Generate `.npz` Model

Use ObsPy to convert the `.tvel` file into a `.npz` model file, which TauPy can use.  
Run the script:  
```bash
python 1_xxx.py
```

### 2. Generate Travel Time Table

Use ObsPy to generate a travel time table with the same data format and grid as JMA.  
Run the script:  
```bash
python generate_travel_time.py
```

### 3. Generate Take-Off Angle Table

Use ObsPy to generate a take-off angle table with the same data format and grid as JMA.  
Run the script:  
```bash
python generate_take_off_angle.py
```

## Notes

- Both travel times and take-off angles are calculated on a predefined depth and distance grid, consistent with the JMA convention.
- Output files are written in fixed-width ASCII format to match JMA’s format exactly.
