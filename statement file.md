**# Vehicle Rental System - Project Statement**

**## Project Overview**

A console-based vehicle rental management system that allows users to manage a fleet of vehicles for rental purposes. The system provides basic CRUD operations and rental management functionality through a simple text-based interface.

**## Core Functionality Requirements**

**### Data Management**

\- Persistent storage of vehicle data using JSON format

\- Automatic data file creation if not exists

\- Error handling for data corruption scenarios

**### Vehicle Operations**

1\. \*\*Add New Vehicle\*\*

`   `- Capture vehicle details: make, model, year, daily rental rate

`   `- Auto-generate unique vehicle identifiers

`   `- Validate numerical inputs (year, rental rate)

2\. \*\*Display Vehicle Inventory\*\*

`   `- List all vehicles with complete details

`   `- Show current rental status (Available/Rented)

`   `- Format output for readability

3\. \*\*Rental Processing\*\*

`   `- Rent available vehicles by ID

`   `- Calculate total cost based on rental duration

`   `- Prevent renting of already rented vehicles

`   `- Validate rental period (positive integers only)

4\. \*\*Return Processing\*\*

`   `- Return rented vehicles by ID

`   `- Update vehicle availability status

`   `- Prevent return of already available vehicles

**### User Interface**

\- Text-based menu system

\- Clear option
