"""
	Requires the following packages:
		- zbar (ran with 'zbarimg' command)
"""

from __future__ import annotations

import subprocess
import sys


def readQRCode(imagePath: str) -> str | None:
	"""
		Reads the QR code in the image at the given path.
		Returns the contents of the QR code.
		Returns None if the QR code could not be read.

		Only works if there is 1 or 0 QR codes in the image.
	"""
	try:
		output = subprocess.check_output(
			["zbarimg", imagePath],
			stderr=subprocess.STDOUT # hides output of zbarimg
		)

		stringOutput = output.decode("utf-8").strip()

		firstLine = stringOutput.split("\n")[0].strip()
		parts = firstLine.split(":")
		linkParts = parts[1:]
		return "".join(linkParts)

	except subprocess.CalledProcessError:
		return None

if __name__ == '__main__':
	paths = sys.argv[1:]

	for path in paths:
		qrCode = readQRCode(path)
		print(f"QR Code in {path}: {qrCode}")