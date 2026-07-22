# Skill Gap Analysis Module

## Objective

This module analyzes a student's resume, extracts skills, compares them with the required skills for the selected career, identifies missing skills, calculates a resume score, and generates a skill gap report.

## Step 1: Resume Reading

The student uploads a resume in PDF format.

The system reads the PDF using Python libraries such as:

- PyPDF2
- pdfplumber

 ## Step 2: Resume Text Extraction

The PDF is converted into plain text so that the system can analyze it.

## Step 3: Skill Extraction

The system searches for technical skills such as:

- Python
- Java
- SQL
- HTML
- CSS
- Machine Learning

## Step 4: Skill Gap Analysis

The detected skills are compared with the required skills of the selected career.

Missing skills are identified.

## Step 5: Resume Score

The resume is scored based on:

- Skills
- Projects
- Certifications
- GitHub Profile

## Step 6: Output

The final report will show:

- Resume Score
- Detected Skills
- Missing Skills
- Recommended Skills
- Career Goal
- Learning Roadmap
