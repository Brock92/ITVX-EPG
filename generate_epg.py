import urllib.request
import gzip
import shutil

xml_url = "https://raw.githubusercontent.com/dp247/Freeview-EPG/master/epg.xml"
xml_file = "guide.xml"
gz_file = "guide.xml.gz"

print("Downloading EPG XML...")
urllib.request.urlretrieve(xml_url, xml_file)

print("Compressing to GZ...")
with open(xml_file, 'rb') as f_in:
    with gzip.open(gz_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("EPG updated successfully.")
