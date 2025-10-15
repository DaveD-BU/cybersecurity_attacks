---
applyTo: '**/*.ipynb'
---
# Copilot Custom Instructions for Repository

description: >
  This repository contains reproducible data science workflows using Jupyter notebooks. It focuses on NLP modeling, benchmarking, and output formatting for real-world robustness. The goal is to support transparent experimentation, mentoring, and deployment-ready pipelines.

coding_style: >
  - Use clear, descriptive variable names (e.g., `token_counts`, `beam_output`)
  - Prefer functional decomposition over monolithic cells
  - Keep notebooks modular: one modeling task per notebook
  - Use Markdown cells to explain rationale, assumptions, and edge cases
  - Avoid hidden state: re-run notebooks top-to-bottom without errors
  - Consolidate all the imports and from statements to the top of the notebook

design_patterns: >
  - Model evaluation must include reproducibility checks (e.g., fixed seeds, corpus normalization)
  - Use checkpoints and versioning for iterative development
  - Prefer beam search or sampling with diversity metrics for generation tasks
  - Separate data loading, preprocessing, modeling, and evaluation into distinct sections
  - Always preserve a clean, unmodified copy of the original dataset to ensure reproducibility and enable audit trails

constraints: >
  - Avoid hardcoded paths or credentials
  - Do not use deprecated libraries or unstable APIs
  - Ensure compatibility with VSCode Jupyter and GitHub Codespaces
  - All notebooks must pass linting (e.g., `nbqa flake8`) and run without exceptions
  - Use lightweight dependencies unless explicitly required
  - Any preprocessing must operate on a copy of the dataset, not the original file
  - When creating notebooks, do not use the command line. Make all changes in the file.

tools_and_frameworks: >
  - Jupyter Notebooks (`.ipynb`)
  - Python 3.10+
  - kerasscikit-learn, pandas, matplotlib, seaborn
  - GitHub Actions for notebook validation and linting

additional_context: >
  - Whenever a new library is added, update `requirements.txt` accordingly
  - Follow best practices for data science and machine learning workflows
  - Save off clean versions of datasets before any preprocessing
  - Document all assumptions and decisions in Markdown cells
  
charting standards: >
  - Use `seaborn` for statistical visualizations
  - Use `matplotlib` for custom plots
  - Ensure all charts have titles, axis labels, and legends where applicable
  - Save figures in high resolution (300 dpi) for publication quality
  - Use consistent color palettes for related charts

COLOR_PALETTE = [
    "#c6d4e1",  # light blue-grey
    "#9bbcd4",  # soft blue
    "#6fa3c7",  # medium blue
    "#4a8ab8",  # strong blue
    "#2f6fa1",  # deep blue
    "#1f4f75",  # navy
    "#d3d3d3",  # light grey
    "#a9a9a9",  # medium grey
    "#696969",  # dark grey
]