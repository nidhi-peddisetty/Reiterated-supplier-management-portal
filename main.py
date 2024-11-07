import os
import pandas as pd
import re
from flask import Flask, render_template, send_from_directory, jsonify, request
from datetime import datetime, timedelta

CSV_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'suppliers_data.csv')  
LICENSE_CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'induce.csv')  


# Class for supplier data
class SupplierData:
    def __init__(self):
        self.data = []

    def load_data(self):
        if os.path.exists(CSV_FILE_PATH):
            try:
                df = pd.read_csv(CSV_FILE_PATH)
                if df.empty:
                    print("No data found in the supplier CSV file.")
                    return

                for _, row in df.iterrows():
                    if not self.is_valid_email(row['EMAIL']):
                        print(f"Invalid email format: {row['EMAIL']}")
                        continue

                    business_data = {
                        'business_name': row['BUSINESSNAME'],
                        'email': row['EMAIL'],
                        'first_name': row['FIRSTNAME'],
                        'last_name': row['LASTNAME'],
                        'phone': row['PHONE'],
                        'external_ref': row['EXTERNALREF'],
                        'administrator': row['ADMINISTRATOR'],
                        'finance_admin': row['FINANCEADMIN'],
                        'login': row['LOGIN'],
                        'ops_center_access': row['OPSCENTERACCESS'],
                        'calendar': row['CALENDAR'],
                        'skills': row['SKILLS'],
                        'regions': row['REGIONS'],
                        'segments': row['SEGMENTS'],
                        'integration_reference': row['INTEGRATIONREFERENCE'],
                        'primary_contact': row['PRIMARYCONTACT']
                    }
                    self.data.append(business_data)

                print(f"Supplier data loaded into memory: {len(self.data)} records.")
            except Exception as e:
                print(f"Error reading supplier CSV: {str(e)}")
        else:
            print(f"File {CSV_FILE_PATH} not found.")

    @staticmethod
    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None


# Class for license data
class LicenseData:
    def __init__(self):
        self.data = []

    def load_data(self):
        if os.path.exists(LICENSE_CSV_PATH):
            try:
                df = pd.read_csv(LICENSE_CSV_PATH)
                if df.empty:
                    print("No data found in the license CSV file.")
                    return

                for _, row in df.iterrows():
                    license_data = {
                        'business_name': row['BusinessName'],
                        'license_type': row['LicenseType'],
                        'expiry_date': row['ExpiryDate']
                    }
                    self.data.append(license_data)

                print(f"License data loaded into memory: {len(self.data)} records.")
            except Exception as e:
                print(f"Error reading license CSV: {str(e)}")
        else:
            print(f"File {LICENSE_CSV_PATH} not found.")


# Class to merge supplier and license data and  also to calculate status
class DataMerger:
    def __init__(self, suppliers, licenses):
        self.suppliers = suppliers
        self.licenses = licenses
        self.merged_data = []

    def calculate_license_status(self, expiry_date_str):
        try:
            try:
                expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
            except ValueError:
                expiry_date = datetime.strptime(expiry_date_str, "%d/%m/%Y")
            today = datetime.today()

            if expiry_date < today:
                return "Inactive"
            elif expiry_date <= today + timedelta(days=30):
                return "Due Soon"
            else:
                return "Active"
        except ValueError as e:
            print(f"Invalid Date: {expiry_date_str} - Error: {str(e)}")
            return "Invalid Date"

    def merge_data(self):
        for business in self.suppliers:
            matching_licenses = [license for license in self.licenses if license['business_name'] == business['business_name']]
            for license in matching_licenses:
                merged_data = business.copy()
                merged_data.update(license)
                merged_data['status'] = self.calculate_license_status(license['expiry_date'])
                self.merged_data.append(merged_data)
        print(f"Merged data contains {len(self.merged_data)} records.")


# Main flask application class
class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.supplier_data = SupplierData()
        self.license_data = LicenseData()
        self.data_merger = None
        self.load_data()
        self.setup_routes()

    def load_data(self):
        self.supplier_data.load_data()
        self.license_data.load_data()
        self.data_merger = DataMerger(self.supplier_data.data, self.license_data.data)
        self.data_merger.merge_data()

    def setup_routes(self):
        @self.app.route('/', methods=['GET', 'POST'])
        def index():
            if request.method == 'POST':
                query = request.form.get('query')
                results = [data for data in self.data_merger.merged_data if query.lower() in data['business_name'].lower()]
                return render_template('index.html', results=results)
            else:
                return render_template('index.html', results=None)

        @self.app.route('/js/<filename>')
        def serve_js(filename):
            return send_from_directory('static/js', filename)

        @self.app.route('/view_data')
        def view_data():
            return jsonify({
                "suppliers": self.supplier_data.data[:5],
                "licenses": self.license_data.data[:5],
                "merged": self.data_merger.merged_data[:5]
            }), 200

        @self.app.route('/sup_search', methods=['GET', 'POST'])
        def sup_search():
            if request.method == 'POST':
                query = request.form.get('query')
                results = [data for data in self.supplier_data.data if query.lower() in data['business_name'].lower()]
                return render_template('sup_search.html', results=results)
            else:
                return render_template('sup_search.html', results=None)

        @self.app.route('/sup_induction')
        def sup_induction():
            return render_template('sup_induction.html', suppliers=self.data_merger.merged_data)

        @self.app.route('/metrics')
        def metrics():
            return render_template('metrics.html')

        @self.app.route('/check_data')
        def check_data():
            if not self.supplier_data.data and not self.license_data.data and not self.data_merger.merged_data:
                return jsonify({"message": "No data in business_data_list, license_data_list, and merged_data_list."}), 400
            else:
                return jsonify({
                    "message": "Data loaded successfully.",
                    "suppliers": self.supplier_data.data[:5],
                    "licenses": self.license_data.data[:5],
                    "merged": self.data_merger.merged_data[:5]
                }), 200

    def run(self):
        self.app.run(debug=True)



if __name__ == '__main__':
    app_instance = App()
    app_instance.run()
