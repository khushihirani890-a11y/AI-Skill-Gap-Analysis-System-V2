# Resume Processing Flow

## Input

Resume PDF

## Process

### Step 1: Upload Resume

Student uploads resume PDF.

### Step 2: Read PDF

System reads PDF using:

- PyPDF2
- pdfplumber

### Step 3: Extract Text

PDF content is converted into plain text.

### Step 4: Extract Skills

System finds skills using skills_database.csv.

### Step 5: Compare Skills

Detected skills are compared with career_skills.csv.

### Step 6: Generate Resume Score

Score is calculated based on:

- Skills
- Projects
- Certifications
- GitHub

### Step 7: Generate Recommendations

System suggests:

- Missing Skills
- Courses
- Internships
- Workshops
- Learning Roadmap

## Output

Skill Gap Report

Contains:

- Resume Score
- Detected Skills
- Missing Skills
- Career Goal
- Recommendations
- Learning Roadmap
