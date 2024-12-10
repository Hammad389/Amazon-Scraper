# Amazon Scraper  

A Python-based tool to scrape product data from Amazon for specified search queries. It extracts product titles, prices, reviews, and image links, saving results in JSON files. The script is designed for simplicity, scalability, and evasion of detection.

---

## Features  

- **Anti-Detection Measures**:  
  - Utilizes `undetected-chromedriver` to bypass Amazon's anti-bot mechanisms.  
  - Avoids using Amazon's homepage to prevent CAPTCHA triggers.  
  - Mimics human-like behavior with randomized typing and action delays.  

- **Scalability**:  
  - Supports multiple search queries from a JSON file.  
  - Handles pagination for scraping multiple result pages per query.  

- **Data Organization**:  
  - Saves scraped data for each query in separate JSON files in the `scraped_data` folder.  

---

## Installation  

### Prerequisites  
- Python 3.8 or later  
- Google Chrome  
- ChromeDriver matching your Chrome version  

### Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Add search queries:  
   - Create a `user_queries.json` file in the root directory with search terms:  
     ```json
     ["laptops", "wireless headphones", "gaming chairs"]
     ```  

---

## Usage  

Run the script with:  
```bash
python amazon_scraper.py
```  

The scraped data will be saved as JSON files in the `scraped_data/` directory.  

---

## File Structure  

```
project-folder/
├── amazon_scraper.py       # Main script containing all functionality
├── user_queries.json       # Input file with search terms
├── scraped_data/           # Directory to save scraped data
├── requirements.txt        # List of dependencies
```

---

## Notes  

- The scraper runs in `--headless` mode for efficiency.  
- Ensure ChromeDriver matches your Chrome browser version.  
- Debugging messages are logged to the console for troubleshooting.  

---

## Dependencies  

The script uses the following libraries:  
- `undetected-chromedriver`  
- `selenium`  
- `os` and `json` for file operations  
- `time` and `random` for human-like delays  

Install all dependencies with:  
```bash
pip install -r requirements.txt
```  

---

## License  

This project is licensed under the MIT License.  

---

## Contributing  

Contributions are welcome! Feel free to open issues or submit pull requests.
