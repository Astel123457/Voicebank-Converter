import sys
import os
import shutil
import main_converter

def main(path, mode):
    paths = os.listdir(path)
    print(f"Scanning {path}")
    mode = mode.lower()   
    print("Converting...") 
    for i in paths:
        old = i
        if mode == "hiragana":
            for key in main_converter.hir_dict.keys():
                i = i.replace(key, main_converter.hir_dict[key])
            i = i.replace("_", "")
            i = i.replace(".わv", ".wav")
            i = i.replace("わv.frq", "_wav.frq")
            i = i.replace("わv.llsm", "wav.llsm")
            i = "_" + i
            i = i.replace("_でsc.mrq", "desc.mrq")
            i = i.replace("_おと.いに", "oto.ini")
            shutil.copy(path + "\\" + old, ".\\output\\" + i)
        elif mode == "romaji":
            for key in main_converter.rom_dict.keys():
                i = i.replace(key, "-" + main_converter.rom_dict[key])
            if i.startswith("_-"):
                i = i.replace("_-", "_")
            if i.startswith("-"):
                i = i[1:]
            shutil.copy(path + "\\" + old, ".\\output\\" + i)
        else:
            print("No valid conversion mode specified!")
    print("Done")

    # f = open(path, "r")
    # strings = f.read()
    # if mode == "hiragana":
    #     strings = strings.lower()
    #     for key in main_converter.hir_dict.keys():
    #         strings = strings.replace(key, main_converter.hir_dict[key])
    #     strings = strings.replace("-", "")
    #     strings = strings.replace("_", "")
    #     print(strings)
    # elif mode == "romaji":
    #     for key in main_converter.rom_dict.keys():
    #         strings = strings.replace(key, "-" + main_converter.rom_dict[key])
    #     if string.startswith("_-"):
    #         string.replace("_-", "_")
    #     print(strings)



if __name__ == "__main__":
    path = sys.argv[1]
    mode = sys.argv[2]
    main(path, mode)