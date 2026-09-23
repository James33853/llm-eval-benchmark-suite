import sqlite3
import pandas as pd

def run_evaluation():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    with open('data/ground_truth_business_data.sql', 'r') as f:
        cursor.executescript(f.read())
    
    query = "SELECT revenue FROM quarterly_financials WHERE quarter='Q1 2024' AND department='Sales';"
    ground_truth_revenue = pd.read_sql_query(query, conn).iloc[0]['revenue']
    
    llm_generated_claim = 150000.00
    is_accurate = (ground_truth_revenue == llm_generated_claim)
    
    print("--- LLM EVALUATION RESULTS ---")
    print(f"Ground Truth Q1 Sales Revenue: ${ground_truth_revenue:,.2f}")
    print(f"LLM Claimed Revenue: ${llm_generated_claim:,.2f}")
    print(f"Factual Accuracy Passed: {is_accurate}")
    print(f"Hallucination Flag: {'NO HALLUCINATION DETECTED' if is_accurate else 'CRITICAL HALLUCINATION DETECTED'}")

if __name__ == "__main__":
    run_evaluation()
