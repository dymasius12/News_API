
# NewsAPI Python Project

This script allows you to fetch the latest news for a given stock company name using the NewsAPI.

## Requirements

- Python 3.x
- `requests` library

## Setup

1. Install the required libraries:

```bash
pip install requests
```

2. Set up a configuration file (`config.ini`) in the same directory as `NewsAPI.py`. This file should contain your NewsAPI API key.

```
[NewsAPI]
API_KEY = YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your actual API key.

**Warning**: Never commit your API keys or sensitive information directly in your scripts or on public repositories.

## Usage

Run the script and provide a stock company name as input:

```bash
python NewsAPI-Python_Wrapper.py
```

Follow the on-screen instructions to input the stock company name and get the latest news.
