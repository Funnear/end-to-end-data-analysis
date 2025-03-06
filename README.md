# Research: What is the difference in music sales trends for Discogs and Bandcamp?

Collect information about music sales from popular platforms Discogs and Bandcamp.
Get insights to the differences and similarities in customer choices for music purchases.

## Dataset description
- Initial datasets, sources, column descriptions from the sources and preliminary cleaning:
  - [source_datasets, notebook](notebooks/source_datasets.ipynb)
- EDA reports
  - [automated preliminary EDA report, md](reports/eda_raw_report.md)
  - [Manual EDA report, md](reports/eda_manual_report.md)

## Methodology
- Exploratory Data Analysis (EDA), including:
  - Data quality analysis and cleanup
  - Identifying numeric and categorical data columns
  - Identifying discrete and continuous data
  - Identifying ordinal and nominal data
- Elements of Principal Component Analysis (PCA)
  - Reducing the dimensionality of large datasets while preserving as much information as possible to make data analysis simpler and more efficient
- Performance optimization for data processing

## Results:

### Key insights
1. Bandcamp is selling more digital media, Discogs is selling more physical media
2. Vynil sales are higher than CD sales everywhere, but on Discogs they are very close
3. The most popular genres on Discogs are Rock and Electronic music

### Frequency diagrams
- [Bandcamp media types distribution, donut chart ](img/bandcamp_media_types.png)
- [Discogs media types distribution, donut chart ](img/discogs_media_types.png)
- [Discogs genre distribution, donut chart ](img/discogs_media_types.png)

---
## Developer setup
[Step-by-step set up guide](docs/developer_setup.md)

---

## Extra materials
- [Link to the presentation slides](https://docs.google.com/presentation/d/1hHTHP7KXCEfrOTBI1uSvPQ56_etWSohvZ1L22Vuh_kI/edit?usp=sharing)
- [Project task and requirements](docs/project_origins.md)
- [Project diary regarding technical and methodological challenges](docs/work_diary.md)

---

