import requests
import xml.etree.ElementTree as ET
from flask import Flask, render_template

app = Flask(__name__)

# RSS feed URL from where the live cricket scores are fetched
RSS_FEED_URL = "https://static.cricinfo.com/rss/livescores.xml"

def parse_rss_feed():
    """
    Fetches and parses the RSS feed to extract live cricket scores.
    """
    try:
        # Fetch the RSS feed content
        response = requests.get(RSS_FEED_URL)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the XML content
        root = ET.fromstring(response.content)
        
        # Use a set to keep track of unique match titles to avoid duplicates
        unique_titles = set()
        matches = []
        for item in root.findall('.//item'):
            original_title = item.find('title').text
            # Clean the title for duplicate checking: remove apostrophes, strip whitespace, and convert to lowercase
            cleaned_title = original_title.replace("'", "").strip().lower()
            
            # If the cleaned title is not already in the set, add it and the original match details
            if cleaned_title not in unique_titles:
                unique_titles.add(cleaned_title)
                description = item.find('description').text
                matches.append({'title': original_title, 'description': description})
        
        return matches, None
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        error_message = f"Error fetching RSS feed: {e}"
        return None, error_message
    except ET.ParseError as e:
        # Handle XML parsing errors
        error_message = f"Error parsing RSS feed: {e}"
        return None, error_message

@app.route('/')
def home():
    """
    Renders the home page with live cricket scores.
    """
    # Fetch and parse the RSS feed
    matches, error = parse_rss_feed()
    
    # Render the template with the fetched data or an error message
    return render_template('index.html', matches=matches, error=error)

@app.route('/guide')
def guide():
    """
    Renders the help/guide page explaining how to read cricket scores.
    """
    return render_template('guide.html')

if __name__ == '__main__':
    app.run(debug=True)