
# Hottest skills in data science industry (2020)

This project involves a survey conducted on the hottest skills in the data science industry based on a dataset scraped from indeed.com. The survey analyzes job postings and resumes to identify the most in-demand skills for data science roles. The project includes data collection, analysis, visualization, and reporting.

---

## Features

### 1. Data Collection
   - **Scraping Job Postings**: Scrapes job postings from indeed.com and stores the data in JSON files.
     - Example files: `jobs/jobs_1.json`, `jobs/jobs_2.json`, ..., `jobs/jobs_20.json`
   - **Scraping Resumes**: Scrapes resumes from indeed.com and stores the data in JSON files.
     - Example files: `resumes/resumes_1.json`, `resumes/resumes_2.json`, ..., `resumes/resumes_20.json`
   - **CSV Datasets**: Contains CSV files with skill data extracted from job postings and resumes.
     - `available_skills.csv`
     - `final_skills.csv`
     - `skills_available.csv`
     - `skills_data.csv`

### 2. Data Analysis
   - **Skill Analysis**: Analyzes the data to identify the most available and most sought-after skills in the data science industry.
   - **Skill Ranking**: Ranks the top 20 hottest skills based on their occurrence in job postings and resumes.

### 3. Visualization
   - **Data Visualizations**: Creates visual representations of the data to highlight key findings.
     - `Hot_skills_in_data_science.png`
     - `hottest_20_skills.png`
     - `most_available_skills.png`
     - `most_sought_out_skills.png`
     - `report_1.png`
     - `report_2.png`

### 4. Reporting
   - **Reports**: Provides detailed reports summarizing the analysis and findings.
     - `report.docx`
     - `report.pdf`

### 5. Documentation and Scripts
   - **Python Scripts**: Includes scripts for scraping data, analyzing skills, and generating visualizations.
     - `script.py`
   - **Jupyter Notebooks**: Contains Jupyter Notebooks for interactive data analysis and visualization.
     - `Untitled.ipynb`

---

## Detailed Explanation

### **Data Collection**

- **Job Postings**: Scraped job postings are stored in JSON format within the `jobs` directory. Each file contains a batch of job postings, capturing details such as job title, company, location, and required skills.
- **Resumes**: Scraped resumes are stored in JSON format within the `resumes` directory. Each file contains a batch of resumes, capturing details such as the applicant's skills, experience, and education.

### **Data Analysis**

- **Skill Extraction**: Skills are extracted from job postings and resumes, and stored in CSV files.
- **Skill Analysis**: The data is analyzed to determine the frequency and distribution of skills. Skills are ranked based on their frequency in job postings and resumes.

### **Visualization**

- **Charts and Graphs**: Visualizations are created to highlight the most in-demand skills. These include bar charts, pie charts, and other graphical representations.

### **Reporting**

- **Report Generation**: Detailed reports are generated, summarizing the findings of the survey. The reports provide insights into the hottest skills in the data science industry and trends over time.

### **Documentation and Scripts**

- **Python Scripts**: `script.py` includes functions for scraping data, processing it, and generating visualizations.
- **Jupyter Notebooks**: `Untitled.ipynb` provides an interactive environment for data analysis and visualization.

---

## Usage Instructions

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies**: 
   - Ensure you have Python and required libraries installed. You can install the necessary libraries using:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Data Collection Script**:
   ```bash
   python script.py
   ```

4. **Analyze Data and Generate Visualizations**:
   - Use the Jupyter Notebook `Untitled.ipynb` for interactive analysis and visualization.
   - The results of the analysis and visualizations will be generated and saved in the appropriate directories.

5. **Review Reports**:
   - The reports summarizing the findings are available in `report.docx` and `report.pdf`.

---

## Conclusion

This project provides a comprehensive analysis of the hottest skills in the data science industry, leveraging data scraped from indeed.com. By analyzing job postings and resumes, it identifies the most in-demand skills and provides valuable insights for professionals and employers in the data science field.

Report : https://github.com/ammarisme/survey-on-data-science-skills/blob/master/report.pdf
