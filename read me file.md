**Vehicle Rental System**

**1. Project Title**

**Vehicle Rental Management System**\
*A Comprehensive Console-Based Rental Solution*

**2. Overview**

The Vehicle Rental System is a robust console-based application designed to streamline and automate rental operations for vehicle rental businesses. This system eliminates manual record-keeping challenges by providing a digital platform to manage vehicle inventory, track rentals, process returns, and calculate costs efficiently.

The application serves as a foundational management tool for small to medium-sized rental companies, offering essential features without the complexity of enterprise-level software. With its intuitive text-based interface and persistent data storage, businesses can maintain accurate records and improve operational efficiency.

**3. Features**

**🚗 Core Functionalities**

**Vehicle Inventory Management**

- **Add New Vehicles**: Register vehicles with complete details including make, model, manufacturing year, and daily rental rate
- **Automatic ID Generation**: System automatically assigns unique identifiers to each vehicle
- **Comprehensive Listing**: View complete inventory with all vehicle specifications

**Rental Operations**

- **Smart Rental Processing**: Rent vehicles by ID with duration-based cost calculation
- **Availability Control**: Prevent double-booking through real-time status tracking
- **Flexible Duration**: Support for custom rental periods with automatic cost computation

**Return Management**

- **Streamlined Returns**: Simple return process with automatic status updates
- **Availability Restoration**: Immediate status change from "Rented" to "Available" upon return

**Data Management**

- **Persistent Storage**: All data automatically saved in JSON format
- **Data Integrity**: Automatic file creation and corruption handling
- **Session Persistence**: Data remains intact between application sessions

**User Experience**

- **Input Validation**: Comprehensive validation for all user inputs
- **Error Handling**: Clear error messages for invalid operations
- **User-Friendly Interface**: Simple menu-driven navigation

**4. Technologies/Tools Used**

**🛠 Technical Stack**

**Programming Language**

- **Python 3.x**: Core programming language chosen for its simplicity, readability, and extensive standard library

**Core Libraries & Modules**

- **json**: For data serialization and persistent storage in JSON format
- **os**: For file system operations and path management

**Data Storage**

- **JSON File Format**: Lightweight, human-readable data storage format
- **UTF-8 Encoding**: Comprehensive character support for international text

**Development & Platform**

- **Cross-Platform Compatibility**: Runs on Windows, macOS, and Linux systems
- **Standard Library Only**: No external dependencies required

**5. Steps to Install and Run the Project**

**📋 Prerequisites Verification**

**Check Python Installation**

\# Verify Python is installed

python --version

\# or

python3 –version

**Required Version**

- Python 3.6 or higher recommended
- No additional packages or libraries needed

**🔧 Installation Process**

**Step 1: Obtain Project Files**

- Download the project ZIP file and extract, OR
- Clone from repository if available

**Step 2: Navigate to Project Directory**

\# Change to project directory

cd vehicle-rental-system

**Step 3: Verify File Structure**\
Ensure the following files are present:

- vehicle\_rental\_system.py (main application file)
- vehicles.json (will be auto-created on first run)

**🚀 Running the Application**

**Initial Launch**

\# Run the application

python vehicle\_rental\_system.py

**Expected Behaviour**

- Application starts immediately
- Main menu displays with 5 options
- vehicles.json file created automatically in same directory

**Normal Operation**

\# Subsequent runs

python vehicle\_rental\_system.py

**6. Instructions for Testing**

**🧪 Comprehensive Test Plan**

**1. Initial Setup Testing**

- ✅ Run application for first time
- ✅ Verify vehicles.json file creation
- ✅ Confirm empty inventory message displays

**2. Vehicle Management Testing**

Test Case: Add Vehicle

\- Action: Select option 1, enter: Toyota, Corolla, 2022, 1500

\- Expected: "Vehicle with ID 1 added" confirmation

\- Verification: Use option 2 to confirm vehicle appears in list

Test Case: Add Multiple Vehicles

\- Action: Add 3 different vehicles

\- Expected: Sequential ID assignment (1, 2, 3)

\- Verification: All vehicles display with correct details

**3. Rental Operations Testing**

Test Case: Rent Available Vehicle

\- Action: Select option 3, enter ID 1, duration 5 days

\- Expected: Cost calculation (5 × 1500 = 7500), status change to "Rented"

\- Verification: Vehicle shows "Rented" status in list

Test Case: Rent Already Rented Vehicle

\- Action: Attempt to rent same vehicle again

\- Expected: "Vehicle is already rented" error message

\- Verification: Rental fails, status remains "Rented"

**4. Return Process Testing**

Test Case: Return Rented Vehicle

\- Action: Select option 4, enter rented vehicle ID

\- Expected: "Vehicle returned successfully" message

\- Verification: Status changes to "Available" in vehicle list

Test Case: Return Available Vehicle

\- Action: Attempt to return available vehicle

\- Expected: "Vehicle is already available" message

\- Verification: No status change occurs

**5. Data Persistence Testing**

Test Case: Application Restart

\- Actions: 

`  `1. Add vehicles and perform rentals

`  `2. Close application completely

`  `3. Restart application

\- Expected: All data preserved, statuses maintained

\- Verification: Vehicle list shows exact same state as before closure

**6. Error Handling Testing**

Test Case: Invalid Inputs

\- Actions: 

`  `- Enter non-numeric values for ID/year/rent/days

`  `- Use negative numbers for rental duration

`  `- Enter non-existent vehicle IDs

\- Expected: Appropriate error messages for each scenario

\- Verification: System doesn't crash, returns to menu

Test Case: Boundary Testing

\- Actions: 

`  `- Enter very large numbers

`  `- Test with zero/negative rental days

\- Expected: Proper validation and error messages

**7. File Corruption Testing**

Test Case: Corrupted Data File

\- Actions: 

`  `1. Manually corrupt vehicles.json file

`  `2. Restart application

\- Expected: System handles error gracefully, continues with empty inventory

\- Verification: Application doesn't crash, creates new data file if needed

**📝 Test Completion Criteria**

**Success Indicators**

- All menu options function correctly
- Data persists between sessions
- Error conditions handled gracefully
- No application crashes during normal operation
- All business logic works as specified

**Expected Output**

- Clear, user-friendly messages
- Accurate cost calculations
- Correct status updates
- Proper data preservation



**Screenshots**










