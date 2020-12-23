from espeak import PhoneConverter
import fileinput

SETP = []
vifile = "TTS_BIG_TRAINING_TEXT.txt"
file = "train.en"
enfile = "train_small.txt"

with open(vifile, "r",encoding="utf-8") as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split("~")[1]
        phonemes = PhoneConverter(line)
        SETP = list(set(SETP + phonemes))
    print(len(lines))
print(SETP)
print(len(SETP))

#['ɛ', 'w', 'ɪ', 'ɕ', '5', ' ', 'a', 'ə', 'ɒ', 'p', 'c', '1', '4', 'ɜ', 'ʊ', 'ː', 'k', 'x', 'ɗ', 'o', 'd', 'ɡ', 's', 'v', 'ɔ', 'y', 'z', 'e', 'ʂ', 'b', 'ŋ', 'l', 'm', 'ɣ', 't', 'i', 'ʒ', 'ɹ', '2', 'ɐ', '7', 'h', 'ɲ', '6', 'ɑ', 'æ', 'n', 'ʃ', 'j', '̪', 'u', 'f']
#52

for line in fileinput.input(enfile):
    phonemes = PhoneConverter(line)
    SETP = list(set(SETP + phonemes))
print(SETP)
print(len(SETP))

# ['h', 'ʐ', 'a', 'æ', 'ʃ', 'ɪ', '2', 'ɐ', 'l', ' ', '7', 'm', 'w', 'ɛ', 'n', 'ð', 'o', '5', 'ɔ', 'ɡ', 'ɑ', ':', 'd', 'θ', 'ʊ', 'ʒ', 'ɗ', ';', 'y', 'k', 't', 'ɒ', 'b', 'j', '6', 'ʌ', 'ʂ', '1', 'ː', 'c', 'ɣ', 'x', 'ə', 'e', 'ɹ', 'p', '̪', 'ɲ', ',', '?', 'v', '4', 'ŋ', 'ɜ', 'z', 'f', 'i', 'u', 's', '!', 'r', '.', 'ɕ']
# 63