# Live Cricket Scores

A lightweight Flask web application that displays live cricket match scores and updates fetched from ESPN Cricinfo's RSS feed. Stay updated with real-time cricket matches right from your browser.

## Features

- **Live Cricket Scores**: Real-time cricket match updates from ESPN Cricinfo
- **Clean Web Interface**: Simple and intuitive user interface for easy score tracking
- **Duplicate Prevention**: Automatically removes duplicate match entries
- **Error Handling**: Robust error handling for network and parsing issues
- **Help Guide**: Built-in guide page to help users understand cricket score terminology
- **No Database Required**: Lightweight application with minimal dependencies

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/live-cricket-scores.git
   cd live-cricket-scores
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **View live scores** on the home page or visit the guide page for help understanding cricket terminology

## Project Structure

```
live-cricket-scores/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   ├── index.html     # Home page template (displays live scores)
│   └── guide.html     # Help/guide page template
└── README.md          # This file
```

## Dependencies

- **Flask**: Web framework for building the application
- **requests**: HTTP library for fetching RSS feeds
- **xml.etree.ElementTree**: XML parsing (built-in Python library)

See `requirements.txt` for the complete list.

## API Information

This application fetches data from:
- **Source**: ESPN Cricinfo Live Scores RSS Feed
- **URL**: `https://static.cricinfo.com/rss/livescores.xml`

The feed is updated in real-time and provides match titles and descriptions.

## How It Works

1. The application fetches the latest RSS feed from ESPN Cricinfo
2. Parses the XML content to extract match information
3. Removes duplicate entries by cleaning and comparing match titles
4. Displays the unique matches on the home page
5. Handles errors gracefully if the feed cannot be accessed or parsed

## Features Explained

### Home Page (`/`)
- Displays all live cricket matches with current scores
- Updates by fetching the latest RSS feed
- Shows match title and description

### Guide Page (`/guide`)
- Provides help and instructions for reading cricket scores
- Useful for users unfamiliar with cricket terminology

## Error Handling

The application handles the following errors gracefully:
- **Network Errors**: When RSS feed cannot be fetched
- **XML Parsing Errors**: When feed content is malformed
- **Server Errors**: Displays user-friendly error messages

## Development

To run in development mode with auto-reload:
```bash
python app.py
```

The Flask development server will start on `http://localhost:5000` with debug mode enabled.

## Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This project uses data from ESPN Cricinfo's public RSS feed. Please ensure you comply with their terms of service when using this application.

## Support

For issues, suggestions, or questions, please open an issue on the GitHub repository.

## Future Enhancements

- Add caching to reduce API calls
- Implement score notifications
- Add filtering by team or match type
- Dark mode support
- Mobile app version