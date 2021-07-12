import pyqrcode
from pyqrcode import QRCode

s = 'https://www.facebook.com'

url = pyqrcode.create(s)

url.svg('facebook.svg', scale=8)