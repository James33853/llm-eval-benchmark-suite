# Enterprise LLM Response Evaluation & Hallucination Benchmark Framework

Designed and maintained by **James Larry**  
[LinkedIn Profile] | [Email: jameslarryh3654@gmail.com]

## Project Overview
This project provides an evaluation framework to assess LLM outputs against ground-truth business data. It benchmarks AI model performance across four key dimensions:
1. **Factual Accuracy:** Cross-referencing generated numbers against SQL ground-truth databases.
2. **Instruction Adherence:** Verifying model compliance with prompt constraints, formatting requirements, and negative constraints.
3. **Hallucination Detection:** Identifying unsupported statements or fabricated metrics in business summaries.
4. **Logical Consistency:** Evaluating multi-step financial reasoning and KPI calculations.

## Tech Stack & Skills Highlighted
- **Languages:** Python (Pandas, SQLite3), SQL
- **AI Evaluation Methodology:** RLHF Rubric Design, SFT Guidance, Red-Teaming, Prompt Engineering
- **Domain Focus:** Business Intelligence, Operations, Data Analytics

## Framework Architecture
1. **Database Tier (`data/ground_truth_business_data.sql`):** Establishes structured operational metrics to test precision.
2. **Evaluation Engine (`scripts/data_validator.py`):** Runs comparative scripts against SQL queries to output pass/fail scores.
