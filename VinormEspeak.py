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
    return ['', 'iɛ7', 'd', 'əɜ', 'ɹ', 't̪', 'y7', 'aːʊ1', 'y4', 'aː4', 'ə5', 'e2', 'o5', 'uː1', 'aːɪɜ', 'i6', 'a7', 'ɑː7', 'iɛ5', 'ʌ7', 'f', 'v', 'ɒ1', 'eɪ7', 'əː7', 'uɪ5', 'oæ7', 'ʂ', 'i4', 'ɛ2', 'z', 'ɛʊ1', 'aːɪ1', 'aːʊ2', 'aːɪ2', 'a2', 'ð', 'ɔ2', 'əʊ4', 'ɣ', 'aː6', 'y2', 'yə5', 'n', 'əʊ5', 'c', 'a4', 'aːʊ6', 'iə5', 'ɔi2', 'o4', 'ə2', 'əːɪ6', 'əʊ7', 'ɜː1', 'əːɪ4', 'aːɪ5', 'b', 'iɛ2', 'əɪ7', 'uɪ7', 'eʊ1', 'iɜ', 'oə5', 'ŋ', 'j', 'əʊ2', 'ɗ', 'ɛɜ', 'uɪ4', 'e1', 'əː1', 'ə1', 'ɔ4', 'ɛʊ7', 'i2', 'ɔ1', 'ʊ7', 'əɪ6', 'ʐ', 'ʃ', 'əɪ4', 'aː1', '.', 'əːɪ2', 'kh', 'eʊɜ', 'yɪ4', 'iɛɜ', 'e5', 'əːɜ', 'uə1', 'o1', 'yə6', 'ɛ6', 'yə4', 'ələl', 'i7', 'iə4', 'ɑːɑː', 'əː2', 'aː7', 'ʌ1', 'ɐɐ', 'o2', 'aɪə7', 'aː2', 'e6', 'iʊ1', 'ɔiɜ', 'aːʊ7', 'oæ2', 'u7', 'iː1', 'uə4', 'oɪ7', 'ʒ', 'ɔɪ2', 'aɪ1', 'eʊ5', 'eɪ1', 'p', 'aːɪ7', 'ɛʊ4', 'h', 'ʊ1', 'ɒ7', 'aː5', 'oəɜ', 'oɪ4', 'θ', 'eɜ', 'aːɪ4', 'əʊ1', 'aɪ2', 'uː7', 'yɜ', 'iɛ1', 'oə4', 'u6', 'o7', 'eə1', 'uɪ6', 'aɪ5', 'aːɪ6', 'u2', 'aɜ', 'ɡ', 'oə1', 'ʊə7', 'ɪ7', 'aːʊɜ', 'ɛʊɜ', 'aa', 'ɔɜ', 'k', 'a1', 'iʊɜ', 'u5', 'yə7', 'ii', 'ɛ5', 's', 'dʒ', 'w', 'ɔ6', 'ɛʊ6', 'uə6', 'e4', 'ə6', 'yə2', 'oɪ5', 'm', 'oɪ2', ' ', 'oɪ6', 'iʊ6', 'y6', 'ɛʊ5', 'uəɜ', 'uɜ', 'uə7', 'x', 'əɪ2', 'aɪə1', 'iə1', 'oɜ', 'əː4', 'iɛ4', 'iʊ4', 'ə4', 'y5', 'aːʊ4', 'əʊ6', 'ɔ5', 'əɪ1', 'aːʊ5', 'uə2', 'tʃ', 'ɔːɔː', 'u1', 'əɪ5', 'uɪ2', 'eə7', 'ɔɪ1', 'əːʊ7', 'l', 'a6', 'oə7', 'aɪ7', 'aʊ2', 'iə7', 'ɔː1', 'iɛ6', 'a5', 'ɔi1', 'aɪɜ', 'əːɪ1', 'əɪɜ', 'ɔɪ6', 'iə2', 'ə7', 'uɪɜ', 'oɪ1', 'uɪ1', 'əʊɜ', 'uə5', 'iʊ2', 'eʊ2', 'iə6', 'ɔɪɜ', 'ɲ', 'o6', 'oæ1', 'əːɪɜ', 't', 'əː5', 'iʊ7', 'ɜː7', 'aʊ1', 'əː6', 'iəɜ', 'iʊ5', 'ɛʊ2', 'əə', 'oə6', 'ɔi6', 'əːɪ7', 'e7', 'əʊəʊ', 'aʊɜ', 'ɔi4', 'ɔɪ4', 'u4', 'eʊ4', 'oə2', 'ɔ7', 'ɛ4', 'tɕ', 'yə1', 'i1', 'aɪ6', 'y1', 'aɪ4', 'ɛ7', 'ɛ1', 'ɔi7', 'i5', 'ɔː7', 'iː7', 'ɔɪ5', 'yəɜ', 'ɑː1', 'ɔɪ7', 'aʊ7', 'oɪɜ', 'aːɜ', 'ɪ1', 'ʊə1']
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