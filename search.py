import argparse
import urllib.parse
import webbrowser

def google(message):
    """
    Perform a Google search for the given message within a set of predefined websites.

    :param message: The search query to use.
    """
    websites = ['stackoverflow.com', 'github.com', 'quora.com']
    query = 'site:' + ' OR site:'.join(websites) + ' ' + message
    encoded_query = urllib.parse.quote_plus(query)
    search_url = 'https://www.google.com/search?q=' + encoded_query
    webbrowser.open_new_tab(search_url)

def main():
    """
    The main function that sets up argument parsing, parses the command-line arguments,
    and calls the google function with the provided search term.
    """
    parser = argparse.ArgumentParser(description="Search Google for specific websites")
    parser.add_argument("search_term", help="The search term to query")
    args = parser.parse_args()

    google(args.search_term)

if __name__ == "__main__":
    main()
