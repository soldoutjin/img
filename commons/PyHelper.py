# -*- coding: utf-8 -*-
import socket
print "-------------------"
jeonIP = '10.54.1.41'
yeoIP = '10.54.1.47'
jeonImgPath = "j\\img\\"
yeoImgPath =  ""

# @Return : 현재 사용하고 있는 피씨의 ip
def __getHost():
    return socket.gethostbyname(socket.gethostname())

# @Return : 각 피씨별 이미지 패쓰
# @Example :   from commons import PyHelper // PyHelper.getImgPath();
def getImgPath():
    if __getHost() == jeonIP :
        return jeonImgPath
    elif __getHost() == yeoIP :
        return yeoImgPath

