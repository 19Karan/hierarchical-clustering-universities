# Hierarchical Clustering – University Segmentation

This project applies **Hierarchical Agglomerative Clustering** to group universities
based on academic, financial, and admission-related attributes.

## Objective
To identify natural groupings of universities for strategic analysis and decision-making.

## Techniques Used
- Data preprocessing and standardization
- Hierarchical Agglomerative Clustering
- Dynamic model training at runtime
- Interactive Streamlit application

## Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- Matplotlib / Seaborn

## How to Run
```bash
pip install -r requirements.txt
streamlit run hierarchical_clustering_app.py

## Note
This project intentionally does not include pre-trained model (.pkl) files.
The clustering model is trained dynamically when the application runs.
This approach ensures reproducibility and avoids model–data version mismatch.




hierarchical-clustering-universities/
│
├── hierarchical_clustering_app.py
├── hierarchical_clustering_analysis.ipynb
├── Universities.csv
├── requirements.txt
├── README.md
└── .gitignore
