# DBLP Co-Author Pattern Mining

A Python-based data mining tool designed to extract co-authorship transactions from the raw DBLP XML dataset and analyze close collaborator patterns using null-invariant correlation measures (Kulczynski and Cosine metrics).

---

## 📋 Table of Contents
- [Prerequisites](#-prerequisites)
- [How to Run the Project](#-how-to-run-the-project)
  - [Step 1: Data Extraction & Cleaning](#step-1-data-extraction--cleaning)
  - [Step 2: Pattern Mining](#step-2-pattern-mining)
- [Input & Output Files](#-input--output-files)

---

## ⚙️ Prerequisites

Before executing the scripts, ensure you have **Python 3.x** installed on your system. 

Install the required dependency libraries using `pip`:

```bash
pip install pandas numpy
```

---

## 🚀 How to Run the Project

Follow these step-by-step instructions to run the data pipeline from extraction to mining.

### Step 1: Data Extraction & Cleaning

1. Place the raw DBLP XML dataset (`dblp.xml`) and the extraction script (`dblp.py`) in your root working directory.
2. Run the extraction script to stream the XML dataset, parse entities, and generate cleaned co-author transaction lines:

```bash
python dblp.py
```

* **Sample Input:** `dblp.xml` (Raw DBLP XML dump file)
* **Generated Output:** `coauthors.txt` (Cleaned transaction lines containing co-authors per paper)

---

### Step 2: Pattern Mining

1. Ensure the generated `coauthors.txt` and the mining script (`minecoauthor.py`) are located in the same folder.
2. Execute the mining script to analyze itemsets, calculate frequencies, and compute correlation measures:

```bash
python minecoauthor.py
```

* **Sample Input:** `coauthors.txt`
* **Generated Output:** `coauthor_patterns.csv` (CSV file containing ranked closely-correlated co-author pairs)

---

## 📁 Input & Output Overview

| File Name | Type | Description |
| :--- | :--- | :--- |
| `dblp.xml` | Input | Original raw DBLP dataset dump. |
| `dblp.py` | Script | Parses raw XML data into structured transaction lines. |
| `coauthors.txt` | Intermediate | Cleaned list of co-author transaction pairs/groups. |
| `minecoauthor.py` | Script | Computes frequency & correlation scores (Kulczynski & Cosine). |
| `coauthor_patterns.csv` | Output | Final ranked patterns of closely correlated collaborators. |
