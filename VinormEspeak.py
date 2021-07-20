from phonemizer.phonemize import phonemize
from vinorm import TTSnorm
from phonemizer.separator import Separator
from string import punctuation

sep = Separator(phone='/', syllable='*', word='_')

def PhonemeConverter(text):
    language = 'vi'
    text = text.strip(punctuation+" ")
    normText = TTSnorm(text)
    phonemes = phonemize(normText,
                         language=language,
                         separator=sep,
                         backend='espeak',
                         preserve_punctuation=True,
                         with_stress=False,
                         njobs=4,
                         language_switch='remove-flags')
    phonemes = phonemes.replace("//","/")
    phonemes = phonemes.replace("," , "/,")
    phonemes = phonemes.split("_")
    phonemes = " /".join(phonemes)
    phonemes = phonemes.split("/")
    
    norm_phoneme = []
    for phone in phonemes:
        if phone =="." or phone == " " or phone == ",":
            norm_phoneme.append(phone)
            continue
        phone = phone.strip(punctuation+" ")

        if phone != "":
            norm_phoneme.append(phone)
    return norm_phoneme



def getPhoneme():
    return ['', 'eə7', 'ɛ7', 'a7', 'eə1', 'd', 's', 'ə2', 'o5', 'ɛ2', 'a2', 'ɑːɑː', 'iə6', 'u5', 'u2', 'i7', 'c', 'iɛɜ', 'm', 'h', 'iəɜ', 'uɜ', 'a5', 'ð', 'ɔː7', 'uə1', 'ɔɪ7', 'ɹ', 'iə5', 'ʊ1', 'ɐɐ', 'iɛ2', 'ɔɜ', 'ə5', 'ələl', 'y2', 'əːʊ7', 'ə7', 'y5', 'ʊ7', 'ɲ', 'u6', 'əɪ6', 'uə2', 'əɜ', '.', 'u1', 'yə7', 'tʃ', 'aɜ', 'aː2', 'aʊ1', 'ii', 'yə2', 'ə6', 'ɔɪ1', 'əː6', 'u7', 'e1', 'a6', 't̪', 'u4', 'o7', 'ʊə7', 'əə', 'yəɜ', 'e6', 'uə7', 'ɔːɔː', 'ɒ7', 'ɛ1', 'o6', 'əː2', 'iə4', 'aː7', 'e2', 'e7', 'aː4', 'aʊ7', 'əɪ7', 'əɪ4', 't', 'ɑː1', 'l', 'y7', 'kh', 'əː1', ' ', 'y4', 'i5', 'yə1', 'əː5', 'ʌ1', 'uəɜ', 'i6', 'ʌ7', 'aːɜ', 'iː7', 'f', 'i4', 'e5', 'əɪɜ', 'o1', 'iɛ5', 'θ', 'əːɜ', 'j', 'ɔ6', 'ɔ2', 'ɪ1', 'iə7', 'n', 'yə4', 'ŋ', 'iɛ4', 'iː1', 'ʒ', 'i2', 'p', 'o2', 'ɪ7', 'ɔ1', 'ɛ5', 'ɔ7', 'ɑː7', 'ə4', 'eɪ1', 'əɪ2', 'aɪ7', 'dʒ', 'x', 'aː1', 'iə2', 'y6', 'ɔ5', 'uə5', 'ɔː1', 'a4', 'aː6', 'əː7', 'iɜ', 'w', 'əː4', 'əɪ5', 'aɪ1', 'ɔ4', 'aɪə1', 'iɛ7', 'ɛ4', 'i1', 'aɪə7', 'k', 'ɗ', 'uə6', 'ɜː7', 'uə4', 'y1', 'ʃ', 'ɜː1', 'o4', 'v', 'a1', 'e4', 'iə1', 'iɛ6', 'ɒ1', 'yɜ', 'eɪ7', 'yə5', 'ʊə1', 'ɛɜ', 'yə6', 'əʊəʊ', 'ə1', 'eɜ', 'uː7', 'uː1', 'b', 'iɛ1', 'oɜ', 'ɛ6', 'ʐ', 'aː5', 'z', 'ɣ', 'ɡ', 'aa']
if __name__ == "__main__":

    testCase = [
        "kiểm tra câu chứa english trong đó",
        "kết thúc bằng dấu chấm.",
        "dấu , phẩy, ở ,giữa   ,   các,kiểu",
        "dấu phẩy dính ,english, trong đó"
    ]

    for test in testCase:
        phoneme = PhonemeConverter(test)
        print("="*100)
        print(test)
        print(phoneme)

    print(len(getPhoneme()))