# Cricket_Score_Alert
# Live Cricket Score Alerts 🏏


## 📖 Project Overview

The **Live Cricket Score Alerts** project is a Python-based application that displays real-time cricket match information directly on your desktop. By fetching live data from the network, this application provides users with instant updates including:
* Team Names
* Live Scores
* Match Location
* Match Start Time
* Match Summary & Description

## 🛠️ Prerequisites & Tech Stack

To run this project, you need **Python 3.x** installed along with the following libraries:

* **Tkinter:** For the Graphical User Interface (UI).
* **Requests:** To send HTTP requests to the cricket website.
* **BeautifulSoup (bs4):** To parse HTML data and extract match details.
* **Pillow (PIL):** To handle image processing (background images).

## ⚙️ Installation

1.  **Clone the repository** (or download the project files).
2.  **Install the required dependencies** using pip:

    ```bash
    pip install requests beautifulsoup4 pillow
    ```
    *(Note: Tkinter usually comes pre-installed with Python. If you are on Linux, you might need `sudo apt-get install python3-tk`)*.

3.  **Assets:** Ensure you have an image file named `background_image.jpg` in the same directory as your script to serve as the GUI background.

## 🚀 How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the main script:

    ```bash
    python main.py
    ```

## 📂 Project Structure & Logic

The project is structured around the `CricketScore` class. Here is a breakdown of the key functions used:

### GUI Components
* **`__init__`**: Initializes the main window, sets geometry (800x500), loads the background, and creates the "Check Score" button.
* **`select()`**: Retrieves the user's choice from the Combobox (dropdown).
* **`show_match_details()`**: Creates a new frame to display the specific details of the selected match.

### Backend/Scraping Logic
* **`scrap()`**: Connects to `https://www.espncricinfo.com/scores/` and fetches the raw HTML data.
* **`match_details()`**: Cleans the raw data and organizes it into a dictionary where the Key is the Match Name and the Value is the match details.
* **`teams_name()`, `match_summary()`, `match_time()`**: Helper functions that parse specific HTML tags (divs and spans) to extract granular data points.

## 📷 Output

The application launches a GUI window titled "LIVE CRICKET SCORE".
1.  **Select Match:** Choose a live match from the dropdown list.
2.  **View Results:** Click "Check Score" to see the summary, score, and location.

---
