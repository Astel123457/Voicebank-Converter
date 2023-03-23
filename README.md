# Voicebank-Converter
A python converter to convert UTAU voicebanks to hiragana from romaji (and vice versa)
# How to use
The Converter only requires 2 positional arguments, the folder location, and the conversion mode
```cl
python main.py <folder_path> <conversion_mode>
```

There are 2 conversion modes, "hiragana" and "romaji". "hiragana" will convert the wav files in a voicebank to hiragana format ("_a-a-i-a-u-e-a" -> "_ああいあうえあ") and "romaji" will do the inverse ("_ああいあうえあ" -> "_a-a-i-a-u-e-a")
