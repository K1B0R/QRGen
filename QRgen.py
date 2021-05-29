import qrcode
import numpy as np
from colorama import init, Fore, Back, Style
# Data That Will Be Encoded

print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '''
    QQQQQQQQQ     RRRRRRRRRRRRRRRRR           GGGGGGGGGGGGG                                      
   QQ:::::::::QQ   R::::::::::::::::R       GGG::::::::::::G                                      
 QQ:::::::::::::QQ R::::::RRRRRR:::::R    GG:::::::::::::::G                                      
Q:::::::QQQ:::::::QRR:::::R     R:::::R  G:::::GGGGGGGG::::G                                      
Q::::::O   Q::::::Q  R::::R     R:::::R G:::::G       GGGGGG    eeeeeeeeeeee    nnnn  nnnnnnnn    
Q:::::O     Q:::::Q  R::::R     R:::::RG:::::G                ee::::::::::::ee  n:::nn::::::::nn  
Q:::::O     Q:::::Q  R::::RRRRRR:::::R G:::::G               e::::::eeeee:::::een::::::::::::::nn 
Q:::::O     Q:::::Q  R:::::::::::::RR  G:::::G    GGGGGGGGGGe::::::e     e:::::enn:::::::::::::::n
Q:::::O     Q:::::Q  R::::RRRRRR:::::R G:::::G    G::::::::Ge:::::::eeeee::::::e  n:::::nnnn:::::n
Q:::::O     Q:::::Q  R::::R     R:::::RG:::::G    GGGGG::::Ge:::::::::::::::::e   n::::n    n::::n
Q:::::O  QQQQ:::::Q  R::::R     R:::::RG:::::G        G::::Ge::::::eeeeeeeeeee    n::::n    n::::n
Q::::::O Q::::::::Q  R::::R     R:::::R G:::::G       G::::Ge:::::::e             n::::n    n::::n
Q:::::::QQ::::::::QRR:::::R     R:::::R  G:::::GGGGGGGG::::Ge::::::::e            n::::n    n::::n
 QQ::::::::::::::Q R::::::R     R:::::R   GG:::::::::::::::G e::::::::eeeeeeee    n::::n    n::::n
   QQ:::::::::::Q  R::::::R     R:::::R     GGG::::::GGG:::G  ee:::::::::::::e    n::::n    n::::n
     QQQQQQQQ::::QQRRRRRRRR     RRRRRRR        GGGGGG   GGGG    eeeeeeeeeeeeee    nnnnnn    nnnnnn
             Q:::::Q                                                                              
              QQQQQQ                                                                              ''')

data = input(Style.BRIGHT + Fore.LIGHTRED_EX + 'URL: ')
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make()
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "Size of the QR Code:", np.array(qr.get_matrix()).shape)
img = qr.make_image(fill_color="black", back_color="white")
# Saving Image State

img.save("QrCode.png")