# Voicebank-Converter
A pure Python converter to convert UTAU voicebank samples from hiragana to romaji (and vice versa).

# Usage
```cl
python main.py path [path ...] {hiragana, romaji}
```

There are 2 conversion modes: "hiragana" or "romaji".  
"hiragana" will convert the wav files in the path to hiragana. (i.e. "_a-a-i-a-u-e-a" -> "_ああいあうえあ")  
"romaji" will do the opposite. (i.e. "_ああいあうえあ" -> "_a-a-i-a-u-e-a")

The script can convert more than one path at once.

# Example

```cl
python main.py "C:\OpenUTAU\Singers\test_bank" hiragana

Scanning "C:\OpenUTAU\Singers\test_bank"
Converting...
Converted test_bank. Hiragana files are in "test_bank_hiragana".
```

```cl
python main.py "C:\OpenUTAU\Singers\bankone" "C:\OpenUTAU\Singers\banktwo" romaji

Scanning "C:\OpenUTAU\Singers\bankone"
Converting...
Converted bankone. Romaji files are in "bankone_romaji".
Scanning "C:\OpenUTAU\Singers\banktwo"
Converting...
Converted banktwo. Romaji files are in "banktwo_romaji".
```