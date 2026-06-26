# Author: ec25
# Date: 2026-06-26
# Description: Script to process and save the RSI of the received tickers as CSV
# Version: 0.3
# Licence: MIT

import csv
from time import sleep
from datetime import datetime
from os import path as os_path
from finvizfinance.quote import finvizfinance


def get_rsi(ticker: str) -> str:
    """Return the RSI (14) of `ticker` on the Finviz Finance service"""
    if ticker == "":
        raise Exception("Ticker is empty")
    try:
        stock = finvizfinance(ticker)
        data = stock.ticker_fundament()
        # Temporary workaround for finvizfinance bug.
        # Remove once PR #155 is merged.
        rsi = data.get("RSI (14)", "?")
        return str(rsi)
    except Exception as e:
        print(e)
        return "?"


def load_tickers() -> list[str]:
    """Load the tickers from the `tickers.csv` file"""
    if not os_path.exists("tickers.csv"):
        raise Exception("tickers.csv not found")

    tickers = []

    with open("tickers.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            tickers.extend(ticker.strip() for ticker in row if ticker.strip())

    return tickers


def save_results_as_csv(results: list[dict[str, str]]) -> None:
    """Save the results to the `results_%Y-%m-%d_%H-%M.csv` file with semicolon as separator"""
    filename = f"results_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["ticker", "rsi"], delimiter=";")
        writer.writeheader()
        writer.writerows(results)

    return


def app() -> str:
    """
    Main App

    Returns:
        str: Message resulting from the processing of tickers in finviz.
    """
    exit_msg = ""

    try:
        tickers = load_tickers()
        if len(tickers) == 0:
            raise Exception("No tickers found in tickers.csv")

        result = []
        for i, ticker in enumerate(tickers, start=1):
            if i % 20 == 0:
                print(f"Processed {i}/{len(tickers)}")
                print("Waiting 1 second...")
                sleep(1)

            rsi = get_rsi(ticker)
            if rsi == "?":
                exit_msg += f"RSI not found for {ticker}\n"

            result.append({"ticker": ticker, "rsi": rsi})

        save_results_as_csv(result)
        exit_msg += "Successfully Processed!"

    except Exception as e:
        exit_msg += f"Error: {e}"

    return exit_msg


if __name__ == "__main__":
    info = app()
    print(info)
    input("Press Enter to exit...")
