# Traffic Sign Detection and Warning System

This project is a real-time Traffic Sign Detection and Warning System built using  OpenCV, and YOLO (You Only Look Once) models from the `ultralytics` library. The application captures live video feed from the camera, detects traffic signs, and provides real-time feedback to help users recognize traffic signs effectively.

## Features
- **Real-time Traffic Sign Detection**: Uses YOLO models to detect traffic signs in live video.
- **Easy to Use**: Designed for real-time detection without uploading images, capturing video directly from the user's camera.

## Requirements

- Python 3.7+
- OpenCV
- Ultralytics (for YOLO models)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SaiGawand12/TRAFIC-SIGN-DETECTION-AND-WARNING-SYSTEM.git
   cd TRAFIC-SIGN-DETECTION-AND-WARNING-SYSTEM
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv env
   # Activate the virtual environment
   # On Windows
   .\env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install Dependencies**

   Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not provided, install dependencies manually:

   ```bash
   pip install  opencv-python-headless ultralytics
   ```

## Usage

1. **Run the Code**

   Start the video interface by running the following command:

   ```bash
   python real_time.py
   ```

2. **Using the Application**

   - Once the code is run, it will access your camera.
   - The system will start detecting traffic signs in real-time and display warnings.
   - Press the "q"  to end the video capture.

## Project Structure

- `real_time.py`: Contains the traffic sign detection functions utilizing YOLO.
- `test.py`: Contains the test code.
- `requirements.txt`: List of required Python packages.
- Additional files and directories may include detection model files, configuration, and helper scripts.

## Troubleshooting

- **ModuleNotFoundError**: If you encounter an error saying `No module named 'ultralytics'`, install it by running `pip install ultralytics`.

## Acknowledgments

- **Ultralytics**: For the YOLO models used in real-time detection.
- **OpenCV**: For enabling real-time computer vision and a user-friendly interface.

## License

This project is licensed under the MIT License.

---
