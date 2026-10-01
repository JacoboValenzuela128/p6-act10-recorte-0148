import numpy as np
import cv2

# Visión Artificial Act10 NC:0148

# --- 1. Lee la imagen ---
img_base = cv2.imread("Baguetteto.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Bagetteto", img_base)
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

# Visión Artificial Act10 NC:0148

# ==========================================
# 2. LINEAS
# ==========================================
print("Mostrando: Linea")
img_linea = np.zeros((512, 512, 3), np.uint8)
img_linea = cv2.line(img_linea, (0, 0), (511, 511), (255, 255, 255), 3)

cv2.imshow('Linea', img_linea)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ==========================================
# 3. CIRCULOS
# ==========================================
print("Mostrando: Circulo")
img_circulo = np.zeros((512, 512, 3), np.uint8)
img_circulo = cv2.circle(img_circulo, (260, 260), 10, (255, 0, 0), -1)

cv2.imshow('Circulo', img_circulo)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ==========================================
# 4. TEXTO
# ==========================================
print("Mostrando: Texto")
img_texto = np.zeros((512, 512, 3), np.uint8)
img_texto = cv2.putText(img_texto, "Jacobo Valenzuela 0148", (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow('Texto', img_texto)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ==========================================
# 5. TRESHOLDING
# ==========================================
print("Mostrando: Thresholding")
# Carga la imagen 'Baguetteto.jpg' en escala de grises
img_thresh_input = cv2.imread('Baguetteto.jpg', 0)

if img_thresh_input is not None:
    ret, thr1 = cv2.threshold(img_thresh_input, 127, 255, cv2.THRESH_BINARY)
    ret, thr2 = cv2.threshold(img_thresh_input, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thr3 = cv2.threshold(img_thresh_input, 127, 255, cv2.THRESH_TRUNC)
    ret, thr4 = cv2.threshold(img_thresh_input, 127, 255, cv2.THRESH_TOZERO)
    ret, thr5 = cv2.threshold(img_thresh_input, 127, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow('BINARY', thr1)
    cv2.imshow('BINARY_INV', thr2)
    cv2.imshow('TRUNC', thr3)
    cv2.imshow('TOZERO', thr4)
    cv2.imshow('TOZERO_INV', thr5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: No se encontró la imagen 'Baguetteto.jpg' para el Thresholding.")


# ==========================================
# 6. TRACKBARS
# ==========================================
print("Mostrando: Trackbars (Presiona ESC para salir)")

def on_trackbar(val):
    print(val)

img_trackbar = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('frame')

cv2.createTrackbar('R', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('G', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('B', 'frame', 0, 255, on_trackbar)

while True:
    cv2.imshow('frame', img_trackbar)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: # Presiona ESC para finalizar
        break

    r = cv2.getTrackbarPos('R', 'frame')
    g = cv2.getTrackbarPos('G', 'frame')
    b = cv2.getTrackbarPos('B', 'frame')

    img_trackbar[:] = [b, g, r]

cv2.destroyAllWindows()