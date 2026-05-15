import pandas as pd

# Load datasets
schools = pd.read_csv('NJPubSchool.csv')
enrollment = pd.read_excel('enrollment_2425.xlsx')

# Clean school names
schools['school_name'] = schools['school_name'].astype(str).str.upper().str.strip()
enrollment['school_name'] = enrollment['school_name'].astype(str).str.upper().str.strip()

# Merge datasets
merged = enrollment.merge(schools, on='school_name', how='left')

# Calculate grades 5–8 totals
merged['grade_5_8_total'] = (
    merged['grade5'] +
    merged['grade6'] +
    merged['grade7'] +
    merged['grade8']
)

# Save merged dataset
merged.to_csv('merged_schools.csv', index=False)

print("Data cleaned and merged successfully.")
