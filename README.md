# Employee Performance Analysis System

##  Project Overview
This project implements an **automated employee performance analysis system** that integrates data from a MySQL database and provides performance insights through a **Tkinter GUI application**. The system evaluates employee productivity, attendance, and deadline adherence, then computes an overall **performance rating (out of 10)**. 

The tool is designed to improve decision-making, reduce manual effort, and streamline performance evaluation in organizations.

 

##  Project Structure
- `FinalPythonDatabase1.py` → Main Python script (database creation, Tkinter GUI, rating logic).
- `phython projrct ppt (2).pptx` → Project presentation summarizing system design and implementation.
- `project results final py.png` → Screenshot of the GUI application displaying results.
- `README.md` → Documentation file.

 

## Installation & Setup

### Requirements
- Python 3.8+
- MySQL server installed and running
- Required Python libraries:
  ```bash
  pip install mysql-connector-python
  ```

### Database Setup
The script automatically creates a database and table if not already present:
- **Database:** `employee_data`
- **Table:** `employee_performance`
- Example employee records are inserted (John, Alice, Bob) with their scheduled hours, attended hours, tasks completed, and tasks completed on time.

 

##  Running the Project
1. Ensure MySQL is running locally with username/password configured in the script.
2. Run the Python script:
   ```bash
   python FinalPythonDatabase1.py
   ```
3. The Tkinter GUI will open.
4. Enter an employee’s name (e.g., `John`) and click **Display Performance**.
5. The system will fetch data from MySQL, calculate KPIs, and display:
   - Scheduled Hours  
   - Attended Hours  
   - Tasks Completed  
   - Tasks Completed on Time  
   - Final Rating (0–10 scale)

 

##  Rating Calculation
The employee rating is calculated based on:
- **Completion Rate** = Tasks Completed / Scheduled Hours  
- **Deadline Adherence** = Tasks Completed on Time / Tasks Completed  
- **Attendance Rate** = Attended Hours / Scheduled Hours  

Final Rating = Average of the above three × 10 (capped at 10).

 

##  Features
- Automated **database creation and data insertion**.
- **Tkinter GUI** for user-friendly interaction.
- Performance rating capped at 10 for consistency.
- Supports **multiple employees** with different performance records.
- Provides clear performance breakdown.

 

##  Future Enhancements
- Add support for updating employee records dynamically.
- Export reports in CSV or PDF format.
- Extend GUI with graphs for better visualization.
- Integration with HR systems for real-time tracking.

 

##  Author
- **Karunakar Uppalapati** (M70733630)

