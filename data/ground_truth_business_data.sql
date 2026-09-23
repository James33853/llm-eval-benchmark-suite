CREATE TABLE quarterly_financials (
    quarter VARCHAR(10),
    department VARCHAR(50),
    revenue DECIMAL(10,2),
    target_revenue DECIMAL(10,2),
    status VARCHAR(20)
);

INSERT INTO quarterly_financials VALUES 
('Q1 2024', 'Sales', 150000.00, 140000.00, 'Exceeded'),
('Q1 2024', 'Marketing', 45000.00, 50000.00, 'Missed'),
('Q1 2024', 'Engineering', 210000.00, 200000.00, 'Exceeded'),
('Q2 2024', 'Sales', 165000.00, 160000.00, 'Exceeded'),
('Q2 2024', 'Marketing', 48000.00, 50000.00, 'Missed');
