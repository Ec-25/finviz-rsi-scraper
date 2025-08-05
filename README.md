# rsi-data-export

Python script to fetch the RSI (Relative Strength Index) of a list of tickers using the [`finvizfinance`](https://github.com/lit26/finvizfinance) library and export it to a CSV file.

## 🔍 What does it do?

Reads tickers from a `tickers.txt` file, fetches their RSI (14) from Finviz, and saves the results in a CSV with the following format:

```
ticker;rsi
AAPL;47.32
GOOGL;63.21
...
```

## 📦 Requirements

- Python 3.10+
- [finvizfinance](https://pypi.org/project/finvizfinance/)

Quick install:

```bash
pip install finvizfinance
```

## 🚀 How to use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rsi-data-export.git
   cd rsi-data-export
   ```

2. Start the virtual environment and install the requirements.
   ```bash
   python -m venv env
   .\env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `tickers.txt` file in the same directory, with tickers separated by semicolons:
   ```
   AAPL;GOOGL;MSFT;TSLA
   ```

4. Run the script:
   ```bash
   python main.py
   ```

5. A file named `results_YYYY-MM-DD_HH-MM.csv` will be generated with the fetched RSI data.
