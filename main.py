import subprocess
import sys

def run_script(script_name):
    """Run a Python script and wait for it to finish."""
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}:")
        print(result.stdout)
        print(result.stderr)
        return False
    print(f"Successfully ran {script_name}.")
    return True

def main():
    # Run recording_convert.py
    if not run_script("recording_convert.py"):
        return
    
    # Run text_summary.py
    if not run_script("text_summary.py"):
        return

if __name__ == "__main__":
    main()
