# watchme
 Let someone watch you?

# Pre requisites
- Python3
    - Depending on your OS install a global python 3 and its related pip version. 
- waitress cli
    - this should be install on a global level.
    - for Ubuntu i have used
    - 
        ```bash
        sudo apt install python3-waitress
        ```
    
- flask
    - This can be installed with pip
    - ```bash
        pip install falsk
        ```
- opencv for camera
    - For getting camera feed
    - ```bash
        pip install opencv-python
        ```
    - ```bash
        pip install opencv-contrib-python
        ```
- obvious a webcam

## Usage
directly from project directory with default configuration
```bash
python start
```
cd into app and then run

or you can run it manually with your post configuration
waitress-serve --host 0.0.0.0 --port 5001 app:app
