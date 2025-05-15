#import tools #module結構化
#from tools import calculate_bmi, get_state #指定improt
import edu #package結構化專案
# form edu.tools import calculate_bmi as a #as 重新命名
# form edu.tools get_state as b
def main():
    try:
        height:int = int(input('請輸入你的身高(公分 cm):'))
        weight = eval(input('請輸入你的體重(公斤 kg):'))
        bmi = edu.tools.calculate_bmi(height, weight)
    except ValueError:
        print('輸入發生錯誤')
    except Exception as e :
        print(e)
    else:
        print(f'你的身高:{height} 公分')
        print(f'你的體重:{weight:.2f} 公斤')
        print(f'你的 BMI值為:{bmi:.2f}')
        print(edu.tools.get_state(bmi))
if __name__ == "__main__" :
    main()
