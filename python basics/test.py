from functools import partial
from datetime import datetime

# Base report generation function
def generate_report(report_type, report_data, start_date, end_date):
    report_header = f"*** {report_type.upper()} REPORT ***\n"
    report_header += f"Period: {start_date} to {end_date}\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report_content = f"Details:\n{report_data}\n"
    return report_header + report_content

# Partial functions for specific report types
customer_sales_report = partial(generate_report, "Customer Sales")
product_performance_report = partial(generate_report, "Product Performance")
revenue_summary_report = partial(generate_report, "Revenue Summary")

# Example report data
customer_sales_data = "Customer: rossi | Total Purchases: $500"
product_performance_data = "Product: Laptop | Units Sold: 300"
revenue_summary_data = "Total Revenue: $150,000"

# Generate reports by only providing remaining arguments (data and date range)
customer_sales = customer_sales_report(
    report_data=customer_sales_data,
    start_date="2025-01-01",
    end_date="2025-01-15"
)

product_performance = product_performance_report(
    report_data=product_performance_data,
    start_date="2025-01-01",
    end_date="2025-01-15"
)

revenue_summary = revenue_summary_report(
    report_data=revenue_summary_data,
    start_date="2025-01-01",
    end_date="2025-01-15"
)

# Print reports
print(customer_sales)
print("\n" + "=" * 35 + "\n")
print(product_performance)
print("\n" + "=" * 35 + "\n")
print(revenue_summary)
