

# #############SImple##################
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os


# def load_data(file_path):
#     """Load and validate data from the CSV file."""
#     if not os.path.exists(file_path):
#         print(f"Error: File '{file_path}' does not exist.")
#         return None

#     df = pd.read_csv(file_path)
#     required_columns = [
#         'Company', 'Period', 'Revenue', 'Net Income',
#         'Liabilities', 'Assets', 'Equity', 'ROA (%)',
#         'ROE (%)', 'Debt to Equity'
#     ]
#     missing_columns = [col for col in required_columns if col not in df.columns]
#     if missing_columns:
#         print(f"Error: Missing required columns: {missing_columns}")
#         return None

#     print(f"Loaded {len(df)} records successfully!")
#     return df


# def generate_summary(df):
#     """Generate summary statistics from the DataFrame."""
#     try:
#         total_revenue = df['Revenue'].sum()
#         avg_revenue_by_company = df.groupby('Company')['Revenue'].mean().to_dict()
#         yearly_revenue = df.groupby(df['Period'].str.split('/').str[2])['Revenue'].sum().to_dict()

#         summary = {
#             "Total Revenue": total_revenue,
#             "Average Revenue by Company": avg_revenue_by_company,
#             "Yearly Revenue": yearly_revenue
#         }
#         return summary
#     except Exception as e:
#         print(f"Error generating summary: {e}")
#         return {}


# def export_summary(summary, file_path):
#     """Export the summary to a CSV file."""
#     try:
#         df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
#         df.to_csv(file_path, index=False)
#         print(f"Summary saved to {file_path}")
#     except Exception as e:
#         print(f"Error exporting summary: {e}")


# def generate_visualizations(df, output_folder):
#     """Generate visualizations and save them to the output folder."""
#     try:
#         os.makedirs(output_folder, exist_ok=True)

#         # Top Companies by Revenue
#         top_companies = df.groupby('Company')['Revenue'].sum().sort_values(ascending=False).head(5)
#         plt.figure(figsize=(10, 6))
#         sns.barplot(x=top_companies.index, y=top_companies.values, palette='viridis')
#         plt.title("Top 5 Companies by Revenue")
#         plt.ylabel("Revenue")
#         plt.savefig(os.path.join(output_folder, "top_companies_by_revenue.png"))
#         plt.close()

#         # Revenue by Year
#         df['Year'] = df['Period'].str.split('/').str[2]
#         revenue_by_year = df.groupby('Year')['Revenue'].sum()
#         plt.figure(figsize=(10, 6))
#         revenue_by_year.plot(kind='line', marker='o', color='blue')
#         plt.title("Yearly Revenue Trends")
#         plt.ylabel("Revenue")
#         plt.savefig(os.path.join(output_folder, "yearly_revenue_trends.png"))
#         plt.close()

#         print(f"Visualizations saved to {output_folder}")
#     except Exception as e:
#         print(f"Error generating visualizations: {e}")


# def main():
#     file_path = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\top.csv"
#     output_folder = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\reports"
#     summary_file = os.path.join(output_folder, "summary_report.csv")

#     # Load Data
#     data = load_data(file_path)
#     if data is None:
#         return

#     # Generate and Display Summary
#     summary = generate_summary(data)
#     for key, value in summary.items():
#         print(f"{key}: {value}")

#     # Export Summary
#     export_summary(summary, summary_file)

#     # Generate Visualizations
#     generate_visualizations(data, output_folder)


# if __name__ == "__main__":
#     main()









#####################################################
########################  22222  ####################
#####################################################


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os


# def load_data(file_path):
#     """Load and validate data from the CSV file."""
#     if not os.path.exists(file_path):
#         print(f"Error: File '{file_path}' does not exist.")
#         return None

#     df = pd.read_csv(file_path)
#     required_columns = [
#         'Company', 'Period', 'Revenue', 'Net Income',
#         'Liabilities', 'Assets', 'Equity', 'ROA (%)',
#         'ROE (%)', 'Debt to Equity'
#     ]
#     missing_columns = [col for col in required_columns if col not in df.columns]
#     if missing_columns:
#         print(f"Error: Missing required columns: {missing_columns}")
#         return None

#     df['Year'] = df['Period'].str.split('/').str[2]  # Extract year from the period
#     print(f"Loaded {len(df)} records successfully!")
#     return df


# def generate_summary(df):
#     """Generate summary statistics from the DataFrame."""
#     try:
#         total_revenue = df['Revenue'].sum()
#         avg_net_income = df['Net Income'].mean()
#         avg_revenue_by_company = df.groupby('Company')['Revenue'].mean().to_dict()
#         yearly_revenue = df.groupby('Year')['Revenue'].sum().to_dict()
#         debt_to_equity_stats = df['Debt to Equity'].describe()

#         summary = {
#             "Total Revenue": total_revenue,
#             "Average Net Income": avg_net_income,
#             "Average Revenue by Company": avg_revenue_by_company,
#             "Yearly Revenue": yearly_revenue,
#             "Debt to Equity Stats": debt_to_equity_stats.to_dict(),
#         }
#         return summary
#     except Exception as e:
#         print(f"Error generating summary: {e}")
#         return {}


# def export_summary(summary, file_path):
#     """Export the summary to a CSV file."""
#     try:
#         summary_flat = []
#         for key, value in summary.items():
#             if isinstance(value, dict):
#                 for sub_key, sub_value in value.items():
#                     summary_flat.append({"Metric": f"{key} - {sub_key}", "Value": sub_value})
#             else:
#                 summary_flat.append({"Metric": key, "Value": value})

#         df = pd.DataFrame(summary_flat)
#         df.to_csv(file_path, index=False)
#         print(f"Summary saved to {file_path}")
#     except Exception as e:
#         print(f"Error exporting summary: {e}")


# def generate_visualizations(df, output_folder):
#     """Generate visualizations and save them to the output folder."""
#     try:
#         os.makedirs(output_folder, exist_ok=True)

#         # Top Companies by Revenue
#         top_companies = df.groupby('Company')['Revenue'].sum().sort_values(ascending=False).head(5)
#         plt.figure(figsize=(10, 6))
#         sns.barplot(x=top_companies.index, y=top_companies.values, palette='viridis')
#         plt.title("Top 5 Companies by Revenue")
#         plt.ylabel("Revenue")
#         plt.savefig(os.path.join(output_folder, "top_companies_by_revenue.png"))
#         plt.close()

#         # Revenue by Year
#         revenue_by_year = df.groupby('Year')['Revenue'].sum()
#         plt.figure(figsize=(10, 6))
#         revenue_by_year.plot(kind='line', marker='o', color='blue')
#         plt.title("Yearly Revenue Trends")
#         plt.ylabel("Revenue")
#         plt.savefig(os.path.join(output_folder, "yearly_revenue_trends.png"))
#         plt.close()

#         # Correlation Heatmap
#         numeric_cols = ['Revenue', 'Net Income', 'Liabilities', 'Assets', 'Equity', 'ROA (%)', 'ROE (%)', 'Debt to Equity']
#         plt.figure(figsize=(10, 8))
#         sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
#         plt.title("Correlation Heatmap")
#         plt.savefig(os.path.join(output_folder, "correlation_heatmap.png"))
#         plt.close()

#         # Revenue vs Net Income Scatter Plot
#         plt.figure(figsize=(10, 6))
#         sns.scatterplot(data=df, x='Revenue', y='Net Income', hue='Company', palette='Set2')
#         plt.title("Revenue vs. Net Income")
#         plt.xlabel("Revenue")
#         plt.ylabel("Net Income")
#         plt.savefig(os.path.join(output_folder, "revenue_vs_net_income.png"))
#         plt.close()

#         # Revenue Distribution
#         plt.figure(figsize=(10, 6))
#         sns.histplot(df['Revenue'], kde=True, color='purple', bins=20)
#         plt.title("Revenue Distribution")
#         plt.xlabel("Revenue")
#         plt.ylabel("Frequency")
#         plt.savefig(os.path.join(output_folder, "revenue_distribution.png"))
#         plt.close()

#         print(f"Visualizations saved to {output_folder}")
#     except Exception as e:
#         print(f"Error generating visualizations: {e}")


# def main():
#     file_path = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\top.csv"
#     output_folder = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\reports"
#     summary_file = os.path.join(output_folder, "summary_report.csv")

#     # Load Data
#     data = load_data(file_path)
#     if data is None:
#         return

#     # Generate and Display Summary
#     summary = generate_summary(data)
#     for key, value in summary.items():
#         print(f"{key}: {value}")

#     # Export Summary
#     export_summary(summary, summary_file)

#     # Generate Visualizations
#     generate_visualizations(data, output_folder)


# if __name__ == "__main__":
#     main()







####################################################
######################  3  #########################
####################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


class FinancialDataAnalyzer:
    def __init__(self, file_path, output_folder):
        self.file_path = file_path
        self.output_folder = output_folder
        self.data = None
        self.summary = {}

    def load_data(self):
        """Load and validate data from the CSV file."""
        if not os.path.exists(self.file_path):
            print(f"Error: File '{self.file_path}' does not exist.")
            return None

        df = pd.read_csv(self.file_path)
        required_columns = [
            'Company', 'Period', 'Revenue', 'Net Income',
            'Liabilities', 'Assets', 'Equity', 'ROA (%)',
            'ROE (%)', 'Debt to Equity'
        ]
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Error: Missing required columns: {missing_columns}")
            return None

        # Clean and preprocess data
        df['Year'] = df['Period'].str.split('/').str[2]
        df['Profit Margin (%)'] = (df['Net Income'] / df['Revenue']) * 100
        df['Revenue Growth (%)'] = df['Revenue'].pct_change() * 100  # Revenue Growth
        self.data = df
        print(f"Loaded {len(df)} records successfully!")

    def generate_summary(self):
        """Generate summary statistics from the data."""
        if self.data is None:
            print("Error: No data loaded. Please load the data first.")
            return

        try:
            total_revenue = self.data['Revenue'].sum()
            avg_profit_margin = self.data['Profit Margin (%)'].mean()
            top_performers = self.data.nlargest(5, 'ROE (%)')[['Company', 'ROE (%)']].to_dict(orient='records')
            debt_to_equity_trends = self.data.groupby('Year')['Debt to Equity'].mean().to_dict()

            self.summary = {
                "Total Revenue": total_revenue,
                "Average Profit Margin (%)": avg_profit_margin,
                "Top Performers (by ROE)": top_performers,
                "Debt to Equity Trends": debt_to_equity_trends
            }
            print("Summary generated successfully!")
        except Exception as e:
            print(f"Error generating summary: {e}")

    def export_summary(self):
        """Export the summary to a CSV file."""
        if not self.summary:
            print("Error: No summary available to export.")
            return

        try:
            summary_file = os.path.join(self.output_folder, "summary_report.csv")
            os.makedirs(self.output_folder, exist_ok=True)

            summary_flat = []
            for key, value in self.summary.items():
                if isinstance(value, list):  # Handle list of dictionaries (e.g., top performers)
                    for record in value:
                        summary_flat.append({"Metric": key, **record})
                elif isinstance(value, dict):  # Handle nested dictionaries
                    for sub_key, sub_value in value.items():
                        summary_flat.append({"Metric": f"{key} - {sub_key}", "Value": sub_value})
                else:
                    summary_flat.append({"Metric": key, "Value": value})

            df = pd.DataFrame(summary_flat)
            df.to_csv(summary_file, index=False)
            print(f"Summary saved to {summary_file}")
        except Exception as e:
            print(f"Error exporting summary: {e}")

    def generate_visualizations(self):
        """Generate visualizations and save them to the output folder."""
        if self.data is None:
            print("Error: No data loaded. Please load the data first.")
            return

        try:
            os.makedirs(self.output_folder, exist_ok=True)

            # 1. Revenue Growth Rate by Year
            growth_trends = self.data.groupby('Year')['Revenue Growth (%)'].mean()
            plt.figure(figsize=(10, 6))
            plt.bar(growth_trends.index, growth_trends.values, color='skyblue')
            plt.title("Revenue Growth Rate by Year")
            plt.xlabel("Year")
            plt.ylabel("Revenue Growth (%)")
            plt.grid(axis='y')
            plt.savefig(os.path.join(self.output_folder, "revenue_growth_rate.png"))
            plt.close()

            # 2. Net Income vs Liabilities Correlation
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=self.data, x='Liabilities', y='Net Income', size='Equity', sizes=(50, 500), alpha=0.6)
            plt.title("Net Income vs Liabilities (Bubble Size: Equity)")
            plt.xlabel("Liabilities")
            plt.ylabel("Net Income")
            plt.savefig(os.path.join(self.output_folder, "net_income_vs_liabilities.png"))
            plt.close()

            # 3. ROA Distribution
            plt.figure(figsize=(10, 6))
            sns.histplot(self.data['ROA (%)'], kde=True, bins=20, color='purple')
            plt.title("Distribution of ROA (%)")
            plt.xlabel("ROA (%)")
            plt.ylabel("Frequency")
            plt.savefig(os.path.join(self.output_folder, "roa_distribution.png"))
            plt.close()

            # 4. Top 5 Companies by Profit Margin
            top_profit_margin = self.data.groupby('Company')['Profit Margin (%)'].mean().nlargest(5)
            plt.figure(figsize=(10, 6))
            sns.barplot(x=top_profit_margin.index, y=top_profit_margin.values, palette='Blues_d')
            plt.title("Top 5 Companies by Average Profit Margin (%)")
            plt.ylabel("Profit Margin (%)")
            plt.savefig(os.path.join(self.output_folder, "top_companies_profit_margin.png"))
            plt.close()

            # 5. Assets vs Liabilities Bubble Chart
            plt.figure(figsize=(10, 6))
            plt.scatter(
                self.data['Assets'], self.data['Liabilities'],
                s=self.data['Equity'] / 1e6, alpha=0.6, c='green', edgecolors="black"
            )
            plt.title("Assets vs Liabilities (Bubble Size: Equity)")
            plt.xlabel("Assets")
            plt.ylabel("Liabilities")
            plt.savefig(os.path.join(self.output_folder, "assets_vs_liabilities_bubble.png"))
            plt.close()

            # 6. Equity Breakdown by Year (Stacked Bar Chart)
            equity_by_company = self.data.pivot_table(values='Equity', index='Year', columns='Company', aggfunc='sum', fill_value=0)
            equity_by_company.plot(kind='bar', stacked=True, figsize=(12, 8), cmap='tab20')
            plt.title("Equity Breakdown by Year")
            plt.ylabel("Equity")
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.savefig(os.path.join(self.output_folder, "equity_breakdown_by_year.png"))
            plt.close()

            # 7. Cumulative Revenue Share (Pareto Chart)
            company_revenue = self.data.groupby('Company')['Revenue'].sum().sort_values(ascending=False)
            cumulative_revenue = company_revenue.cumsum() / company_revenue.sum() * 100
            plt.figure(figsize=(10, 6))
            plt.bar(company_revenue.index, company_revenue.values, color='gray')
            plt.plot(company_revenue.index, cumulative_revenue.values, marker='o', color='red', label='Cumulative Revenue (%)')
            plt.title("Cumulative Revenue Share by Companies")
            plt.xlabel("Companies")
            plt.ylabel("Revenue")
            plt.legend()
            plt.xticks(rotation=45, ha='right')
            plt.savefig(os.path.join(self.output_folder, "cumulative_revenue_share.png"))
            plt.close()

            print(f"Visualizations saved to {self.output_folder}")
        except Exception as e:
            print(f"Error generating visualizations: {e}")


def main():
    file_path = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\top.csv"
    output_folder = r"C:\Users\BUZZ TECH\pythonLabs\CP_Project\reports"

    analyzer = FinancialDataAnalyzer(file_path, output_folder)
    analyzer.load_data()
    analyzer.generate_summary()
    analyzer.export_summary()
    analyzer.generate_visualizations()


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
