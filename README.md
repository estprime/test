# CSV Payment Converter

This repository contains a Python script `convert_csv.py` that converts the payment method column (column E) in a CSV file to numeric codes based on a predefined mapping.

## Payment Method Mapping

```
代引き          -> 0
クレジットカード -> 1
銀行振込        -> 2
```

## Usage

1. Install the required dependency:

```bash
pip install pandas
```

2. Run the converter script:

```bash
python convert_csv.py
```

A small window will open. Select the CSV file you want to convert, then choose where to save the converted file. The script will replace values in the fifth column (column E) according to the mapping and save the result.
