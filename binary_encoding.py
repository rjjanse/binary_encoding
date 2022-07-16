###############################
# Binary interpreter
# Roemer J. Janse - 16/07/2022
###############################

### Binary to text
def bin_to_txt(binary):
    ##### 0. Import libraries
    import pandas as pd

    ##### 1. Create dataframe with ASCII encodings
    # Set-up ASCII data for dataframe
    dec = range(32, 127)
    char = [" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4",
            "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[",
            r"\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

    dat_ascii = {"dec": dec, "char": char}

    # Create dataframe with ASCII data
    df_ascii = pd.DataFrame(dat_ascii)

    # # Set Pandas to print all rows of dataframe, print dataframe, and reduce max rows printed again to 10 (default)
    # pd.set_option("display.max_rows", None)
    # print(df_ascii)
    # pd.set_option("display.max_rows", 10)

    ##### 2. Binary-to-text
    # Load in binary
    binar = binary

    # Remove any spaces
    binar = binar.replace(" ", "")

    # Split binary into bytes (8 bits or numbers) using loop
    sby = []
    items = len(binar) / 8

    for chk in range(0, int(items)):
        # Append subsets of object binary to list sby
        sby.append(binar[chk + (chk * 7):(chk + (chk * 7) + 7 + 1)])

    # Change each byte to decimal number using loop
    sdec = []

    for byte in range(0, len(sby)):
        # Append converted decimals to list sdec
        sdec.append(
            # Calculate decimal
            int(sby[byte][0]) * 128 + int(sby[byte][1]) * 64 + int(sby[byte][2]) * 32 + int(sby[byte][3]) * 16 +
            int(sby[byte][4]) * 8 + int(sby[byte][5]) * 4 + int(sby[byte][6]) * 2 + int(sby[byte][7]) * 1
        )

    # Match decimal numbers with characters from ASCII dataframe
    conv = ""

    for decimal in range(0, len(sdec)):
        # For each decimal find corresponding character and add to conv
        conv += df_ascii["char"][  # Column char is extracted
            (df_ascii[df_ascii["dec"] == sdec[decimal]  # Logical test
                      ].index[0])]  # Returned index number is indexed at first location to get row number

    print(conv)

### Text to binary
def txt_to_bin(text, bytes = True):
    ##### 0. Import libraries
    import pandas as pd

    ##### 1. Create dataframe with ASCII encodings
    # Set-up ASCII data for dataframe
    dec = range(32, 127)
    char = [" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4",
            "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[",
            r"\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

    dat_ascii = {"dec": dec, "char": char}

    # Create dataframe with ASCII data
    df_ascii = pd.DataFrame(dat_ascii)

    # # Set Pandas to print all rows of dataframe, print dataframe, and reduce max rows printed again to 10 (default)
    # pd.set_option("display.max_rows", None)
    # print(df_ascii)
    # pd.set_option("display.max_rows", 10)

    ##### 2. Text-to-binary encoding
    # Load in text
    txt = text

    # Indicate if binary should be given with bytes seperated or not
    byte_sep = bytes

    # Create list of decimal numbers corresponding to character
    declist = []

    for c in txt:
        declist.append(
            df_ascii["dec"][
                (df_ascii[df_ascii["char"] == c
                          ].index[0])]
        )

    # Convert decimals to binary
    binlist = []

    for d in declist:
        binlist.append(
            bin(d).replace("0b", "").rjust(8, "0")
        )

    # Print result based on if bytes should be seperated
    conv = ""

    if byte_sep:
        for i in binlist:
            conv += i + " "

        conv = conv[1:len(conv) - 1]

    else:
        for i in binlist:
            conv += i

    print(conv)
