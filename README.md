# DBLP Co-Author Pattern Mining

A Python-based project for parsing large-scale DBLP XML datasets, extracting co-author relationships, and mining closely-correlated co-author pairs using null-invariant measures (Kulczynski and Cosine).

---

## 🛠️ Environment Setup & Prerequisites

Make sure you have **Python 3** installed on your system. 

Install the required Python packages by running the following command in your terminal:

```bash
pip install pandas numpy
```

---

## 🚀 How to Run the Project (Step-by-Step Guide)

### Step 1: Extracting and Cleaning the DBLP Dataset
1. Place the raw DBLP XML dataset (`dblp.xml`) and the extraction script (`dblp.py`) in the same working directory.
2. Run the extraction script to stream the dataset, handle special XML entities, and generate the cleaned transactions file:

```bash
python dblp.py
```

* **Sample Input:** `dblp.xml` (Raw DBLP XML dump file)
* **Generated Output:** `coauthors.txt` (Cleaned transaction lines containing co-authors per paper)

---

### Step 2: Mining Close Collaborators
1. Ensure `coauthors.txt` and the mining script (`minecoauthor.py`) are in the same folder.
2. Execute the mining script to process transactions, calculate individual frequencies, and compute correlation measures:

```bash
python minecoauthor.py
```

* **Sample Input:** `coauthors.txt`
* **Generated Output:** `coauthor_patterns.csv` (CSV file containing ranked closely-correlated co-author pairs)

---

## 📁 File Structure

```text
├── dblp.py               # Script for parsing and cleaning dblp.xml
├── minecoauthor.py       # Script for mining frequent patterns & correlation
├── dblp.xml              # Raw dataset (Input)
├── coauthors.txt         # Cleaned transactions (Intermediate Output)
└── coauthor_patterns.csv # Final ranked output patterns (Generated Output)
```
