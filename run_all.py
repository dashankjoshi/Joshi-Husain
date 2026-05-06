import subprocess
import sys

scripts = [
    "scripts/01_profile_data.py",
    "scripts/02_clean_flights.py",
    "scripts/03_clean_weather.py",
    "scripts/04_integrate_data.py",
    "scripts/05_analyze_visualize.py",
]

for script in scripts:
    print(f"\nRunning {script}...")
    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"Error: {script} failed.")
        sys.exit(result.returncode)

print("\nWorkflow complete. All scripts ran successfully.")