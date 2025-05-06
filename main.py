import pandas as pd
import os

# Load CSV file
input_file = "market_data.csv"
df = pd.read_csv(input_file)

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Filter for "Counter-Strike 2" game only
df_cs2 = df[df["Game Name"].str.strip().str.lower() == "counter-strike 2"]

# Filter for item names that contain "case" (case-insensitive)
df_cases = df_cs2[df_cs2["Item Name"].str.lower().str.contains("case")]

# Drop unwanted columns
columns_to_drop = [
    "Game Name",
    "Price in Cents",
    "App Id",
    "Context Id",
    "Asset Id",
    "Instance Id",
    "Class Id",
    "Unowned Context Id",
    "Unowned Id",
    "Market Name",
]

# Make sure the column names match exactly after stripping
df_cases = df_cases.drop(
    columns=[col for col in columns_to_drop if col in df_cases.columns]
)

# Create output directory
output_dir = "cases_output"
os.makedirs(output_dir, exist_ok=True)

# Save entries for each case to its own CSV
for case_name, group in df_cases.groupby("Item Name"):
    # Create a safe filename
    safe_name = "".join(
        c for c in case_name if c.isalnum() or c in (" ", "-", "_")
    ).rstrip()
    output_path = os.path.join(output_dir, f"{safe_name}.csv")
    group.to_csv(output_path, index=False)

print(
    f"Saved {len(df_cases['Item Name'].unique())} cleaned case files to '{output_dir}/'"
)
