# Web Scraping for Faculty of Law Professors' Information

This Python script is designed for web scraping the profile information of professors from the Faculty of Law at the University of Brawijaya. It collects data such as names, titles, sub-titles, profile URLs, image URLs, NIP (Nomor Induk Pegawai) numbers, email addresses, education details, research information, publications, and books authored. The scraped data is saved in a CSV file for further analysis.

## Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- `requests`: Used for making HTTP requests to web pages.
- `BeautifulSoup` (imported as `bs`): A library for parsing HTML content.
- `csv`: Used for writing data to a CSV file.

You can install these libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone this repository or download the Python script to your local machine.

2. Open the script in your favorite text editor or integrated development environment (IDE).

3. Customize the script if needed:

   - `BASE_URL`: The URL of the Faculty of Law professors' profiles page you want to scrape.
   - `TIMEOUT`: The timeout for HTTP requests (in seconds).
   - `HEADERS`: HTTP headers for requests.

4. Run the script:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the actual name of the script.

5. The script will start scraping professor information and print the names, titles, and sub-titles of each professor as it progresses. Once completed, the data will be saved to a CSV file named `data_dosen_fh_unibraw.csv` in the same directory as the script.

## Output

The CSV file `data_dosen_fh_unibraw.csv` will contain the following columns:

- `Name`: Professor's name.
- `Title`: Professor's title.
- `Sub`: Sub-title (if available).
- `Profile URL`: URL to the professor's profile.
- `Img URL`: URL to the professor's profile image.
- `NIP`: Nomor Induk Pegawai (Employee Identification Number).
- `Email`: Professor's email address.
- `Education`: Education background.
- `Research`: Research information.
- `Publication`: Publication details with links (if available).
- `Books`: Books authored by the professor.

## Note

- Make sure to respect the website's terms of use and scraping policies.
- This script is provided as-is and may require adjustments to work with different websites or changes to the target website's structure.
- Be aware of ethical and legal considerations when scraping websites for data. Always ensure that you have the necessary permissions and comply with applicable laws and terms of service.
