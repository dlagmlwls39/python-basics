def korean_number(num):
    num_list = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']
    if 1 <= num <= 10:
        return num_list[num - 1]
    else:
        return '지원하지 않는 숫자입니다.'
    
    # match(num):
    #     case 1:
    #         return '일'
    #     case 2:
    #         return '이'
    #     case 3:
    #         return '삼'
    #     case 4:
    #         return '사'
    #     case 5:
    #         return '오'
    #     case 6:
    #         return '육'
    #     case 7:
    #         return '칠'
    #     case 8:
    #         return '팔'
    #     case 9:
    #         return '구'
    #     case 10:
    #         return '십'

if __name__ == '__main__':
    num = int(input())
    korean_num = korean_number(num)
    print(korean_num)
