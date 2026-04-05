import cv2

# Use CAP_DSHOW to bypass modern Windows camera 'negotiation'
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open webcam at index 0. Trying index 1...")
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

print("Attempting to open camera... if successful, a window will pop up.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Is another app (Zoom/Teams) using the camera?")
        break
        
    cv2.imshow('Contrast Healthcare Lab - Test 1', frame)
    
    # Wait for 1 millisecond. If 'q' is pressed, exit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Program closed successfully.")