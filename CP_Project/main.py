

#############SImple##################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def load_data(file_path):
    """Load and validate data from the CSV file."""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return None

    df = pd.read_csv(file_path)
    required_columns = [
        'Company', 'Period', 'Revenue', 'Net Income',
        'Liabilities', 'Assets', 'Equity', 'ROA (%)',
        'ROE (%)', 'Debt to Equity'
    ]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Error: Missing required columns: {missing_columns}")
        return None

    print(f"Loaded {len(df)} records successfully!")
    return df


def generate_summary(df):
    """Generate summary statistics from the DataFrame."""
    try:
        total_revenue = df['Revenue'].sum()
        avg_revenue_by_company = df.groupby('Company')['Revenue'].mean().to_dict()
        yearly_revenue = df.groupby(df['Period'].str.split('/').str[2])['Revenue'].sum().to_dict()

        summary = {
            "Total Revenue": total_revenue,
            "Average Revenue by Company": avg_revenue_by_company,
            "Yearly Revenue": yearly_revenue
        }
        return summary
    except Exception as e:
        print(f"Error generating summary: {e}")
        return {}


def export_summary(summary, file_path):
    """Export the summary to a CSV file."""
    try:
        df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
        df.to_csv(file_path, index=False)
        print(f"Summary saved to {file_path}")
    except Exception as e:
        print(f"Error exporting summary: {e}")


def generate_visualizations(df, output_folder):
    """Generate visualizations and save them to the output folder."""
    try:
        os.makedirs(output_folder, exist_ok=True)

        # Top Companies by Revenue
        top_companies = df.groupby('Company')['Revenue'].sum().sort_values(ascending=False).head(5)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_companies.index, y=top_companies.values, palette='viridis')
        plt.title("Top 5 Companies by Revenue")
        plt.ylabel("Revenue")
        plt.savefig(os.path.join(output_folder, "top_companies_by_revenue.png"))
        plt.close()

        # Revenue by Year
        df['Year'] = df['Period'].str.split('/').str[2]
        revenue_by_year = df.groupby('Year')['Revenue'].sum()
        plt.figure(figsize=(10, 6))
        revenue_by_year.plot(kind='line', marker='o', color='blue')
        plt.title("Yearly Revenue Trends")
        plt.ylabel("Revenue")
        plt.savefig(os.path.join(output_folder, "yearly_revenue_trends.png"))
        plt.close()

        print(f"Visualizations saved to {output_folder}")
    except Exception as e:
        print(f"Error generating visualizations: {e}")


def main():
    file_path = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\top.csv"
    output_folder = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\reports"
    summary_file = os.path.join(output_folder, "summary_report.csv")

    # Load Data
    data = load_data(file_path)
    if data is None:
        return

    # Generate and Display Summary
    summary = generate_summary(data)
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Export Summary
    export_summary(summary, summary_file)

    # Generate Visualizations
    generate_visualizations(data, output_folder)


if __name__ == "__main__":
    main()

































# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os


# # Class to represent individual sales records
# class SalesRecord:
#     def __init__(self, company, period, revenue, net_income, liabilities, assets, equity, roa, roe, debt_to_equity):
#         self.Company = company
#         self.Period = period
#         self.Revenue = revenue
#         self.Net_Income = net_income
#         self.Liabilities = liabilities
#         self.Assets = assets
#         self.Equity = equity
#         self.ROA = roa
#         self.ROE = roe
#         self.Debt_to_Equity = debt_to_equity


# # Class to manage sales data
# class SalesManager:
#     def __init__(self):
#         self.records = []

#     def load_data(self, file_path):
#         try:
#             if not os.path.exists(file_path):
#                 print(f"Error: File '{file_path}' does not exist.")
#                 return

#             df = pd.read_csv(file_path)

#             # Display the available columns for debugging
#             print("Available Columns in File:")
#             print(df.columns.tolist())

#             required_columns = [
#                 'Company', 'Period', 'Revenue', 'Net Income', 
#                 'Liabilities', 'Assets', 'Equity', 'ROA (%)', 
#                 'ROE (%)', 'Debt to Equity'
#             ]
#             missing_columns = [col for col in required_columns if col not in df.columns]

#             if missing_columns:
#                 print(f"Error: Missing required columns: {missing_columns}")
#                 return

#             for _, row in df.iterrows():
#                 record = SalesRecord(
#                     row['Company'], row['Period'], row['Revenue'], row['Net Income'],
#                     row['Liabilities'], row['Assets'], row['Equity'], row['ROA (%)'],
#                     row['ROE (%)'], row['Debt to Equity']
#                 )
#                 self.records.append(record)

#             print(f"Loaded {len(self.records)} records successfully!")
#         except Exception as e:
#             print(f"Error loading file: {e}")

#     def get_summary(self):
#         try:
#             df = self.to_dataframe()

#             # Debug: Check the actual columns in DataFrame
#             print("Columns in DataFrame:")
#             print(df.columns.tolist())

#             if 'Revenue' not in df.columns:
#                 print("Error in summary computation: Missing column 'Revenue'")
#                 return {}

#             summary = {
#                 "Total Revenue": df['Revenue'].sum(),
#                 "Average Revenue by Company": df.groupby('Company')['Revenue'].mean().to_dict(),
#                 "Yearly Revenue": df.groupby(df['Period'].str.split('/').str[2])['Revenue'].sum().to_dict()
#             }
#             return summary
#         except Exception as e:
#             print(f"Error in summary computation: {e}")
#             return {}

#     def to_dataframe(self):
#         if not self.records:
#             print("No records available to convert to DataFrame.")
#             return pd.DataFrame()
#         # Convert records to DataFrame with consistent column names
#         return pd.DataFrame([{
#             'Company': record.Company,
#             'Period': record.Period,
#             'Revenue': record.Revenue,
#             'Net Income': record.Net_Income,
#             'Liabilities': record.Liabilities,
#             'Assets': record.Assets,
#             'Equity': record.Equity,
#             'ROA (%)': record.ROA,
#             'ROE (%)': record.ROE,
#             'Debt to Equity': record.Debt_to_Equity
#         } for record in self.records])


# # Class to generate reports and visualizations
# class ReportGenerator:
#     @staticmethod
#     def top_companies_by_revenue(manager, top_n=5):
#         df = manager.to_dataframe()
#         if 'Company' not in df.columns or 'Revenue' not in df.columns:
#             print("Error: Missing required columns 'Company' or 'Revenue' for top companies computation.")
#             return pd.Series()
#         return df.groupby('Company')['Revenue'].sum().sort_values(ascending=False).head(top_n)

#     @staticmethod
#     def revenue_by_period(manager):
#         df = manager.to_dataframe()
#         if 'Period' not in df.columns or 'Revenue' not in df.columns:
#             print("Error: Missing required columns 'Period' or 'Revenue' for revenue by period computation.")
#             return pd.Series()
#         df['Year'] = df['Period'].str.split('/').str[2]
#         return df.groupby('Year')['Revenue'].sum()

#     @staticmethod
#     def export_summary(summary, file_name):
#         try:
#             df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
#             df.to_csv(file_name, index=False)
#             print(f"Summary saved to {file_name}")
#         except Exception as e:
#             print(f"Error exporting summary: {e}")

#     @staticmethod
#     def generate_visualizations(manager, output_folder):
#         try:
#             df = manager.to_dataframe()

#             if 'Company' not in df.columns or 'Revenue' not in df.columns:
#                 print("Error: Missing required columns for visualizations.")
#                 return

#             # Top Companies by Revenue Bar Chart
#             top_companies = df.groupby('Company')['Revenue'].sum().sort_values(ascending=False).head(5)
#             plt.figure(figsize=(10, 6))
#             sns.barplot(x=top_companies.index, y=top_companies.values, palette='viridis')
#             plt.title("Top 5 Companies by Revenue")
#             plt.ylabel("Revenue")
#             plt.savefig(os.path.join(output_folder, "top_companies_by_revenue.png"))
#             plt.close()

#             # Revenue by Year Line Chart
#             df['Year'] = df['Period'].str.split('/').str[2]
#             revenue_by_year = df.groupby('Year')['Revenue'].sum()
#             plt.figure(figsize=(10, 6))
#             revenue_by_year.plot(kind='line', marker='o', color='blue')
#             plt.title("Yearly Revenue Trends")
#             plt.ylabel("Revenue")
#             plt.savefig(os.path.join(output_folder, "yearly_revenue_trends.png"))
#             plt.close()

#             # Debt-to-Equity Distribution Pie Chart
#             debt_to_equity = df.groupby('Company')['Debt to Equity'].mean()
#             plt.figure(figsize=(8, 8))
#             debt_to_equity.plot(kind='pie', autopct='%1.1f%%', startangle=140)
#             plt.title("Debt-to-Equity Distribution by Company")
#             plt.ylabel("")
#             plt.savefig(os.path.join(output_folder, "debt_to_equity_distribution.png"))
#             plt.close()

#             print(f"Visualizations saved to {output_folder}")
#         except Exception as e:
#             print(f"Error generating visualizations: {e}")


# # Main function to run the program
# def main():
#     # File path and output folder
#     file_path = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\top.csv"
#     output_folder = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\reports"
#     os.makedirs(output_folder, exist_ok=True)

#     # Create objects for SalesManager and ReportGenerator
#     manager = SalesManager()
#     report_gen = ReportGenerator()

#     # Load Data
#     manager.load_data(file_path)

#     # Display Summary
#     summary = manager.get_summary()
#     if summary:
#         for key, value in summary.items():
#             print(f"{key}: {value}")

#     # Generate and Save Visualizations
#     report_gen.generate_visualizations(manager, output_folder)

#     # Save Summary Report
#     summary_file = os.path.join(output_folder, "summary_report.csv")
#     report_gen.export_summary(summary, summary_file)


# if __name__ == "__main__":
#     main()















# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os


# # Class to represent individual sales records
# class SalesRecord:
#     def __init__(self, company, period, revenue, net_income, liabilities, assets, equity, roa, roe, debt_to_equity):
#         self.company = company
#         self.period = period
#         self.revenue = revenue
#         self.net_income = net_income
#         self.liabilities = liabilities
#         self.assets = assets
#         self.equity = equity
#         self.roa = roa
#         self.roe = roe
#         self.debt_to_equity = debt_to_equity


# # Class to manage sales data
# class SalesManager:
#     def __init__(self):
#         self.records = []

#     def load_data(self, file_path):
#         try:
#             if not os.path.exists(file_path):
#                 print(f"Error: File '{file_path}' does not exist.")
#                 return

#             # Load CSV into a DataFrame
#             df = pd.read_csv(file_path)

#             # Validate required columns
#             required_columns = [
#                 'Company', 'Period', 'Revenue', 'Net Income', 'Liabilities', 
#                 'Assets', 'Equity', 'ROA (%)', 'ROE(%)', 'Debt to Equity'
#             ]
#             missing_columns = [col for col in required_columns if col not in df.columns]
#             if missing_columns:
#                 print(f"Error: Missing required columns: {missing_columns}")
#                 return

#             # Populate records
#             for _, row in df.iterrows():
#                 record = SalesRecord(
#                     row['Company'], row['Period'], row['Revenue'], row['Net Income'],
#                     row['Liabilities'], row['Assets'], row['Equity'], row['ROA (%)'],
#                     row['ROE(%)'], row['Debt to Equity']
#                 )
#                 self.records.append(record)

#             print(f"Loaded {len(self.records)} records successfully!")
#         except pd.errors.EmptyDataError:
#             print(f"Error: File '{file_path}' is empty.")
#         except pd.errors.ParserError:
#             print(f"Error: File '{file_path}' contains invalid data.")
#         except Exception as e:
#             print(f"Error loading file: {e}")

#     def get_summary(self):
#         try:
#             df = self.to_dataframe()

#             summary = {
#                 "Total Revenue": df['Revenue'].sum(),
#                 "Average Revenue by Company": df.groupby('Company')['Revenue'].mean().to_dict(),
#                 "Yearly Revenue": df.groupby(df['Period'].str.split('/').str[2])['Revenue'].sum().to_dict()
#             }
#             return summary
#         except KeyError as e:
#             print(f"Error in summary computation: Missing column {e}")
#             return {}
#         except Exception as e:
#             print(f"Error in summary computation: {e}")
#             return {}

#     def to_dataframe(self):
#         return pd.DataFrame([vars(record) for record in self.records])


# # Class to generate reports and visualizations
# class ReportGenerator:
#     @staticmethod
#     def top_companies_by_revenue(manager, top_n=5):
#         df = manager.to_dataframe()
#         top_companies = df.groupby('Company')['Revenue'].sum().sort_values(ascending=False).head(top_n)
#         return top_companies

#     @staticmethod
#     def revenue_by_period(manager):
#         df = manager.to_dataframe()
#         df['Year'] = df['Period'].str.split('/').str[2]
#         return df.groupby('Year')['Revenue'].sum()

#     @staticmethod
#     def export_summary(summary, file_name):
#         try:
#             df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
#             df.to_csv(file_name, index=False)
#             print(f"Summary saved to {file_name}")
#         except Exception as e:
#             print(f"Error exporting summary: {e}")

#     @staticmethod
#     def generate_visualizations(manager, output_folder):
#         try:
#             df = manager.to_dataframe()

#             # Top Companies by Revenue Bar Chart
#             top_companies = df.groupby('Company')['Revenue'].sum().sort_values(ascending=False).head(5)
#             plt.figure(figsize=(10, 6))
#             sns.barplot(x=top_companies.index, y=top_companies.values, palette='viridis')
#             plt.title("Top 5 Companies by Revenue")
#             plt.ylabel("Revenue")
#             plt.savefig(os.path.join(output_folder, "top_companies_by_revenue.png"))
#             plt.close()

#             # Revenue by Year Line Chart
#             df['Year'] = df['Period'].str.split('/').str[2]
#             revenue_by_year = df.groupby('Year')['Revenue'].sum()
#             plt.figure(figsize=(10, 6))
#             revenue_by_year.plot(kind='line', marker='o', color='blue')
#             plt.title("Yearly Revenue Trends")
#             plt.ylabel("Revenue")
#             plt.savefig(os.path.join(output_folder, "yearly_revenue_trends.png"))
#             plt.close()

#             # Debt-to-Equity Distribution Pie Chart
#             debt_to_equity = df.groupby('Company')['Debt to Equity'].mean()
#             plt.figure(figsize=(8, 8))
#             debt_to_equity.plot(kind='pie', autopct='%1.1f%%', startangle=140)
#             plt.title("Debt-to-Equity Distribution by Company")
#             plt.ylabel("")
#             plt.savefig(os.path.join(output_folder, "debt_to_equity_distribution.png"))
#             plt.close()

#             print(f"Visualizations saved to {output_folder}")
#         except KeyError as e:
#             print(f"Error generating visualizations: Missing column {e}")
#         except Exception as e:
#             print(f"Error generating visualizations: {e}")


# # Main function to run the program
# def main():
#     # File path and output folder
#     file_path = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\top.csv"
#     output_folder = 'reports'
#     os.makedirs(output_folder, exist_ok=True)

#     # Create objects for SalesManager and ReportGenerator
#     manager = SalesManager()
#     report_gen = ReportGenerator()

#     # Load Data
#     manager.load_data(file_path)

#     # Display Summary
#     summary = manager.get_summary()
#     if summary:
#         for key, value in summary.items():
#             print(f"{key}: {value}")

#         # Generate and Save Visualizations
#         report_gen.generate_visualizations(manager, output_folder)

#         # Save Summary Report
#         summary_file = os.path.join(output_folder, "summary_report.csv")
#         report_gen.export_summary(summary, summary_file)


# if __name__ == "__main__":
#     main()
