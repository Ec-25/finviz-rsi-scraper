# Finviz RSI Scraper

A simple Python script that retrieves the **RSI (14)** indicator for a list of stock tickers using the `finvizfinance` library and exports the results to a CSV file.

## Features

* Reads stock tickers from a CSV file.
* Retrieves the **RSI (14)** value for each ticker from Finviz.
* Exports the results as a semicolon-separated CSV.
* Handles missing or unavailable RSI values gracefully.
* Includes a temporary workaround for the current `finvizfinance` issue (see `PATCH_FINVIZFINANCE.md`).

## Requirements

* Python 3.10+
* Internet connection

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Important

The current version of `finvizfinance` is incompatible with the latest Finviz website layout.

Before running the script, apply the temporary patch described in:

```text
PATCH_FINVIZFINANCE.md
```

This patch can be removed once the upstream fix is released.

## Input

Create a file named:

```text
tickers.csv
```

using semicolons (`;`) as separators.

Example:

```text
AAPL;MSFT;TSLA
```

The repository includes a sample file:

```text
tickers.example.csv
```

Simply rename or copy it to `tickers.csv`.

## Running

Execute:

```bash
python main.py
```

## Output

A CSV file named like:

```text
results_YYYY-MM-DD_HH-MM.csv
```

Example:

```text
ticker;rsi
AAL;77.35
AAP;57.57
AAPL;37.15
ABBV;73.39
ABEV;55.37
BPA11;?
```

A value of `?` indicates that the RSI could not be retrieved for that ticker.

## Project Structure

```text
.
├── main.py
├── requirements.txt
├── tickers.example.csv
├── PATCH_FINVIZFINANCE.md
├── LICENSE
└── README.md
```

## Dependency

This project uses:

* `finvizfinance`

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
