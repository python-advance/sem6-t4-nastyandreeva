import pyqrcode
import png

def createQr(content, module_color, background, file_format, scale):
    qrcode = pyqrcode.create(content)
    if file_format == 'png':
        qrcode.png('qrcode.png', module_color = module_color, background=background,scale=scale)
    elif file_format == 'svg':
        qrcode.svg('qrcode.svg', module_color = module_color, background=background,scale=scale)

result = input("Введите нужную строку: ")
createQr(result, (119,136,153), (255,228,225), file_format = 'png', scale = 10)
