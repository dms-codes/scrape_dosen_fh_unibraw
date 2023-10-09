import requests
from bs4 import BeautifulSoup as bs
import csv

# Constants
BASE_URL = "https://hukum.ub.ac.id/profil-dosen-2/"
TIMEOUT = 30
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

# Function to extract and clean text from an element
def extract_text(element):
    if element:
        return element.text.strip()
    return ''

# Function to extract education, research, publication, and books information
def extract_info(section):
    result = ""
    for item in section.find_all("div", class_="contentDetails"):
        university = extract_text(item.find("strong"))
        details = extract_text(item.find("p", class_="subDetails"))
        result += f"{university}\n{details}\n"
    return result

# Initialize a session
s = requests.Session()

# Fetch the HTML content
html = s.get(BASE_URL, timeout=TIMEOUT, headers=HEADERS).content
soup = bs(html, 'html.parser')

# Open a CSV file for writing
with open('data_dosen_fh_unibraw.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['Name', 'Title', 'Sub', 'Profile URL', 'Img URL', 'NIP', 'Email', 'Education', 'Research', 'Publication', 'Books']
    writer.writerow(header)

    # Find professor containers
    containers = soup.find_all("div", class_="elementor-widget-wrap elementor-element-populated")
    for c in containers:
        try:
            name_title_sub_e = c.find_all("h3", class_="elementor-heading-title elementor-size-default")
            name, title, sub = [extract_text(x) for x in name_title_sub_e]
            print(name, title, sub)

            url_e = c.find("a", href=True)
            url = url_e["href"]
            if "hukum.ub" in url:
                url = url

            img_url_e = c.find("img", src=True, title=True, alt=True)
            img_url = img_url_e["src"]

            p = c.find("p")
            nip, email = [x.strip() for x in str(p).strip("<p>").strip("</p>").strip("NIP. ").replace("<br/>", " ").split(" ")]
            
            try:
                html = s.get(url, timeout=TIMEOUT, headers=HEADERS).content
                soup = bs(html, 'html.parser')
            except:
                print('Failed to fetch individual professor page.')

            res_pendidikan = extract_info(soup.find("div", id="pendidikan"))
            res_penelitian = extract_info(soup.find("div", id="penelitian"))

            res_publikasi = ""
            publikasi_c = soup.find("div", id="publikasi")
            for p in publikasi_c.find_all("a", class_="gsc_oci_title_link", href=True):
                res_publikasi += f"{p.text.strip()} {p['href']}\n"

            res_books = ""
            for p in publikasi_c.find_all("p")[1:]:
                res_books += f"{p.text.strip()}\n"

            row = [name, title, sub, url, img_url, nip, email, res_pendidikan, res_penelitian, res_publikasi, res_books]
            if row:
                writer.writerow(row)
                f.flush()
        except Exception as e:
            print(f'Error: {str(e)}')
            pass

print("Scraping completed and data saved to 'data_dosen_fh_unibraw.csv'.")
