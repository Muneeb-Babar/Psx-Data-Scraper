# PSX Market Summary Scraper

This Python script scrapes all the market summary tables from the Pakistan Stock Exchange (PSX) website and saves them into a single CSV file.

## Features

* Extracts all tables inside `.table-responsive` containers.
* Waits for content to load using Selenium WebDriver.
* Cleans and saves the combined table data to `psx_all_tables.csv`.

## Requirements

* Python 3.x
* Google Chrome
* ChromeDriver

Install the required Python packages using pip:

pip install selenium pandas

## How to Run

1. Clone or download this repository.
2. Edit the `CHROMEDRIVER_PATH` variable in `main.py` to match the path to your ChromeDriver. Example:

CHROMEDRIVER\_PATH = r"c:\Users\YourName\Downloads\chromedriver-win64\chromedriver.exe"

3. Run the script:

python main.py

## Output

The script creates a file named `psx_all_tables.csv`, which contains all table data combined in one place.

Example CSV output:

SCRIP,LDCP,OPEN,HIGH,LOW,CURRENT,CHANGE,VOLUME
ABC,101.00,103.00,105.00,99.00,104.50,+3.50,250000
XYZ,98.00,97.50,100.00,96.00,99.00,+1.00,300000

## Author

Muneeb Babar
BS Computer Science
Hackathon Participant | MERN Stack Developer

## License

This project is free to use for learning and development purposes.

