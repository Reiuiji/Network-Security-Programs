HW1 Stenography
=========================

In this folder you will see a python script called HW1.py
This script will run though encrypting a image.

The program is design to hide a license plate to anonymity vehicles but if need can be decrypted by an authorized user.

The work was based on Ikechukwu Azogu and Hong Liu paper "Privacy-Preserving License Plate Image Processing"

The License plate image is a stock image obtain from their paper.

Use:
-------------------------

python2.7 HW1.py [-h] [-i IMG] [-d] [-s SEED] [-sa] [-w]

Examples:

Encrypt image with the shift algorithm overlay

python2.7 HW1.py -sa

Set a custom Seed (0x4bf3ebdddb87b417ab837ded40ce5c3ab5f8126d2722a18087c8991ef89477df)

python2.7 HW1.py -s 0x4bf3ebdddb87b417ab837ded40ce5c3ab5f8126d2722a18087c8991ef89477df

Select a new image to encrypt

python2.7 HW1.py -i /home/user/Pictures/image.jpg

Enable Debug

python2.7 HW1.py -d
