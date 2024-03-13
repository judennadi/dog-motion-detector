import cv2

def detect_motion():
    # Initialize video capture
    cap = cv2.VideoCapture(0)

    # Initialize motion detector
    motion_detector = cv2.createBackgroundSubtractorMOG2()

    while True:
        # Read frame from camera
        ret, frame = cap.read()
        
        if not ret:
            break

        # Apply motion detection
        fgmask = motion_detector.apply(frame)

        # Find contours of detected motion
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw rectangles around detected motion
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display frame
        cv2.imshow('Dog Motion Detector', frame)

        # Check for 'q' key press to exit
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

def main():
    detect_motion()

if __name__ == "__main__":
    main()
