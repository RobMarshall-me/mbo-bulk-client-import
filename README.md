# Bulk Client Import for MindBodyOnline

This Python script automates the process of importing client data into MindBodyOnline using Selenium WebDriver. It reads client information from a CSV file and fills out the required fields in the MindBodyOnline client portal.

## Prerequisites

Before running the script, you will need to have the following installed:

- Python 3.8+ (or a version supported by Poetry)
- ChromeDriver (make sure it matches your version of Chrome)
- Poetry (for managing the virtual environment)

### Required Python Libraries:
- Selenium
- pandas
- python-dotenv

## Installation

1. **Clone the Repository or Create a New Project Directory**

   Clone the repository or set up a new project directory:

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install Poetry**

   If you don't have Poetry installed, you can install it following the official guide: https://python-poetry.org/docs/#installation.

3. **Install Dependencies Using Poetry**

   Install the dependencies specified in the `pyproject.toml` file:

   ```bash
   poetry install
   ```

   This will create a virtual environment and install all the required dependencies.

4. **Set Up Environment Variables**

   Create a `.env` file in the project directory to store your sensitive information, such as login credentials and paths. Example `.env`:

   ```env
   login_url="https://clients.mindbodyonline.com"
   business="YourBusinessName"
   username="your_username"
   password="your_password"
   chromedriver_path="path_to_chromedriver"
   ```

## Usage

1. **Prepare the CSV File**

   Ensure that the `contacts.csv` file is in the same directory as the script. The CSV should include the following columns:

   - `First Name`
   - `Last Name`
   - `E-mail`
   - `Phone`

2. **Run the Script**

   You can run the script with Poetry:

   ```bash
   poetry run python <your_script_name>.py
   ```

   The script will:
   - Open the MindBodyOnline login page and log in using the credentials from the `.env` file.
   - Iterate over the rows of `contacts.csv` and add each client to the MindBodyOnline portal.
   - Switch to the appropriate iframe to interact with the form, fill out the client details, and submit the form.

## Script Breakdown

- **Selenium WebDriver**: The script uses Selenium to automate the Chrome browser to interact with the MindBodyOnline client portal.
- **Environment Variables**: Sensitive data like login credentials and the ChromeDriver path are securely stored in a `.env` file, which is loaded using the `python-dotenv` package.
- **CSV Processing**: The `pandas` library is used to read client data from the CSV file and loop through each row.
- **Iframe Handling**: The script switches to the iframe (`<iframe id="portal">`) within the MindBodyOnline portal to add client data.
- **Error Handling**: If any error occurs while adding a client, the script logs the error and continues with the next client.

## Notes

- Make sure the path to `chromedriver.exe` is correct in the `.env` file (`chromedriver_path="path_to_chromedriver"`).
- Ensure the client form fields (e.g., `First Name`, `Last Name`, `Email`, `Phone`) in the MindBodyOnline portal match the IDs used in the script. If these change, you may need to update the script.
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.