 **Supplier Management Portal**  - README

The **Supplier Management Portal** centralizes supplier information, performance metrics, and compliance tracking. Initially developed with a stack of Python Flask, React.js, Apache Supersets,Airflow, Jupyter, and MariaDB, it has since been updated to use **Python Flask, React.js, Tableau, and in-memory data storage** to enhance security and maintain organizational privacy. The use of in-memory data ensures no organisation data is being divulged.

 Features

 1. **Supplier Viewing Interface**
   - Created an interface to view supplier details, offering easy navigation and access to both a supplier list and individual profiles.
   - Integrated filtering and search functionalities for a user-friendly experience.

 2. **Data Management Using RAM Memory**
   - Replaced the main database link with in-memory storage, ensuring sensitive data is secure and does not persist after sessions.
   - Dummy data sources allow safe interaction with all portal features, maintaining full functionality for demonstrations.

 3. **Supplier Profile Management**
   - Implemented features allowing suppliers to update contact information, certifications, and service details, with real-time validation checks.
   - Designed a user-friendly profile interface for efficient data updates.

 4. **Supplier Metrics Dashboard**
   - Developed a dashboard showcasing key metrics such as completed work orders, ratings, and performance indicators.
   - Metrics update dynamically for real-time performance visibility.

 5. **Compliance Tracking**
   - Built tools to track and display compliance statuses, with live indicators for licenses that are active, expired, or due soon.
   - Added search and filter options for easy access to compliance records based on type, status, and renewal dates.
