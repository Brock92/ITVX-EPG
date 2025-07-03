import urllib.request
import gzip
import shutil

# Download the EPG XML file
xml_url = "https://raw.githubusercontent.com/dp247/Freeview-EPG/master/epg.xml"
xml_filename = "guide.xml"
gz_filename = "guide.xml.gz"

# Fetch XML
print("Downloading EPG...")
urllib.request.urlretrieve(xml_url, xml_filename)

# Compress to .gz
print("Compressing to .gz...")
with open(xml_filename, 'rb') as f_in:
    with gzip.open(gz_filename, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("EPG downloaded and compressed.")
