# zero-width-lib-python

<p align="center">
  <img width="150" height="150" src="https://user-images.githubusercontent.com/6414178/44472944-dd525880-a661-11e8-9c56-3e73395109c3.png">
</p>

## What's zero-width-lib
Zero-width-lib is a library for manipulating zero width characters (ZWC), which are non-printing and invisible chars.

The common usage of ZWC includes fingerprinting confidential text, embedding hidden text and escaping from string matching (i.e. regex)...

The lib is inspired by this great [medium article](https://medium.com/@umpox/be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters-18b4e6f17b66) and got the following features:

1. 💯stable & cover full test cases
2. 😆support full width Unicode chars 
3. ⚡️dependencies & performance considered
4. 📦support CJS, ESM and UMD

Forked from [this](https://github.com/yuanfux/zero-width-lib) JavaScript implementation. 

**WARNING**: Not 100% compatible with original implementation.
## Install
```
pip install zero_width_lib
```

## Usage
```python3
import zero_width_lib as zwlib
# or
from zero_width_lib import *
```
```python3
# note * represents the invisible ZWC
# U+ represents the Unicode for the character

# 0. six different zwc
my_dict = zwlib.zeroWidthDict
print(my_dict.zeroWidthSpace)  # '*' U+200B
print(my_dict.zeroWidthNonJoiner)  # '*' U+200C
print(my_dict.zeroWidthJoiner)  # '*' U+200D
print(my_dict.leftToRightMark) # '*' U+200E
print(my_dict.rightToLeftMark)  # '*' U+200F
print(my_dict.zeroWidthNoBreakSpace)  # '*' U+FEFF

# 1. convert text
text = 'text'
zwc = zwlib.t2z(text)  # '********'
back = zwlib.z2t(zwc)  # 'text'

# 2. embed hidden text
visible = 'hello world'
hidden = 'transplanted by @shacha086'
encoded = zwlib.encode(visible, hidden)  # 'h*********ello world'
decoded = zwlib.decode(encoded)  # 'transplanted by @shacha086'

# 3. extract ZWC from text
extracted = zwlib.extract(encoded)
vis = extracted.vis  # 'hello world'
hid = extracted.hid  # '*********'

# 4. escape from string matching
forbidden = 'forbidden'
escaped = zwlib.split(forbidden)  # 'f*o*r*b*i*d*d*e*n*' 
```

## License
MIT
