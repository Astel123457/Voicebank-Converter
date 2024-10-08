import os
import shutil
import main_converter
import argparse

AUDIO = ["wav", "flac", "aif", "aiff", "aifc", "mp3"]
FRQ = ["frq", "llsm", "dio", "ctspec", "sc.npz", "sc"]


def main(path, mode):
    bankname = path.split("\\")[-1]  # Get the name of the voicebank folder to use as the name of the new folder
    paths = os.listdir(path)
    print(f"Scanning {path}")
    mode = mode.lower()
    print("Converting...")
    try:
        os.mkdir(f".\\{bankname}_{mode}")  # Create a new folder for the converted files if it does not exist
    except FileExistsError:
        pass  # If it does exist, this is okay
    for i in paths:
        try:
            old = i
            ext = i.split(".")[-1]
            oto = [] # this is incase there is an oto
            if old == "oto.ini":
                with open(old, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        wav, data = line.split("=")
                        if mode == "hiragana":
                            for key in main_converter.hir_dict.keys():
                                wav = wav.replace(key, main_converter.hir_dict[key])
                            wav = wav.replace(".わv", ".wav")
                        elif mode == "romaji":
                            for key in main_converter.rom_dict.keys():
                                wav = wav.replace(key, "-" + main_converter.rom_dict[key])

                            if wav.startswith("_-"):
                                wav = wav.replace("_-", "_")

                            if i.startswith("-"):
                                wav = wav[1:]
                        oto.append(f"{wav}={data}")
            if ext not in AUDIO and ext not in FRQ:
                pass  # don't convert if not an audio file, frq file, or ini file
            elif mode == "hiragana":
                for key in main_converter.hir_dict.keys():
                    i = i.replace(key, main_converter.hir_dict[key])
                i = i.replace("_", "")
                i = i.replace(".わv", ".wav")
                i = i.replace("flあc", "flac")
                i = i.replace("わv.frq", "_wav.frq")
                i = i.replace("わv.llsm", "wav.llsm")
                i = i.replace(".あいf", ".aif")
                i = i.replace("あいf.frq", "_aif.frq")
                i = i.replace("あいf.llsm", "aif.llsm")
                i = i.replace(".あいff", ".aiff")
                i = i.replace("あいff.frq", "_aiff.frq")
                i = i.replace("あいff.llsm", "aiff.llsm")
                i = i.replace(".あいfc", ".aifc")
                i = i.replace("あいfc.frq", "_aifc.frq")
                i = i.replace("あいfc.llsm", "aifc.llsm")
                i = "_" + i
                i = i.replace("_でsc.mrq", "desc.mrq")
                i = i.replace("_おと.いに", "oto.ini")
            elif mode == "romaji":
                for key in main_converter.rom_dict.keys():
                    i = i.replace(key, "-" + main_converter.rom_dict[key])

                if i.startswith("_-"):
                    i = i.replace("_-", "_")

                if i.startswith("-"):
                    i = i[1:]
            else:
                print("No valid conversion mode specified!")

            # finally, copy the file to the new folder
            if len(oto) > 0:
                with open(f".\\{bankname}_{mode}\\" + "oto.ini", "w") as f:
                    f.writelines(oto)
            shutil.copy(path + "\\" + old, f".\\{bankname}_{mode}\\" + i)
        except FileNotFoundError:
            print(f"File not found? Skipping {old}")
        except PermissionError:
            print(f"Permission error. Skipping {old}")
        except:
            print(f"Unknown error. Skipping {old}")
    print(f"Converted {bankname}. {mode.title()} files are in \"{bankname}_{mode}\".")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Voicebank-Converter",
        description="Converts UTAU voicebank sample filenames from Hiragana to Romaji, or vice versa."
    )

    parser.add_argument(
        "path",
        help="Path to the voicebank folder.",
        nargs="+",
        type=str
    )

    parser.add_argument(
        "mode",
        help="Conversion mode. Either 'hiragana' or 'romaji'.",
        nargs=1,
        type=str,
        choices=["hiragana", "romaji"]
    )

    args = parser.parse_args()
    for i in args.path:
        main(i, args.mode[0])
