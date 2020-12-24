### Project combine vinorm and espeak

Vinorm for Vietnamese Text Normalization

Espeak for handling cross-language and convert text to phoneme 

```shell
pip install vinorm
```
Call function to convert Text to grapheme

```python
from VinormEspeak import PhoneConverter
phonemes = PhoneConverter("Vào tháng 12/2020 đã có vaccine phòng ngừa Covid-19")
```
Output of Vinorm and NormEspeak
```shell
vào tháng mười hai năm hai nghìn không trăm hai mươi đã có vaccine phòng ngừa covid mười chín . 
```
```
vaːʊ2 taːɜŋ myə2j haːɪ1 na1m haːɪ1 ŋi2n xo1 tʃa1m haːɪ1 myə1j ɗaː5 ɡɔɜ va1ksiː1n fɔ2 ŋyə2 kɒ1vɪ1d myə2j tɕiɜn  .
```

Get list of grapheme

```python
from VinormEspeak import getPhoneme
phonemeList = getPhoneme()
```