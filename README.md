# Age-Related Whole Brain Volume Atrophy Analysis

This project investigates the correlation between aging and brain volume loss (atrophy) using real-world neuroimaging data.

## Project Overview
The analysis utilizes the **OASIS-1 (Open Access Series of Imaging Studies)** dataset to visualize how Normalized Whole Brain Volume (nWBV) decreases with age and how this process differs in clinical dementia.

## Methodology
- **Data Source:** OASIS cross-sectional MRI data via `nilearn`.
- **Pre-processing:** Data cleaning performed to handle missing values (final sample size n=56).
- **Visualization:** Scatter plots with clinical group mapping (Healthy Control vs. Dementia Group).
- **Libraries:** `Pandas`, `Seaborn`, `Matplotlib`, `Nilearn`, `Scipy`.

## Key Findings
The visualization clearly demonstrates a negative correlation between age and nWBV. Furthermore, subjects in the Dementia Group show a more pronounced volume loss compared to age-matched healthy controls.

---
*Developed for my Neuroscience PhD Portfolio.*
