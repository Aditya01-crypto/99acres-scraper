# 🏠 99acres Real Estate Intelligence Tool

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Playwright](https://img.shields.io/badge/playwright-1.40+-green.svg)
![BeautifulSoup](https://img.shields.io/badge/beautifulsoup4-4.12+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

> **Professional-grade real estate data extraction system** with advanced anti-detection capabilities and ethical scraping practices.

A production-ready Python tool that automates property data collection from 99acres.com, featuring intelligent browser automation, human-like behavior simulation, and structured data export.

---

## 💡 Why This Tool?

Real estate data is fragmented across platforms, making property analysis time-consuming and inefficient. This tool solves that problem.

### Business Value

- ⏱️ **Save 10+ hours weekly** on manual data collection
- 📊 **Enable data-driven decisions** with structured property datasets
- 💰 **Identify market opportunities** through comprehensive analysis
- 🎯 **Competitive intelligence** for real estate professionals

### Real-World Applications

- **Property Investors**: Analyze market trends, identify undervalued properties
- **Real Estate Agencies**: Market research and competitive analysis
- **Data Analysts**: Study pricing patterns and location-based trends
- **Individual Buyers**: Compare properties efficiently across locations

---

## 🎯 Technical Highlights

### Advanced Anti-Detection System

- ✅ **Playwright Stealth Integration** - Bypasses basic bot detection
- ✅ **Human-like Mouse Movements** - Randomized cursor patterns
- ✅ **Intelligent Scrolling** - Variable speed with natural reading pauses
- ✅ **Geo-Spoofing** - Indian locale, timezone, and location simulation
- ✅ **User Agent Rotation** - Authentic browser fingerprints

### Production-Ready Architecture

- ⚡ **Async/Await Operations** - Efficient, non-blocking execution
- 📝 **Dual-Level Logging** - Console (INFO) + File (DEBUG) with timestamps
- 🛡️ **Comprehensive Error Handling** - Graceful failures with detailed logs
- 📊 **Smart Data Parsing** - Handles multiple card layouts automatically
- 💾 **Clean Excel Export** - Timestamped files with structured data

### Configurable & Flexible

- 🎛️ **Adjustable Scroll Depth** - Control data volume
- 👁️ **Headless/GUI Modes** - Debug visually or run in background
- 🌍 **Multi-Location Support** - Any Indian city
- 🔧 **Extensible Codebase** - Easy to modify and enhance

---

## 📋 Features

| Feature | Description |
|---------|-------------|
| **Smart Scraping** | Extracts property name, price, BHK, location, links, and descriptions |
| **Dual Card Support** | Handles both `tupleNew` and `PseudoTupleRevamp` card types |
| **Timestamped Output** | Auto-generates Excel files with `YYYYMMDD_HHMMSS_Location.xlsx` format |
| **Missing Data Handling** | Fills gaps with 'N/A' for incomplete listings |
| **Scroll-Based Pagination** | Configurable depth (5-100 scrolls) |
| **Debug Mode** | Watch the scraper work in real-time (GUI mode) |

---

## 🛠️ Installation

### Prerequisites

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **pip** package manager (included with Python)
- **Git** (optional, for cloning)

### Quick Setup (5 Minutes)

```bash
# 1. Clone the repository
git clone https://github.com/Aditya01-crypto/99acres-Real-Estate-Intelligence-Tool.git
cd 99acres-Real-Estate-Intelligence-Tool

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install additional parsers
pip install lxml

# 4. Install Playwright browsers (one-time setup)
playwright install
```

### Dependencies

```txt
playwright>=1.40.0
playwright-stealth>=1.0.6
beautifulsoup4>=4.12.0
lxml>=4.9.0
pandas>=2.0.0
openpyxl>=3.1.0
```

---

## 🚀 Usage

### Basic Usage

```python
import asyncio
from main import main

# Scrape properties in Pune
asyncio.run(main('Pune'))
```

### Advanced Configuration

```python
async def main(loc, scroll=20, no_gui=False):
    """
    Parameters:
    -----------
    loc : str
        Target city (e.g., 'Mumbai', 'Bangalore', 'Delhi')
    
    scroll : int, default=20
        Number of scroll iterations
        - More scrolls = more listings
        - Recommended: 10-30 for balance
        - Each scroll ≈ 10-15 listings
    
    no_gui : bool, default=False
        Browser visibility
        - False: Show browser (debugging)
        - True: Headless mode (production)
    """
```

### Example Scenarios

**🔍 Debugging Mode** (Watch it work):
```python
# Small dataset, visible browser
asyncio.run(main('Bangalore', scroll=10, no_gui=False))
```

**🚀 Production Mode** (Fast, background):
```python
# Larger dataset, headless
asyncio.run(main('Mumbai', scroll=30, no_gui=True))
```

**💼 Client Project** (Balanced):
```python
# Medium dataset, professional output
asyncio.run(main('Hyderabad', scroll=20, no_gui=True))
```

---

## 📊 Output Structure

### Excel File Format

Generated files: `YYYYMMDD_HHMMSS_Location_RealEstateData.xlsx`

**Example**: `20241201_143052_Pune_RealEstateData.xlsx`

### Data Columns

| Column | Description | Example |
|--------|-------------|---------|
| **Building Name** | Property/project name | "Godrej Emerald" |
| **Full Price** | Complete pricing info | "₹ 1.2 Cr - 1.8 Cr" |
| **Price per Sqft** | Rate per sq ft | "₹ 8,500/sqft" |
| **BHK** | Bedroom configuration | "2, 3 BHK Apartment" |
| **Location** | Detailed address | "Kharadi, Pune" |
| **Link** | Property URL | "https://..." |
| **Summary** | Brief description | "Ready to move luxury..." |

### Sample Output

```
Building Name    | Full Price       | BHK              | Location
-----------------|------------------|------------------|-------------
Godrej Emerald   | ₹ 1.2-1.8 Cr    | 2, 3 BHK         | Kharadi, Pune
Prestige Park    | ₹ 95 Lac-1.4 Cr | 2, 3 BHK         | Wakad, Pune
```

---

## 📁 Project Structure

```
99acres-Real-Estate-Intelligence-Tool/
│
├── main.py                          # Core scraper engine
├── RealEstateDataCleaner.py         # Data parser & Excel exporter
├── RealEstatelogger.py              # Logging configuration
├── requirements.txt                 # Python dependencies
├── README.md                        # Documentation (this file)
│
├── RealState.logs                   # Debug logs (auto-generated)
├── outputdata.txt                   # Raw HTML cache (auto-generated)
└── YYYYMMDD_HHMMSS_Location_RealEstateData.xlsx  # Output files
```

---

## 🏗️ Architecture Overview

### 1. **Logging System** (`RealEstatelogger.py`)

Dual-output logging for debugging and monitoring:

- **Console**: INFO level, simple format for real-time monitoring
- **File**: DEBUG level, detailed with timestamps and function names
- Log file: `RealState.logs`

```python
# Example log output
INFO - Starting scraper for location: Pune
DEBUG - Browser launched successfully
DEBUG - Navigation complete: https://99acres.com
INFO - Scroll 5/20 complete
```

### 2. **Scraper Engine** (`main.py`)

Three core functions power the anti-detection system:

#### `human_like_mouse_movement(page, duration)`
Simulates natural cursor behavior to avoid bot detection.

```python
# Moves mouse in small, random increments
# Duration: 1-3 seconds typically
# Pattern: Curved, human-like trajectories
```

#### `human_like_scroll(page, scroll_count)`
Intelligent scrolling with variable patterns:

```python
# Features:
# - Random scroll distances (300-700px)
# - Variable delays (0.3-2s between scrolls)
# - Occasional "reading pauses" (3-8s)
# - Mouse movement integration
```

#### `main(loc, scroll, no_gui)`
Orchestrates the entire scraping workflow:

1. Initialize Playwright with stealth plugins
2. Configure Indian geo-location and timezone
3. Navigate to 99acres.com
4. Perform location search
5. Execute human-like scrolling
6. Extract and save page HTML
7. Trigger data cleaning and export

### 3. **Data Processor** (`RealEstateDataCleaner.py`)

Parses HTML and generates structured Excel output:

- **Handles two card types**: 
  - `tupleNew__contentWrap` (individual listings)
  - `PseudoTupleRevamp__contentWrapAb` (project listings)
- **Graceful error handling**: Missing fields filled with 'N/A'
- **Clean export**: Pandas DataFrame → Excel with openpyxl

---

## ⚖️ Responsible Usage Guidelines

### Ethical Scraping Practices

This tool is designed with responsibility in mind:

- ✅ Human-like behavior reduces server load
- ✅ Configurable rate limiting
- ✅ Respects website performance
- ✅ Intended for legitimate data collection

### Recommended Scroll Limits

| Use Case | Scroll Count | Expected Listings | Notes |
|----------|--------------|-------------------|-------|
| **Testing** | 5-10 | ~50-100 | Quick verification |
| **Personal Research** | 10-20 | ~100-200 | Balanced approach |
| **Market Analysis** | 20-50 | ~200-500 | Use cautiously |
| **⚠️ Maximum** | 100 | ~1000 | Single session limit |

### Best Practices Checklist

- [ ] **Start small**: Test with 5 scrolls first
- [ ] **Add delays**: Wait 5-10 minutes between runs
- [ ] **Off-peak hours**: Run during low-traffic times
- [ ] **Monitor logs**: Check for errors in `RealState.logs`
- [ ] **Cache results**: Don't re-scrape unnecessarily
- [ ] **Respect ToS**: Review 99acres.com terms of service
- [ ] **Use ethically**: Personal research, not commercial resale

### Legal Compliance

**Users must:**
- Comply with target website's Terms of Service
- Use collected data for legitimate purposes only
- Implement appropriate rate limits
- Not use for unauthorized commercial redistribution
- Obtain necessary permissions for business use

**This tool is suitable for:**
- Personal property research
- Academic studies
- Market analysis (with proper authorization)
- Business intelligence (non-competitive use)

---

## 🐛 Troubleshooting

### Common Issues & Solutions

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| **"Search Bar not found"** | Website HTML changed | Update CSS selectors in `main.py` |
| **Timeout errors** | Slow network/page load | Increase `wait_for_load_state` timeout |
| **Empty Excel file** | No data collected | Check `outputdata.txt`; increase scroll count |
| **Browser crash** | Memory overload | Reduce scroll count; add more delays |
| **"Playwright not installed"** | Missing browsers | Run `playwright install` |
| **Import errors** | Missing dependencies | Run `pip install -r requirements.txt` |

### Debug Workflow

1. **Check logs first**:
   ```bash
   # Linux/Mac
   tail -50 RealState.logs
   
   # Windows
   Get-Content RealState.logs -Tail 50
   ```

2. **Run in GUI mode**:
   ```python
   asyncio.run(main('Pune', scroll=3, no_gui=False))
   ```
   Watch the browser to identify where it fails.

3. **Verify raw data**:
   Check if `outputdata.txt` contains HTML. If empty, scraping failed.

4. **Test with minimal settings**:
   ```python
   # Bare minimum test
   asyncio.run(main('Mumbai', scroll=1, no_gui=False))
   ```

### Getting Help

If issues persist:

1. 📋 Review `RealState.logs` for error details
2. 🔍 Check that all dependencies are installed: `pip list`
3. 🌐 Verify Playwright browsers: `playwright install`
4. 🔄 Update dependencies: `pip install -r requirements.txt --upgrade`
5. 💬 Open an issue on GitHub with logs and error messages

---

## 🔧 Customization

### Modify Browser Settings

Edit the Playwright context in `main()`:

```python
context = await browser.new_context(
    user_agent='Mozilla/5.0...',  # Custom user agent
    viewport={'width': 1920, 'height': 1080},
    locale='en-IN',
    timezone_id='Asia/Kolkata',
    geolocation={'latitude': 18.5204, 'longitude': 73.8567},  # Pune coords
    permissions=['geolocation']
)
```

### Adjust Scraping Timing

Modify delays in `human_like_scroll()`:

```python
# Make it slower (more cautious)
delay = random.uniform(1.0, 4.0)  # Longer delays between scrolls
read_time = random.uniform(5, 12)  # Longer reading pauses

# Make it faster (use carefully)
delay = random.uniform(0.2, 1.0)
read_time = random.uniform(2, 5)
```

### Add New Data Fields

Update `RealEstateDataCleaner.py` to extract additional data:

```python
# Example: Extract property age
property_age = card.find('span', class_='propertyAge').text.strip()
data.append({
    # ... existing fields ...
    'Property Age': property_age
})
```

### Support Multiple Cities

Batch processing example:

```python
import asyncio
from main import main

async def scrape_multiple_cities():
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Pune']
    
    for city in cities:
        print(f"Scraping {city}...")
        await main(city, scroll=20, no_gui=True)
        await asyncio.sleep(600)  # 10-minute delay between cities

asyncio.run(scrape_multiple_cities())
```

---

## 🧪 Testing

### Quick Test (2 Minutes)

```python
import asyncio
from main import main

# Minimal test
asyncio.run(main('Pune', scroll=3, no_gui=False))
```

**Expected output:**
- Browser opens and navigates to 99acres.com
- Search is performed
- Page scrolls 3 times
- Excel file generated with ~30-50 listings
- Logs show successful completion

### Verification Checklist

After running:

- [ ] Excel file created with timestamp in filename
- [ ] File contains data (not empty)
- [ ] All columns present (Building Name, Price, BHK, etc.)
- [ ] Links are valid 99acres.com URLs
- [ ] `RealState.logs` shows no critical errors
- [ ] `outputdata.txt` contains HTML content

---

## 📈 Performance Metrics

### Typical Execution Times

| Scroll Count | Time (GUI) | Time (Headless) | Listings |
|--------------|------------|-----------------|----------|
| 5 scrolls | ~2 minutes | ~1.5 minutes | ~50 |
| 10 scrolls | ~4 minutes | ~3 minutes | ~100 |
| 20 scrolls | ~8 minutes | ~6 minutes | ~200 |
| 50 scrolls | ~20 minutes | ~15 minutes | ~500 |

*Times vary based on network speed and website load*

### Resource Usage

- **Memory**: ~200-400 MB (Playwright browser)
- **CPU**: Low to moderate (async operations)
- **Disk**: Minimal (~5-10 MB per output file)
- **Network**: ~2-5 MB data transfer per run

---

## 🎓 Learning Resources

### Understanding the Code

**Key Concepts Demonstrated:**
- Async/await patterns in Python
- Playwright browser automation
- BeautifulSoup HTML parsing
- Anti-bot detection techniques
- Logging best practices
- Data processing with Pandas

### Further Reading

- [Playwright Documentation](https://playwright.dev/python/)
- [BeautifulSoup Guide](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Ethical Web Scraping](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01)
- [Python Async Programming](https://docs.python.org/3/library/asyncio.html)

---

## 🤝 Contributing

Contributions are welcome! Potential improvements:

### Feature Ideas

- [ ] Add property type filters (apartment, villa, plot)
- [ ] Implement price range filtering
- [ ] Add support for other real estate sites (MagicBricks, Housing.com)
- [ ] Create data visualization dashboard
- [ ] Add database storage option (SQLite/PostgreSQL)
- [ ] Implement data deduplication
- [ ] Add email notifications on completion
- [ ] Create command-line interface (CLI)

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ No warranty provided
- ⚠️ No liability accepted

---

## 🌟 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/99acres-Real-Estate-Intelligence-Tool?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/99acres-Real-Estate-Intelligence-Tool?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/99acres-Real-Estate-Intelligence-Tool)

---

## 👨‍💻 About the Developer

**Automation Specialist | Python Developer| Web Scraping Expert**

This project demonstrates expertise in:
- Advanced web scraping techniques
- Anti-detection and stealth automation
- Async Python programming
- Data extraction and processing
- Production-ready code architecture

### Tech Stack

**Languages**: Python 3.8+  
**Frameworks**: Playwright, BeautifulSoup4, Pandas  
**Specialization**: Web automation, data extraction, anti-bot systems

### Let's Connect

Need custom scraping solutions or automation workflows?

- 💼 **Portfolio**: [incoming]
- 📧 **Email**: [connectwithaditya04@gmail.com]
- 🐙 **GitHub**: [@Aditya01-crypto](https://github.com/@Aditya01-crypto)

---

## 💼 Professional Services

### Available for Freelance Projects

Specializing in:

- 🔍 **Web Scraping**: Complex sites, anti-bot systems, JavaScript rendering
- 🤖 **Automation**: Workflow automation, data processing, scheduled tasks
- 📊 **Data Extraction**: APIs, databases, Excel/CSV processing
- 🛠️ **Custom Tools**: Tailored solutions for your business needs

**Typical Project Scope:**
- Simple scraping: ₹10,000-25,000
- Complex anti-detection: ₹30,000-60,000
- Full automation systems: ₹50,000-1,50,000

---

## 📞 Support

**Have questions? Found a bug? Need help?**

- 🐛 [Report Issues](https://github.com/Aditya01-crypto/99acres-Real-Estate-Intelligence-Tool/issues)
- 💬 [Start a Discussion](https://github.com/Aditya01-crypto/99acres-Real-Estate-Intelligence-Toolr/discussions)


**Response time**: Usually within 24-48 hours

---

## ⭐ Show Your Support

If this project helped you, please consider:

- ⭐ **Star this repository** on GitHub
- 🍴 **Fork it** and build something cool
- 📢 **Share it** with others who might benefit
- 💬 **Provide feedback** to help improve it

---

## 🙏 Acknowledgments

- **Playwright Team** - Excellent browser automation framework
- **BeautifulSoup Community** - Powerful HTML parsing library
- **Python Community** - Amazing ecosystem and support

---

## 📝 Changelog

### Version 1.0.0 (Current)

**Features:**
- ✅ Initial release
- ✅ Dual card type support
- ✅ Human-like behavior simulation
- ✅ Excel export functionality
- ✅ Comprehensive logging
- ✅ Anti-detection capabilities

**Coming Soon:**
- 🔜 Multi-city batch processing
- 🔜 Advanced filtering options
- 🔜 Database integration
- 🔜 CLI interface

---

**Built with ❤️ for ethical data collection**

*Last updated: December 2024*
