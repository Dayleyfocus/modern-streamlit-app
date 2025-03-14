"""
Launch script for the Modern Streamlit App.
"""
import os
import sys
import subprocess


def main():
    """Launch the Streamlit application."""
    print("Starting Modern Streamlit App...")
    
    # Get the absolute path to the current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Run the streamlit app directly with the correct PYTHONPATH
    env = os.environ.copy()
    
    # Make sure the parent directory is in PYTHONPATH so 'app' is recognized as a package
    env["PYTHONPATH"] = current_dir + os.pathsep + env.get("PYTHONPATH", "")
    
    # Run streamlit with the app/main.py file
    subprocess.run(["streamlit", "run", os.path.join(current_dir, "app/main.py")], env=env)


if __name__ == "__main__":
    main() 