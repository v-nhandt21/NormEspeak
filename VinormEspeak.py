from phonemizer.phonemize import phonemize
from vinorm import TTSnorm

def PhoneConverter(text):
    language = 'vi'
    normText = TTSnorm(text)
    print(normText)
    phonemes = phonemize(normText,
                         language=language,
                         backend='espeak',
                         preserve_punctuation=True,
                         with_stress=False,
                         njobs=4,
                         language_switch='remove-flags')
    print(phonemes)
    return list(phonemes)

print(PhoneConverter("Vào tháng 12/2020 đã có vaccine phòng ngừa Covid-19"))

def getPhoneme():
    return ['h', 'ʐ', 'a', 'æ', 'ʃ', 'ɪ', '2', 'ɐ', 'l', ' ', '7', 'm', 'w', 'ɛ', 'n', 'ð', 'o', '5', 'ɔ', 'ɡ', 'ɑ', ':', 'd', 'θ', 'ʊ', 'ʒ', 'ɗ', ';', 'y', 'k', 't', 'ɒ', 'b', 'j', '6', 'ʌ', 'ʂ', '1', 'ː', 'c', 'ɣ', 'x', 'ə', 'e', 'ɹ', 'p', '̪', 'ɲ', ',', '?', 'v', '4', 'ŋ', 'ɜ', 'z', 'f', 'i', 'u', 's', '!', 'r', '.', 'ɕ']