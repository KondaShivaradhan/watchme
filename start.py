import subprocess
import sys
import os


def run_waitress():
    host = "0.0.0.0"
    port = 5001
    app_module = "app:app"
    app_directory = "app"  # Update this with the actual app directory name

    # Change the working directory to the app directory
    os.chdir(app_directory)

    command = [sys.executable, "-m", "waitress",
               f"--host={host}", f"--port={port}", app_module]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Waitress: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_waitress()
