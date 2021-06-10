import qrcode
import image
qr = qrcode.QRCode(
  version = 15,
  box_size = 10,
  border = 5
)

### in data, you can use your own url or file path and the qr code would be generted, which when scanned with a qr code scanner would direct it to the file ###

data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",back_color = "white" )
img.save('test.png')
