import requests
from bs4 import BeautifulSoup as bs
import csv, time

BASE_URL = "https://hukum.ub.ac.id/profil-dosen-2/"
TIMEOUT = 30 
HEADERS = {
    'authority': 'www.dickssportinggoods.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
}


s = requests.Session()
html = s.get(BASE_URL, timeout=TIMEOUT, headers=HEADERS).content
soup = bs(html, 'html.parser')

with open('data_dosen_fh_unibraw.csv','w',newline='') as f:
    writer = csv.writer(f)
    header = 'Name', 'Title', 'Sub', 'Profile URL','Img URL', 'NIP', 'Email','Education', 'Research', 'Publication', 'Books'
    writer.writerow(header)

    containers = soup.find_all("div", class_="elementor-widget-wrap elementor-element-populated")
    for c in containers:
        try:
            name_title_sub_e = c.find_all("h3", class_="elementor-heading-title elementor-size-default")
            name, title, sub = [x.text.strip() for x in name_title_sub_e]
            print(name, title, sub)

            url_e = c.find("a", href=True)
            url = url_e["href"]
            if "hukum.ub" in url:
                url = url

            img_url_e = c.find("img", src=True, title=True, alt=True)
            img_url = img_url_e["src"]
            #print(img_url)

            p = c.find("p")
            nip, email = str(p).strip("<p>").strip("</p>").strip("NIP. ").replace("<br/>"," ").split(" ")
            #print(nip,email)

            #print()
            try:   
                html = s.get(url, timeout=TIMEOUT, headers=HEADERS).content
                soup = bs(html, 'html.parser')
            except:
                print('failed')

            res_pendidikan = ""
            pendidikan_c = soup.find("div", id="pendidikan")
            for sc in pendidikan_c.find_all("div", class_="sectionContent")[3:]:
                university = sc.find("div", class_="contentDetails").find("strong").text.strip()
                details = sc.find("p", class_="subDetails").text.strip()
                res_pendidikan += f"""{university}
{details}"""
            #print(res_pendidikan)
            #print()

            res_penelitian =""
            penelitian_c = soup.find("div", id="penelitian")
            for p in penelitian_c.find_all("div", class_="contentDet"):
                res_penelitian += f"""{p.text.strip()}
"""
            #print(res_penelitian)

            res_publikasi = ""
            publikasi_c = soup.find("div", id="publikasi")
            for p in publikasi_c.find_all("a", class_="gsc_oci_title_link", href=True):
                res_publikasi += f"""{p.text.strip()} {p['href']}
"""
            #print(res_publikasi)
            #print()

            res_books = ""
            for p in publikasi_c.find_all("p")[1:]:
                res_books += f"""{p.text.strip()}
"""
            #print(res_books)
            #print()

            row = name, title, sub, url, img_url, nip, email, res_pendidikan,res_penelitian, res_publikasi, res_books
            if row:
                writer.writerow(row)
                #print(row)
            f.flush()
        except:
            pass
        #name = c.find("div", )