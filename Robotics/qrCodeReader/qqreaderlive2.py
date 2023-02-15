"""
	Requires the following OS packages:
		- zbar (ran with 'zbarimg' command)
"""

from __future__ import annotations

import cv2
import time


if __name__ == "__main__":

    qcd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Can't open camera.")
        quit()
    else:
        print("Opened camera.")

    time.sleep(1)

    start = time.time()
    delta = 1.0

    while True:

        print()

        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame.")
            break

        retQr, decodedInfo, points, _straightQr = qcd.detectAndDecodeMulti(frame)

        if retQr:
            if len(decodedInfo) > 0:
                print(f"QR Code(s): {decodedInfo}")
            
            for s, p in zip(decodedInfo, points):
                if s:
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)


        delta = time.time() - start
        fps = 1 / delta
        start = time.time()

        print(f"FPS: {fps:.2f}\tDelta: {(delta * 1000):.2f} ms")

        cv2.imshow("Camera Feed", frame)


        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
