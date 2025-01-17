from flask import Flask, render_template_string, send_file
import markdown
import os

app = Flask(__name__)

# Minimalist template for displaying the Markdown
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Markdown Server</title>
</head>
<body>
    <div>{{ content|safe }}</div>
</body>
</html>
"""

# Global configuration for the Markdown file path
markdown_file = None

@app.route("/")
def render_markdown():
    if markdown_file and os.path.exists(markdown_file):
        with open(markdown_file, "r", encoding="utf-8") as f:
            md_content = f.read()
            html_content = markdown.markdown(md_content)
        return render_template_string(HTML_TEMPLATE, content=html_content)
    else:
        return "Markdown file not found.", 404

@app.route("/download")
def download_markdown():
    if markdown_file and os.path.exists(markdown_file):
        return send_file(markdown_file, as_attachment=True)
    else:
        return "Markdown file not found.", 404

def run_server(md_path):
    global markdown_file
    if not os.path.exists(md_path):
        raise FileNotFoundError(f"The file '{md_path}' was not found.")
    markdown_file = md_path
    app.run(debug=True)

