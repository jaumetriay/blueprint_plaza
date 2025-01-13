#!/bin/bash

# Check if pv is installed
if ! command -v pv &> /dev/null; then
    echo "Installing pv for progress visualization..."
    sudo apt-get install pv
fi

# Initialize progress counter
total_steps=4
current_step=0

# Function to update progress
update_progress() {
    current_step=$((current_step + 1))
    echo "[$current_step/$total_steps] $1"
    echo $((current_step * 100 / total_steps)) | pv -qL 10
}

# Create HTML report
cat << EOF > security_report.html
<!DOCTYPE html>
<html>
<head>
    <title>Security Scan Report</title>
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 40px;
        background-color: #f0f2f5;
        color: #333;
        line-height: 1.6;
    }
    .container {
        max-width: 1200px;
        margin: 0 auto;
        background-color: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1 {
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
        margin-bottom: 30px;
        font-size: 2.5em;
        text-align: center;
    }
    h2 {
        color: #34495e;
        margin-top: 30px;
        font-size: 1.8em;
        padding-left: 15px;
        border-left: 5px solid #3498db;
    }
    pre {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 8px;
        overflow-x: auto;
        font-family: 'Consolas', 'Monaco', monospace;
        font-size: 14px;
        line-height: 1.5;
        border: 1px solid #e9ecef;
        box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);
    }
    .timestamp {
        color: #7f8c8d;
        font-style: italic;
        text-align: center;
        margin-bottom: 30px;
        font-size: 0.9em;
    }
    .section {
        margin: 30px 0;
        padding: 25px;
        background-color: white;
        border-left: 5px solid #3498db;
        border-radius: 0 8px 8px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }
    .section:hover {
        transform: translateX(5px);
    }
    /* Error and warning highlighting */
    .error {
        color: #dc3545;
        font-weight: bold;
    }
    .warning {
        color: #ffc107;
        font-weight: bold;
    }
    .success {
        color: #28a745;
        font-weight: bold;
    }
    /* Scrollbar styling */
    pre::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    pre::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    pre::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 4px;
    }
    pre::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
</style>
</head>
<body>
    <div class="container">
        <h1>🔍 Security Scan Report</h1>
        <p class="timestamp">Generated on $(date)</p>
EOF

# Run each check with progress update
echo "Starting security scan..."

update_progress "Running Pylint checks..."
echo '<div class="section"><h2>1. Pylint Code Quality Checks</h2><pre>' >> security_report.html
pylint . >> security_report.html 2>&1
echo '</pre></div>' >> security_report.html

update_progress "Running Bandit security checks..."
echo '<div class="section"><h2>2. Bandit Security Vulnerabilities</h2><pre>' >> security_report.html
bandit -r . -ll --exclude '/venv/,/static/,/templates/' -s B104 >> security_report.html 2>&1
echo '</pre></div>' >> security_report.html

update_progress "Running Safety checks..."
echo '<div class="section"><h2>3. Safety Dependency Checks</h2><pre>' >> security_report.html
safety check --short-report --ignore 40459 >> security_report.html 2>&1
echo '</pre></div>' >> security_report.html

update_progress "Running Pip-audit checks..."
echo '<div class="section"><h2>4. Pip-Audit Dependency Checks</h2><pre>' >> security_report.html
pip-audit >> security_report.html 2>&1
echo '</pre></div>' >> security_report.html

# Close HTML tags
echo '</div></body></html>' >> security_report.html

echo -e "✅ Security scan complete. \e]8;;file://$(pwd)/security_report.html\e\\Click here to open security_report.html\e]8;;\e\\"
echo "Or open: file://$(pwd)/security_report.html"