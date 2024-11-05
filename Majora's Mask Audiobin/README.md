# Generating a Majora's Mask Audiobin File for Ocarina of Time Randomizer
With version 8.3 and above of the Ocarina of TIme Randomizer, it is possible to use Majora's Mask Randomizer music files (`.mmrs`) alongside Ocarina of Time Randomizer music files (`.ootrs`).

To use Majora's Mask Randomizer music files with Ocarina of Time Randomizer you will need to use a decompressed Majora's Mask NTSC-U version 1.0 ROM to create and place a Majora's Mask audiobin file (`MM.audiobin`) into your local Ocarina of Time Randomizer installation's music folder.

This guide will help you through the process of decompressing a compressed Majora's Mask ROM file, and generating the audiobin file necessary to use Majora's Mask Randomizer music files (`.mmrs`) with Ocarina of Time Randomizer.

> [!TIP]
> If you wish to ensure that the ROM file you have is a compressed Majora's Mask NTSC-U version 1.0 ROM, you can check the ROM file's MD5 checksum with [this online checksum tool](https://emn178.github.io/online-tools/md5_checksum.html "Online Checksum Tool").
>
> The correct MD5 checksum for a compressed Majora's Mask NTSC-U version 1.0 ROM are listed below:
> ```
> MD5: 2A0A8ACB61538235BC1094D297FB6556
> ```

### Decompressing Your ROM

#### 1. Downloading z64decompress
Download the z64decompress executable file (`.exe`) from the [z64decompress GitHub releases page](https://github.com/z64utils/z64decompress/releases).

> [!NOTE]
> You do not need to use z64decompress, nDEC or a decompressed ROM created by decomp both work. ROM files decompressed with any option will match one another byte-for-byte. z64decompress is merely the easiest-to-use option.

#### 2. Using z64decompress
To decompress your compressed Majora's Mask ROM file with z64decompress, drag your ROM file onto the z64decompress executable file (`.exe`) — your ROM file *does not* need to be in the same folder as z64decompress for it to decompress your ROM file.

After dragging your compressed Majora's Mask ROM file onto the z64decompress executable file (`.exe`) a terminal window should pop up — you may close the terminal window whenever — and a decompressed copy of your ROM file should appear in the folder with your compressed ROM file with the following filename:
```
*.decompressed.z64
```

> [!IMPORTANT]
> For your compressed ROM file to be decompressed with z64compress it must be in the "Big Endian" byte order — indicated by the file extension `.z64`. If your ROM is not in the "Big Endian" byte order — indicated by either the  `.n64` (Little Endian) or `.v64` (Byteswapped) file extension — then you must use [Tool64](https://www.zophar.net/utilities/n64aud/tool-n64.html) to swap the byte order.
>
> Simply renaming the file extension will not change the byte order.

### Generating Your Audiobin File

#### 1. Downloading the Audiobin Generator Script
Download the `Generate MM Audiobin.py` script in the "Majora's Mask Audiobin" folder of this repository is the script to generate a Majora's Mask audiobin file.

#### 2. Generate Your Majora's Mask Audiobin File
To generate your Majora's Mask audiobin file (`MM.audiobin`), drag your decompressed Majora's Mask ROM file onto the `Generate MM Audiobin.py` script.

> [!IMPORTANT]
> *Do not* change the filename of the audiobin file from `MM.audiobin` to anything else — Ocarina of Time Randomizer specifically checks for a file called "`MM.audiobin`".

#### 3. Place MM.audiobin in Your Music Folder
After your Majora's Mask audiobin file (`MM.audiobin`) has been generated, place the audiobin file into your local Ocarina of Time Randomizer installation's music folder.

> [!NOTE]
> The music folder for a local installation of Ocarina of Time Randomizer is normally located at the following operating system path:
>
> **Windows:**
> ```
> C:\Users\<USERNAME>\AppData\Local\Programs\ootr-electron-gui\resources\app\python\data\Music
> ```

### Using Majora's Mask Music Files in Ocarina of Time Randomizer
With the Majora's Mask audiobin file in your music folder, you can now place any Majora's Mask Randomizer music file (`.mmrs`) into your music folder and have it be placed in an Ocarina of Time Randomizer seed like it would for a regular Ocarina of Time Randomizer music file (`.ootrs`).