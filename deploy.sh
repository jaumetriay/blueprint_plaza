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
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
        }
        pre {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
        }
        .timestamp {
            color: #7f8c8d;
            font-style: italic;
        }
        .section {
            margin: 20px 0;
            padding: 20px;
            background-color: white;
            border-left: 4px solid #3498db;
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
bandit -r . -ll --exclude '/venv/,/static/,/templates/' >> security_report.html 2>&1
echo '</pre></div>' >> security_report.html

update_progress "Running Safety checks..."
echo '<div class="section"><h2>3. Safety Dependency Checks</h2><pre>' >> security_report.html
safety check >> security_report.html 2>&1
echo '</pre></div>' >> security_report.html

update_progress "Running Pip-audit checks..."
echo '<div class="section"><h2>4. Pip-Audit Dependency Checks</h2><pre>' >> security_report.html
pip-audit >> security_report.html 2>&1
echo '</pre></div>' >> security_report.html

# Close HTML tags
echo '</div></body></html>' >> security_report.html

echo -e "✅ Security scan complete. \e]8;;file://$(pwd)/security_report.html\e\\Click here to open security_report.html\e]8;;\e\\"
echo "Or open: file://$(pwd)/security_report.html"