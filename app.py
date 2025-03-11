# app.py
import os
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# --- Configuration ---
# Define the path to the data directory relative to app.py
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# Update Flask app to use the defined template folder
app.template_folder = TEMPLATE_DIR
app.static_folder = STATIC_DIR


# --- Routes ---
@app.route("/")
def index():
    """
    Route for the root URL ("/").
    Renders the index.html template, which is the main dashboard page.
    """
    return render_template('index.html')

@app.route("/api/marketShare")
def get_market_share():
    """
    API endpoint for fetching market share data.
    Reads data from marketShare.json and returns it as JSON.
    """
    market_share_file = os.path.join(DATA_DIR, 'marketShare.json')
    try:
        with open(market_share_file, 'r') as f:
            market_share_data = json.load(f)
        return jsonify(market_share_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data file"}), 500

@app.route("/api/revenueTrends")
def get_revenue_trends():
    """
    API endpoint for fetching revenue trends data.
    Reads data from revenueTrends.json and returns it as JSON.
    """
    revenue_trends_file = os.path.join(DATA_DIR, 'revenueTrends.json')
    try:
        with open(revenue_trends_file, 'r') as f:
            revenue_trends_data = json.load(f)
        return jsonify(revenue_trends_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data file"}), 500

@app.route("/api/marketSegmentation")
def get_market_segmentation():
    """
    API endpoint for fetching market segmentation data.
    Reads data from marketSegmentation.json and returns it as JSON.
    """
    market_segmentation_file = os.path.join(DATA_DIR, 'marketSegmentation.json')
    try:
        with open(market_segmentation_file, 'r') as f:
            market_segmentation_data = json.load(f)
        return jsonify(market_segmentation_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data file"}), 500

# --- Static Files Serving (Optional, if you have files in 'static' folder like CSS, images etc.) ---
# Flask automatically serves files from a directory named 'static' in the same directory as your script.
# If you need to customize the URL or directory name, you can use:
# @app.route('/static/<path:filename>')
# def serve_static(filename):
#     static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
#     return send_from_directory(static_dir, filename)


if __name__ == '__main__':
    app.run(debug=True) # Set debug=False in production


"""
Recommended Repository Structure:

Your GitHub repository should be structured to keep everything organized. A good structure would be:

your-repo-name/
├── app.py          (Flask application file)
├── templates/      (Folder for HTML templates)
│   └── index.html  (Dashboard HTML file)
├── data/         (Folder for JSON data files)
│   ├── marketShare.json
│   ├── revenueTrends.json
│   └── marketSegmentation.json
├── static/       (Optional folder for static assets like CSS, JS, images)
│   └── (your static files if any, e.g., styles.css)
├── README.md       (Project description and instructions)
└── requirements.txt (List of Python dependencies, e.g., Flask)

Explanation:
- Root Directory (your-repo-name/): Contains all project files.
- app.py: The main Flask application script.
- templates/: Holds the HTML template files. 'index.html' is placed here.
- data/: Contains the JSON data files used by the application.
- static/:  If you have any static files like CSS stylesheets, JavaScript files (other than D3.js which is loaded from CDN), or images, they go in this folder.  Although not explicitly required in this problem, it's good practice to include it for future scalability.
- README.md:  A Markdown file to describe your project, how to set it up, and how to run it.  Very important for making your project understandable to others (and your future self!).
- requirements.txt: Lists the Python packages your project depends on (in this case, likely just Flask). This is used by pip to easily install all dependencies. You can generate this file by running `pip freeze > requirements.txt` in your project's root directory after installing Flask.

This structure keeps your application code, templates, data, and static assets logically separated, making the project easier to manage and maintain.
"""
