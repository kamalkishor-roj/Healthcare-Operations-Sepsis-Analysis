# Healthcare-Operations-Sepsis-Analysis
End-to-End Healthcare Analytics Project. Engineered an XML-to-CSV pipeline in Python and used Advanced SQL to audit hospital performance, revealing a 35% compliance failure in critical sepsis care.

# 🏥 Healthcare Operations Analysis: Emergency Room Bottlenecks & Sepsis Care Compliance

## 📌 Executive Summary
In Emergency Medicine, Sepsis is a time-critical condition where the **"Golden Hour"** protocol dictates that antibiotics must be administered within 60 minutes of triage.

This project analyzes over **15,000 event logs** from a hospital operational database to identify process bottlenecks, measure compliance with the Golden Hour standard, and recommend staffing optimizations based on patient arrival patterns.

## 💼 The Business Problem
Hospital administrators identified variability in patient outcomes and suspected operational delays. The objective of this analysis was to answer three key questions:
1.  **Compliance:** What percentage of Sepsis patients are receiving antibiotics within the required 60 minutes?
2.  **Bottleneck Detection:** Is the delay occurring during **Registration (Admin)** or **Clinical Assessment (Medical)**?
3.  **Resource Planning:** When is the ER most overwhelmed, necessitating increased staffing?

## 📊 Data Source
* **Dataset:** Sepsis Cases - Event Log
* **Source:** 4TU.ResearchData (TU/e)
* **Description:** Real-life event logs tracking patient journeys from `ER Registration` $\to$ `ER Triage` $\to$ `IV Antibiotics` $\to$ `Discharge`.
* **Volume:** 1,050 Cases / 15,214 Events.
* **Citation:** *Mannhardt, F. (2016). Sepsis Cases - Event Log [Data set]. 4TU.ResearchData. https://doi.org/10.4121/uuid:915d2bfb-7e84-49ad-a286-dc35f063a460*

## 🛠️ Methodology & Tech Stack

### 1. Data Engineering (Python)
* **Challenge:** The raw data was in `.xes` (XML) format, a hierarchical structure used in Process Mining that is incompatible with standard SQL databases.
* **Solution:** Built a custom ETL parser using Python (`xml.etree` and `pandas`) to flatten the XML tree into a relational CSV format suitable for analysis.
* **Code:** `scripts/xml_to_csv_parser.py`

### 2. Analytical Logic (SQL - PostgreSQL)
* **Pivoting:** Used `CASE` statements and `GROUP BY` to transform row-based events into a column-based "Patient Journey" table.
* **KPI Calculation:** Engineered metrics for `Door-to-Triage` and `Triage-to-Antibiotic` time.
* **Data Cleaning:** Implemented logic to handle negative timestamps (data entry errors) and `NULL` values (patients who did not receive treatment).
* **Code:** `sql/sepsis_analytics.sql`

### 3. Visualization
* **Tools:** Python (Seaborn/Matplotlib) and Power BI.
* **Focus:** Distribution analysis (Histograms) and Temporal patterns (Heatmaps).

## 🔎 Key Insights & Visualizations

### 1. The "Golden Hour" Compliance Failure
* **Finding:** Analysis reveals that **~35% of patients** missed the 1-hour antibiotic target.
* **Metric:** The average wait time for antibiotics was significantly higher than the target, with a "Long Tail" of patients waiting 3+ hours.

<img width="1120" height="349" alt="Screenshot 2025-12-05 172307" src="https://github.com/user-attachments/assets/933eb07b-a643-40b7-b076-fef58b6e990e" />

*(Above: Histogram showing the distribution of wait times. Note the "U-Shape" indicating a split between patients treated instantly and those neglected for hours.)*

### 2. Operational Bottlenecks
* **Front Desk Efficiency:** Average `Door-to-Triage` time is **< 10 minutes**.
* **Clinical Inefficiency:** Average `Triage-to-Antibiotic` time often exceeds **60-80 minutes**.
* **Conclusion:** The bottleneck is **not** administrative; it is clinical (availability of doctors/nurses or bed space).

### 3. Crisis Hour Identification
* **Finding:** Patient volume is not evenly distributed. 
* **Peak Load:** The Heatmap identifies critical surges on **Mondays (9 AM - 11 AM)** and **Thursdays (1 PM)**.
* **Recommendation:** Reallocate nursing staff from low-volume slots (Late Nights/Fridays) to cover the Monday morning surge.

<img width="1219" height="617" alt="Screenshot 2025-12-05 171958" src="https://github.com/user-attachments/assets/81c4b698-176f-459e-bec2-1957a48c221f" />

*(Above: Heatmap of Patient Volume by Day & Hour)*

## 💻 How to Run This Project
1.  Clone the repository.
2.  **ETL:** Run the Python script to generate the CSV:
    ```bash
    python scripts/etl_script.py
    ```
3.  **Database:** Import `sepsis_cleaned.csv` into PostgreSQL.
4.  **Analysis:** Execute the SQL query in `sql/analysis.sql` to generate the final KPI table.

## 📈 Future Improvements
* Implement **Predictive Modeling** (Random Forest) to predict likelihood of Sepsis based on initial triage vitals.
* Connect the SQL database directly to **Tableau** for a live operational dashboard.

---
**Author:** kamalkishor roj  
**LinkedIn:** [[Link to your LinkedIn Profile]](https://www.linkedin.com/in/kamalkishor-roj/)
