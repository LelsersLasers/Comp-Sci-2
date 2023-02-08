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
	"""
	try:
		# Run the zbarimg command to read the QR code
		output = subprocess.check_output(
			["zbarimg", imagePath],
			stderr=subprocess.STDOUT
		)
		# Get the contents of the QR code
		stringOutput = output.decode("utf-8").strip()

		firstLine = stringOutput.split("\n")[0].strip()
		parts = firstLine.split(":")
		linkParts = parts[1:]
		return "".join(linkParts)
	except subprocess.CalledProcessError: # better to just let it throw?
		return None

if __name__ == '__main__':
	args = sys.argv[1:]

	for arg in args:
		qrCode = readQRCode(arg)
		print(f"QR Code in {arg}: {qrCode}")