# EasyToUseQRCodeGenerator

You can use this script to generate custom QRCodes from links.

## Installation:
You may want to make a virtual environment to store the libraries

```bash
virtualenv <virtualenv_name>
```

```bash
source <virtualenv_name>/bin/activate
```

Install requirements:
```bash
pip3 install -r requirements.txt
```

## Usage
Generate QRCodes with default name
```bash
python3 qrcodegen.py <link>
```

Generate QRCodes with custom name
```bash
python3 qrcodegen.py <link> -o Rickroll
```

Generate QRCodes with custom complexity
```bash
python3 qrcodegen.py <link> -c 12
```
