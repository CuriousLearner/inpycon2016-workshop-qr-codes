# inpycon2016-workshop-qr-codes
Getting name and QR codes for sticker printing for PyCon India 2016

Setup Instructions:

- Make a directory `qrcodes` and place all the qrcode jpg files under it.
- Place `workshop.csv` file in the root directory.


The id number corresponds to the row that would be fetched from the CSV as well as the image of qr code to be referred.

How to build:

- Install staticjinja
- Run `python build_qr.py --id <idno>`
- Open the `index.html` file in the root directory.
