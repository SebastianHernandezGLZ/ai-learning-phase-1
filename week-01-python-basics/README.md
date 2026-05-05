# Week 01 - Python Basics

## Overview

This folder contains my first practical Python exercises for Phase 1 of my AI learning roadmap.

The main goal of this week was to practice Python fundamentals by building a simple customer classifier.

## Project: Customer Classifier

The project classifies potential customers based on their behavior.

Each customer has information such as:

- Name
- Age
- Career interest
- Contact channel
- Whether they replied
- Whether they requested information
- Whether they received follow-up
- Manual lead score

The classifier labels each customer as:

- Hot lead
- Warm lead
- Interested lead
- Cold lead

## Logic

The classification rules are:

- Hot lead: replied, requested information, and received follow-up.
- Warm lead: replied and requested information.
- Interested lead: replied but did not request information yet.
- Cold lead: did not reply.

## Python concepts practiced

- Variables
- Data types
- Conditionals
- Lists
- Dictionaries
- Loops
- Functions
- Basic project organization
- Git and GitHub workflow

## Files

- `customer_classifier.py`: main mini project for classifying customers.
- `exercises.py`: basic Python practice exercises.
- `test_notebook.ipynb`: basic Jupyter test file.

## How to run

Open the terminal inside this folder and run:

```bash
python customer_classifier.py
```

## Expected output

The program prints each customer summary and the final totals for each lead category.

Example final output:

Total de clientes revisados: 6
Total de Hot leads: 1
Total de Warm leads: 1
Total de Interested leads: 2
Total de Cold leads: 2

## What I learned

This week I learned how to write basic Python code and organize it into a small practical project. I practiced how to represent customer data using dictionaries, store multiple customers in a list, use functions to organize logic, and use Git/GitHub to save my progress.

## Next steps

Next week I will continue improving my Python skills and start preparing data in a more structured way for future analysis and machine learning.