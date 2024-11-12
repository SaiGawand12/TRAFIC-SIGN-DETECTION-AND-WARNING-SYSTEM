import cv2
import numpy as np
from ultralytics import YOLO
import streamlit as st

# Load the YOLOv8 model
model = YOLO('weights\\best.pt')

classes = model.names

# Set up the Streamlit app
st.title('Traffic Sign Detection and Warning System')

# Option to select webcam source
camera_url = st.text_input('Enter camera URL (or leave empty for PC webcam):', '')

if camera_url:
    cap = cv2.VideoCapture(camera_url)  # Use external webcam (IP webcam)
else:
    cap = cv2.VideoCapture(0)  # Use PC webcam

# Start video processing if the capture device is open
if cap.isOpened():
    stframe = st.empty()  # Create an empty slot for video frames

    # Set the confidence threshold for detection
    confidence_threshold = st.slider('Confidence Threshold', 0.0, 1.0, 0.6)

    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            result = model.predict(frame, conf=confidence_threshold)

            # Visualize the results on the frame
            annotated_frame = result[0].plot()

            # Display the annotated frame in Streamlit
            stframe.image(annotated_frame, channels='BGR')

            # Warning and Detection Logic
            stop_sign_index = 71  # 'Stop' sign has index 71
            school_ahead_sign_index = 40  # 'School Ahead' sign has index 40
            Speed_limit_50_sign_index = 56  # Example of speed limit sign index

            for r in result:
                if r.boxes:
                    box = r.boxes[0]
                    class_id = int(box.cls)
                    object_name = model.names[class_id]

                    if classes[stop_sign_index] in object_name:
                        st.warning("Warning: You need to stop!")
                    elif classes[school_ahead_sign_index] in object_name:
                        st.warning("Warning: There is a school ahead!")
                    elif classes[Speed_limit_50_sign_index] in object_name:
                        st.warning("Warning: Speed Limit 50 - Watch your speed!")
        else:
            break

    cap.release()

else:
    st.error("Failed to open video stream.")

# Close the app when done
st.write('App finished.')
