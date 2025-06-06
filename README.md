# Kannadafy-deobfuscator

Kannadafy-deobfuscator is a Python tool designed to help reverse engineer and analyze Python scripts obfuscated using `exec` and non-ASCII character tricks (such as Kannada characters). The tool attempts to safely reveal the original source code by replacing dangerous `exec` calls with `print` and capturing the output.

## 🚨 Disclaimer

This tool is provided **for educational and research purposes only**. It is intended to help users understand obfuscation techniques and learn about code analysis.

You are **solely responsible** for how you use this software. By using this tool, you agree to the following:

- I (the creator of this tool) am **not responsible** for any misuse, damage, or legal issues arising from the use of this code.
- You must **not use this tool** to analyze, run, or modify any code you do not have permission to inspect.
- The code is **not intended** to be used for malicious purposes.
- Always comply with your local laws, licenses, and intellectual property regulations.

If you're unsure whether your use is legal or ethical, **stop and seek proper guidance.**

## 🔍 Features

- Parses and modifies obfuscated Python scripts without directly altering the original file.
- Replaces dangerous `exec(...)` calls with `print(...)` to safely view hidden code.
- Captures and saves the revealed source code in a separate `.py` file.
- Optionally allows running the original file (with caution).

## 📦 Requirements

- Python 3.6+
- `astor` (install via `pip install astor`)

## 🚀 How to Use

1. Clone this repository or download the script.
2. Place the obfuscated Python script you want to analyze in the same folder.
3. Run the tool:

```bash
python Kannadafy-deobfuscator.py
