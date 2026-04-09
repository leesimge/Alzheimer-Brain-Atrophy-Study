import matplotlib.pyplot as plt
import seaborn as sns
from nilearn import datasets
import pandas as pd


print("Fetching real neuroimaging data from OASIS... Please wait.")
oasis_dataset = datasets.fetch_oasis_vbm(n_subjects=100)
df = pd.DataFrame(oasis_dataset.ext_vars)


df = df.dropna(subset=['age', 'nwbv', 'cdr'])
df['Clinical_Status'] = df['cdr'].map(lambda x: 'Dementia Group' if x > 0 else 'Healthy Control')

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 7))

custom_palette = {'Healthy Control': 'blue', 'Dementia Group': 'red'}

sns.scatterplot(
    data=df, 
    x='age', 
    y='nwbv', 
    hue='Clinical_Status', 
    palette=custom_palette, 
    s=120, 
    alpha=0.8,
    edgecolor='w'
)

plt.title('Neuroscience Portfolio: Age-Related Whole Brain Volume Atrophy (OASIS Dataset)', fontsize=16)
plt.xlabel('Age of Subject (Years)', fontsize=13)
plt.ylabel('Normalized Whole Brain Volume (nWBV)', fontsize=13)

plt.savefig('professional_oasis_analysis.png', dpi=300)
plt.show()

print("\n--- Project Summary ---")
print(f"Total subjects processed: {len(df)}")
print("Analysis exported with clinical color mapping (Blue: Healthy, Red: Dementia).")

df.to_csv('oasis_100_subjects.csv', index=False)