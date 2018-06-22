#coding=utf-8
def is_target_shop(given):
    if '鲜花' in given:
        return True
    if '蛋糕' in given:
        return True
    if '小龙虾' in given:
        return True
    return False


def get_shop_type(given):
    shop_type = '其他'
    if('蛋糕' in given):
        shop_type = '蛋糕';
    elif('鲜花' in given):
        shop_type = '鲜花'
    elif('小龙虾' in given):
        shop_type = '小龙虾'
    return shop_type


def is_in_fence(aLon, aLat, pointList):
    try:
        iSum = 0
        iCount = len(pointList)
        aLat = float(aLat)
        aLon = float(aLon)

        if(iCount < 3):
            return False

        for i in range(iCount):

            pLon1 = float(pointList[i][3])
            pLat1 = float(pointList[i][4])

            if(i == iCount - 1):

                pLon2 = float(pointList[0][3])
                pLat2 = float(pointList[0][4])
            else:
                pLon2 = float(pointList[i + 1][3])
                pLat2 = float(pointList[i + 1][4])

            if ((aLat >= pLat1) and (aLat < pLat2)) or ((aLat>=pLat2) and (aLat < pLat1)):

                if (abs(pLat1 - pLat2) > 0):

                    pLon = pLon1 - ((pLon1 - pLon2) * (pLat1 - aLat)) / (pLat1 - pLat2);

                    if(pLon < aLon):
                        iSum += 1

        if(iSum % 2 != 0):
            return True
        else:
            return False
    except Exception as err :
        return False