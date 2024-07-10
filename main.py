import subprocess
import shutil
import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Check if wget is installed
if shutil.which("wget") is None:
    print("wget is not installed. Installing wget...")
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", "-y", "wget"])

# Define XMRig version
XMRIG_VERSION = "6.18.0"
XMRIG_TAR = f"xmrig-{XMRIG_VERSION}-linux-x64.tar.gz"
XMRIG_DIR = f"xmrig-{XMRIG_VERSION}"

# Download XMRig
print(f"Downloading XMRig version {XMRIG_VERSION}...")
subprocess.run(["wget", f"https://github.com/xmrig/xmrig/releases/download/v{XMRIG_VERSION}/{XMRIG_TAR}"])

# Extract XMRig
print("Extracting XMRig...")
subprocess.run(["tar", "-zxvf", XMRIG_TAR])

# Navigate to the XMRig directory
os.chdir(XMRIG_DIR)

# Run XMRig with parameters for unMineable BCH mining
print("Starting XMRig for BCH mining on unMineable...")
process = subprocess.Popen(["./xmrig", "-o", "rx.unmineable.com:3333", "-a", "rx", "-k", "-u", "BCH:qqe3cudqxmc498e7nza7rfwajjyeh6x3nghsvtm39p.pc#xnsub"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

@app.route('/')
def index():
    # Read the output from the XMRig process
    output = process.stdout.readline()
    
    # Define the HTML template
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>XMRig Status</title>
    </head>
    <body>
        <h1>XMRig Status</h1>
        <pre>{{ output }}</pre>
    </body>
    </html>
    '''
    
    # Render the template with the XMRig output
    return render_template_string(template, output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
