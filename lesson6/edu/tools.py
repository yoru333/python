def calculate_bmi(height,weight):
    if height < 120 or height > 220:
            raise Exception(f'輸入的身高: {height} 公分 不在 120 ~ 220 範圍內')
    height /= 100
    if weight < 30.0 or weight > 200.0:
            raise Exception(f'輸入的體重: {weight:.2f} 公斤 不在 30 ~ 200 範圍內')
    bmicalculate = weight / height ** 2
    return bmicalculate

def get_state(bmi):
    if bmi < 18.5:
        massage = "（過輕）"
    elif bmi < 24:
        massage = "（正常）"
    elif bmi < 27:
        massage = "（過重）"
    else:
        massage = "（肥胖）" 
    return massage