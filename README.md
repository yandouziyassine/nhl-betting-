# Live NHL Betting Odds Calculator

A Python program that calculates real-time betting odds for NHL games using live statistics from the NHL API and historical data stored in an Excel sheet. 

---

## Project Overview
This tool combines **live game data** (fetched via the NHL API) and **historical team statistics** (stored in an Excel file) to compute dynamic betting odds for two competing NHL teams. The odds are calculated using a customizable formula that factors in team performance metrics, historical trends, and real-time gameplay statistics.

**Disclaimer**: This project is intended for educational purposes only. Gambling involves risks, and this tool does not guarantee accuracy.

---

##  Features
- *Live Data Fetching**: Pulls real-time game statistics (e.g., shots on goal, possession time, penalties) using the NHL API.
- *Historical Data Integration**: Loads team performance history (e.g., win/loss records, head-to-head stats) from an Excel file.
- *Dynamic Odds Calculation**: Applies a weighted formula to compute betting odds based on live and historical data.
- *Simple CLI Output**: Displays calculated odds in an easy-to-read format.

---

## Prerequisites
- Python 3.8+
- Required Python libraries: `pandas`, `requests`, `openpyxl`
- Access to the [NHL API]
- An Excel file (`historical_data.xlsx`) containing historical team data (see [Data Format](#data-format)).

---
You are allowed to:
🛠 Modify the code for personal or commercial use.

📦 Redistribute the software (with proper attribution).

🔄 Integrate this tool into other projects.


Yassine Yandouzi
