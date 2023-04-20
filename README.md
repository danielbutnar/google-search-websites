# Google Search Websites

A Python script to search Google for specific terms within a predefined set of websites, such as Stack Overflow, GitHub, and Quora.

## Installation

1. Clone or download the repository to your local machine.

2. Make sure you have Python installed. You can download Python from the [official website](https://www.python.org/downloads/).

3. Install any required packages, if needed.

## Usage

To use the script, navigate to the directory containing the script and run the following command:

python google_search_websites.py "your search query"


Replace "your search query" with the term you want to search for.

## Automation

### Windows

1. Create a new `.cmd` file (e.g., `google-search.cmd`) with the following content:

```cmd
@echo off
python "C:\path\to\google_search_websites.py" %*
Replace C:\path\to\ with the actual path to the directory containing the google_search_websites.py script.

Press Win + X and select "System." Click on "Advanced system settings" and then click on "Environment Variables."

In the "System variables" section, find the "Path" variable, select it, and click "Edit."

Click "New" and add the path to the directory containing the google-search.cmd file (e.g., C:\scripts\).

Click "OK" to save the changes.

Now you can use the google-search command followed by your search query in the Command Prompt.

macOS and Linux
Open your terminal and run the following command to create an alias for the script:
bash
Copy code
echo 'alias google-search="python /path/to/google_search_websites.py"' >> ~/.bashrc
Replace /path/to/ with the actual path to the directory containing the google_search_websites.py script.

Run source ~/.bashrc to apply the changes to the current session.
Now you can use the google-search command followed by your search query in the terminal.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

This README file provides information on the purpose of the script, installation instructions, usage instructions,
and a guide to automating the process on Windows, macOS, and Linux. You can customize the file as needed to better
suit your specific project.

