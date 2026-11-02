# AI Resume Screening & Candidate Ranking System

## What is included
- Separate Candidate and Admin portals
- Candidate registration/login; admin accounts are created locally only
- Admin can create/edit/open/close vacancies, rank applicants, review resume skills, update statuses, and download PDF ranking reports
- Candidates can search vacancies, apply with PDF/DOCX, view their own scores/statuses, see matched/missing skills, and explore more open jobs
- SQLite database, password hashing, role checks, upload extension validation, 5 MB upload limit
- TF-IDF/cosine similarity plus skill coverage for explainable matching

## Scoring
Required skill coverage = matched required skills / total required skills × 100.
Overall score = 60% skill coverage + 40% TF-IDF text similarity.
This score is an educational matching indicator, not a hiring probability. A human must make hiring decisions.

## Setup (Windows + PyCharm)
1. Extract the ZIP and open the folder in PyCharm.
2. Select a Python interpreter (Python 3.10–3.13 recommended).
3. Open the PyCharm Terminal and run `python -m pip install -r requirements.txt`.
4. Run `python create_admin.py` and follow the prompts.
5. Run `app.py`.
6. Open `http://127.0.0.1:5000` in your browser.
7. Log in as admin and create a vacancy. Register a candidate account and apply using the included demo resume.

If `python` is not recognized in Windows CMD, use the interpreter configured in PyCharm or try `py -m pip install -r requirements.txt`.

## Limitations and responsible use
- Scanned/image-only PDFs are not supported; OCR is not included.
- Skill extraction uses a predefined skill bank and simple matching, not a production-grade resume parser.
- This is a local educational project using SQLite and Flask's development server. Do not expose it publicly as-is; set a strong `FLASK_SECRET_KEY` before deployment.
- Use fictional resumes during demonstrations. Candidate data is sensitive. Do not automatically reject people based only on this score.
