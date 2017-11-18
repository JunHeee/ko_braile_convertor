import re

from map.ko_braile_map import *


BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def ko_braile_convertor(sentence):
    sentence = sentence.replace(" ", "/")
    split_keyword_list = list(sentence)
    print(split_keyword_list)

    result = list()
    for keyword in split_keyword_list:
        # 한글 여부 check 후 분리
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result.append(map_chosung[CHOSUNG_LIST[char1]])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result.append(map_jungsung[JUNGSUNG_LIST[char2]])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            result.append(map_jongsung[JONGSUNG_LIST[char3]])
        elif re.match('[0-9]', keyword) is not None:
            result.append(map_number[int(keyword)])
        else:
            result.append(keyword)

    result = "".join(result)
    result = result.replace(" ", "")
    result = result.replace("/", " ")

    # result
    return result


if __name__ == '__main__':
    result = ko_braile_convertor('한글 점자 번역기')
    print(result)
