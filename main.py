import cv2
import mediapipe as mp
import os

# Variable para controlar si el video ya se mostró
video_shown = False

# Cargar imagen plantilla de mano
template = cv2.imread('hand_template.png', cv2.IMREAD_UNCHANGED)
template_h, template_w = template.shape[:2]

# Inicializar cámara
cap = cv2.VideoCapture(0)

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Función para superponer imagen con transparencia
def overlay_image_alpha(img, img_overlay, pos):
    x, y = pos
    alpha_overlay = img_overlay[:, :, 3] / 255.0
    alpha_background = 1.0 - alpha_overlay

    for c in range(3):
        img[y:y+img_overlay.shape[0], x:x+img_overlay.shape[1], c] = (
            alpha_overlay * img_overlay[:, :, c] +
            alpha_background * img[y:y+img_overlay.shape[0], x:x+img_overlay.shape[1], c]
        )

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    center_x, center_y = w // 2 - template_w // 2, h // 2 - template_h // 2
    overlay_image_alpha(frame, template, (center_x, center_y))

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            x_coords = [lm.x for lm in hand_landmarks.landmark]
            y_coords = [lm.y for lm in hand_landmarks.landmark]
            x_min, x_max = int(min(x_coords) * w), int(max(x_coords) * w)
            y_min, y_max = int(min(y_coords) * h), int(max(y_coords) * h)

            # Mostrar el video con sonido si la mano está alineada y aún no se mostró
            if (not video_shown and
                center_x < x_min < center_x + template_w and
                center_y < y_min < center_y + template_h and
                center_x < x_max < center_x + template_w and
                center_y < y_max < center_y + template_h):

                os.startfile("yourfile.mp4")
                video_shown = True

    cv2.imshow('Hand Scanner', frame)

    # Salir si se cierra la ventana o se presiona ESC
    if cv2.getWindowProperty('Hand Scanner', cv2.WND_PROP_VISIBLE) < 1:
        break
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
