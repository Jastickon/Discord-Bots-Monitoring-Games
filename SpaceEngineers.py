import os
import socket

def SEP():
    ip = "176.57.181.101"
    port = 28700

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b"\xff\xff\xff\xff\x41\x62\xde\x97\x76", (ip, port))
    data, server = client_socket.recvfrom(1)
    print(f'{data}')

SEP()

"""
Date: 03.06.2023 
Discord: [PnD] Хлебушек Игорь#8603
info: Connection on UDP
S -> C (\xff\xff\xff\xff\x41 (\x..\x..\x..\x..) тут стоят симолы хз от чего хависит )
C -> S (\xff\xff\xff\xff(\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79)TSourceEngineQuery (\x..\x..\x..\x..)тут стоят такиеже символы )
S -> C (00000009  ff ff ff ff 49 11 53 70  61 63 65 20 45 6e 67 69   ....I.Sp ace Engi
00000019  6e 65 65 72 73 20 53 65  72 76 65 72 20 47 4f 00   neers Se rver GO.
00000029  41 6c 74 65 72 6e 61 74  69 76 20 72 65 61 6c 69   Alternat iv reali
00000039  74 79 00 53 70 61 63 65  20 45 6e 67 69 6e 65 65   ty.Space  Enginee
00000049  72 73 00 53 70 61 63 65  20 45 6e 67 69 6e 65 65   rs.Space  Enginee
00000059  72 73 00 00 00 00 0b 00  64 77 01 01 31 32 30 32   rs...... dw..1202
00000069  31 31 39 00 b1 48 71 02  08 3a cb e4 5b 40 01 67   119..Hq. .:..[@.g
00000079  72 6f 75 70 49 64 30 20  76 65 72 73 69 6f 6e 31   roupId0  version1
00000089  32 30 32 31 31 39 20 64  61 74 61 68 61 73 68 47   202119 d atahashG
00000099  6c 64 31 76 6d 76 68 66  32 74 6d 49 37 43 48 64   ld1vmvhf 2tmI7CHd
000000A9  35 77 43 46 6d 52 43 74  6c 73 3d 20 6d 6f 64 73   5wCFmRCt ls= mods
000000B9  33 37 20 67 61 6d 65 6d  6f 64 65 53 32 35 2d 32   37 gamem odeS25-2
000000C9  30 2d 31 30 2d 31 30 20  76 69 65 77 36 30 30 30   0-10-10  view6000
000000D9  00 72 bc 03 00 00 00 00  00                        .r...... .) 
NO COMMENT
"""