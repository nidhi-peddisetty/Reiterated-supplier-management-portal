Here’s the content for your **README.md** file with setup instructions and the relevant details about the **Supplier Management Portal** project:

---

 Supplier Management Portal

The **Supplier Management Portal** centralizes supplier information, performance metrics, and compliance tracking. Initially developed using a stack of Python Flask, React.js, Apache Superset, Airflow, Jupyter, and MariaDB, the system has since been updated to use Python Flask, React.js, Tableau, and in-memory data storage. This change enhances security by ensuring that no organizational data is stored permanently, thus maintaining privacy.

 Features

 1. Supplier Viewing Interface
- A user-friendly interface that allows easy access to supplier details.
- Features include a supplier list and individual supplier profiles.
- Integrated search and filter options for a smoother user experience.

 2. Data Management Using RAM Memory
- Replaced the main database with in-memory storage to ensure sensitive data remains secure and does not persist after the session ends.
- Dummy data sources are used for interaction, making it safe for demonstrations and testing.

 3. Supplier Profile Management
- Suppliers can update their contact information, certifications, and service details.
- Real-time validation checks ensure the data entered is accurate and up to date.
- User-friendly profile interface that simplifies data management.

 4. Supplier Metrics Dashboard
- A dynamic dashboard that displays key supplier metrics, including completed work orders, ratings, and performance indicators.
- Metrics update in real-time for up-to-date insights on supplier performance.

 5. Compliance Tracking
- Tools to track and display compliance statuses with live indicators for licenses that are active, expired, or due for renewal.
- Search and filter options to quickly find compliance records based on type, status, and renewal dates.

---

 Setup Instructions

 1. Install Python and pip

Make sure Python is installed on your system. If Python is not installed, download and install it from the [official website](https://www.python.org/downloads/).

You can verify your Python installation by running:
```bash
python --version
```

`pip`, the Python package manager, is included with Python by default. If needed, you can install or upgrade `pip` using:
```bash
python -m ensurepip --upgrade
```

 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment for your project to keep dependencies isolated.

- To create a virtual environment, run:
  ```bash
  python -m venv venv
  ```

- To activate the virtual environment:

  - **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

  - **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```

After activation, your terminal prompt should change, showing `(venv)` to indicate the virtual environment is active.

 3. Install Dependencies

With your virtual environment activated, install the required packages for the project. To install Flask and any other dependencies, run:
```bash
pip install Flask
```

If the project has a `requirements.txt` file, you can install all dependencies at once by running:
```bash
pip install -r requirements.txt
```

 4. Clone the Repository (if applicable)

If the project is hosted on a GitHub repository, you can clone it to your local machine by running:
```bash
git clone https://github.com/nidhi-peddisetty/Reiterated-supplier-management-portal.git
cd Reiterated-supplier-management-portal
```

 5. Run the Project

Once the dependencies are installed, you can run the project by executing the following command:
```bash
python main.py
```

This will start the Flask server, and you can access the portal in your web browser at:
```
http://127.0.0.1:5000/
```

 6. Deactivate the Virtual Environment

After you're done working, deactivate the virtual environment by running:
```bash
deactivate
```

---

 Contributing

If you’d like to contribute to the development of the **Supplier Management Portal**, feel free to fork this repository and submit pull requests with your improvements or bug fixes. Please make sure to follow the standard coding practices and include relevant tests when applicable.

---

 License

This project is open source and available under the [MIT License](LICENSE).

---

This README provides a complete guide to set up and run the **Supplier Management Portal** locally, as well as additional information about the project’s features and how to contribute.
