import cv2
from model import load_model, predict

model = load_model()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # preprocessing
    input_data = frame

    result = predict(model, input_data)

    print("Prediction:", result)

    cv2.imshow("ASD Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()