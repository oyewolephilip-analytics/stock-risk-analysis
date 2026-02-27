📊 Stock Risk Analysis Research Project

Volatility, VaR, Drawdown & Risk-Adjusted Performance

⸻

🔹 Project Overview

This project analyzes the risk characteristics of selected equities using quantitative financial modeling techniques.

The objective is to evaluate downside risk exposure, volatility behavior, and risk-adjusted performance using historical market data.

The analysis is implemented in Python and visualized through a Power BI dashboard.

⸻

🔹 Research Objectives
	•	Measure daily return behavior
	•	Estimate historical volatility
	•	Compute 95% Historical Simulation Value-at-Risk (VaR)
	•	Calculate Expected Shortfall (Conditional VaR)
	•	Analyze Maximum Drawdown
	•	Evaluate Sharpe Ratio
	•	Compare risk profiles across assets

⸻

🔹 Methodology
	1.	Historical price data collection
	2.	Daily log/simple return computation
	3.	Volatility estimation (annualized)
	4.	Historical Simulation VaR calculation
	5.	Expected Shortfall estimation
	6.	Cumulative return and running maximum computation
	7.	Drawdown analysis
	8.	Risk-adjusted performance measurement

No parametric distribution assumptions were imposed for VaR estimation, allowing the model to reflect actual historical market behavior.

⸻

🔹 Tools & Technologies
	•	Python (pandas, numpy, scipy)
	•	Power BI
	•	Parquet data export for structured reporting
	•	Git version control

⸻

🔹 Repository Structure
	•	src/ → Core risk modeling script
	•	data/ → Historical price datasets
	•	notebooks/ → Exploratory research notebook
	•	screenshots/ → Dashboard visuals
	•	.pbix → Power BI dashboard file

⸻

🔹 Key Insights Explored
	•	Sensitivity of portfolio risk to allocation weights
	•	Comparison of volatility regimes
	•	Tail-risk magnitude under stress conditions
	•	Capital erosion measured through drawdown

🔹 Dashboard Preview
![Dashboard Overview](screenshots/dashboard_overview.png)
![Risk Metrics](screenshots/risk_metrics.png)
