# MathonGO Student Performance Report System

## Project Overview
This project provides a comprehensive student performance report system for MathonGO, designed to analyze student test data, generate personalized motivational feedback using AI, and produce detailed PDF reports. It consists of two main components:
- A Jupyter Notebook (`task.ipynb`) for data analysis, prompt engineering experimentation, and PDF generation testing.
- A Streamlit web app (`app.py`) that allows users to upload student JSON files and interactively generate and download performance reports.

## Technologies Used
- Python 3.12+
- [Streamlit](https://streamlit.io/) for the interactive web app
- [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) for data processing
- [Google Generative AI (Gemini)](https://developers.generativeai.google/) for AI-powered feedback generation
- [Langchain](https://python.langchain.com/) for AI integration
- [FPDF2](https://pyfpdf.github.io/fpdf2/) for PDF report creation
- [python-dotenv](https://github.com/theskumar/python-dotenv) for environment variable management
- [tqdm](https://tqdm.github.io/) for progress bars in notebook

## Prompt Engineering
The system leverages prompt engineering to generate personalized, motivational feedback for students preparing for Indian engineering entrance exams. Using Google Gemini's generative model, a carefully crafted prompt includes detailed chapter-wise, concept-wise, and time-vs-accuracy statistics. The prompt instructs the AI to produce a structured feedback report with:
- A personalized motivational introduction
- Performance highlights
- Time vs accuracy analysis
- Strengths and weaknesses
- Areas to improve
- Actionable suggestions relevant to the exam context
- An encouraging closing message

This approach ensures feedback is tailored, insightful, and student-focused.

## PDF Report Structure and Content
The generated PDF reports feature:
- A header with the title "MathonGO Performance Report"
- A footer with the generation date and MathonGO branding
- Student ID prominently displayed
- Well-formatted sections corresponding to the AI-generated feedback structure:
  - Motivational introduction
  - Performance highlights
  - Time vs accuracy analysis
  - Strengths and weaknesses
  - Areas to improve
  - Actionable suggestions
  - Encouraging closing remarks

The report uses clear typography and color accents for headers to enhance readability.

## Usage Instructions

### Jupyter Notebook (`task.ipynb`)
1. Ensure your environment variables are set, including `GOOGLE_API_KEY` for the Google Generative AI.
2. Place student JSON files in the `./data` folder.
3. Run the notebook cells to:
   - Load and analyze student data
   - Generate AI feedback using prompt engineering
   - Create styled PDF reports saved in the `./reports` folder
4. Review outputs and experiment with prompt modifications as needed.

### Streamlit App (`app.py`)
1. Activate your Python environment and install dependencies (see Requirements below).
2. Run the app with:
   ```
   streamlit run app.py
   ```
3. Use the web interface to upload a student `.json` file.
4. View the performance summary and AI-generated feedback.
5. Click "Generate PDF" to create and download the detailed report.

## Folder Structure
```
.
├── app.py                  # Streamlit app for interactive report generation
├── notebook_api.py         # Core analysis, feedback, and PDF generation functions
├── task.ipynb              # Jupyter Notebook for data analysis and testing
├── requirement.txt         # Project dependencies
├── data/                   # Sample student JSON files for analysis
├── fonts/                  # Fonts used for PDF report generation
├── reports/                # Generated PDF reports output folder
└── README.md               # This documentation file
```

## Requirements and Installation
Install the required Python packages using:
```
pip install -r requirement.txt
```
Ensure you have a valid Google API key set in your environment variables as `GOOGLE_API_KEY` for AI feedback generation.

## Sample Output
The reports provide:
- A summary of correct and incorrect answers, and overall accuracy.
- Motivational, personalized feedback highlighting strengths and areas for improvement.
- Detailed analysis of chapter-wise and concept-wise performance.
- Actionable study suggestions tailored to Indian engineering entrance exam preparation.
- A downloadable PDF report with all the above information formatted clearly.

---

This system empowers educators and students with actionable insights and personalized coaching to improve learning outcomes effectively.
