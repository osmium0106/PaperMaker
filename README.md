# PaperMaker

A Streamlit app for generating, editing, and exporting question papers and answer sheets from uploaded PDFs, with AI-powered question generation and Word/PDF export.

## Features
- Upload PDF(s) and generate question papers and answer sheets using Gemini AI
- Specify paper metadata, sections, and question types
- Bulk question generation per section
- Download as PDF or editable Word (docx)
- Edit the question paper in a Word-like interface and export as PDF
- Unicode font support for math and symbols

## Setup Instructions

### 1. Clone the repository
```sh
git clone <your-repo-url>
cd PaperMaker
```

### 2. Create a virtual environment (Windows)
```sh
python -m venv venv
venv\Scripts\activate
```

If you are on Mac/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

#### For Word to PDF export (optional, Windows only):
```sh
pip install docx2pdf pywin32
```

### 4. Set up your environment variables
Create a `.env` file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Run the Streamlit app
```sh
streamlit run app.py
```

The app will open in your browser at [http://localhost:8501](http://localhost:8501).

## Usage
- Use the sidebar to upload your PDF(s) and select the desired workflow.
- Fill out the form to generate a question paper.
- Download the generated PDFs or edit the question paper in Word format.
- After editing, export the final version as PDF (requires `docx2pdf` and `pywin32` on Windows).

## Notes
- All sensitive files and outputs are ignored by `.gitignore` and will not be pushed to GitHub.
- For best results, use the app on Windows for full PDF export support from Word.

---

For any issues, please open an issue on the repository or contact the maintainer.