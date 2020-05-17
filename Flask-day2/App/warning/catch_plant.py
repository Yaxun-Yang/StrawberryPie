def judge_new_plant():
    return True


def catch_plant():
    #如果获取到了 judge为true 否则为false
    judge = judge_new_plant()
    if judge:
        #获取植物 检测到两个参数
        plant_name = "桃蛋"
        img_url = "http"
        plant = {
            "plant_name": plant_name,
            "img_url": img_url
        }
        return plant
    else:
        return None

