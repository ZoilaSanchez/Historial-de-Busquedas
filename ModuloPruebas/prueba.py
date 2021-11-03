import regex as re
import demoji
demoji.download_codes()

text = "given emojis😳 to text "
emojis = demoji.findall(text)
# Print converted emojis
print(emojis)