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
## 📥 Dataset Source & Download
The raw DBLP XML dataset (`dblp.xml`) is required to run the extraction script. You can obtain it using the official sources below:
* **Direct XML Dump Download:** [https://dblp.org/xml/](https://dblp.org/xml/)
* **Download & Parsing FAQ Guide:** [https://dblp.org/faq/How+can+l+download+the+whole+dblp+dataset.html](https://dblp.org/faq/How+can+l+download+the+whole+dblp+dataset.html)

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

## QUESTIONS

**A) Propose a method to efficiently mine a set of coauthor relationships that are closely correlated (e.g. often coauthoring papers together).**

To efficiently mine close co-author relationships from the massive DBLP dataset (>5 GB), we can apply a streaming-based association analysis approach:

Efficient Streaming Extraction: Because the standard XML parser struggles with the large file size and special entity errors, we use a line-by-line streaming parser with Regular Expressions (re) to extract author names from <article> and <inproceedings> tags safely and quickly, writing them into a structured text file (coauthors.txt).

Minimum Support Pruning: To eliminate random pairings or rare collaborations, we apply a minimum support threshold (e.g., min_support = 5). Pairs with fewer joint papers than this threshold are pruned immediately.

Pair Generation & Correlation Computation: Using combination tools (itertools.combinations), we group authors by paper, generate unique pairs of co-authors, count individual and joint occurrences, and compute null-invariant correlation measures (Kulczynski and Cosine). The final results are exported to coauthor_patterns.csv.

**B) Based on the mining results and the pattern evaluation measures discussed in this chapter, discuss which measure may convincingly uncover close collaboration patterns better than others. **

The Advantage of Null-Invariant Measures (Kulczynski & Cosine): In co-authorship networks, the vast magnitude of author pairs never collaborate at all (resulting in massive true negatives / zero-frequency pairs). Traditional measures like Lift or Confidence are heavily skewed by these unshared zeroes. Conversely, null-invariant measures like Kulczynski and Cosine are completely unaffected by the massive number of author pairs who do not share publications.

Kulczynski vs. Cosine:

Kulczynski is defined as the average conditional probability of participation between two authors. It performs exceptionally well in identifying true collaboration bonds even if one author is exceptionally prolific (publishing with many different people) while the other has a lower overall publication count.

Therefore, Kulczynski (backed by Cosine) is the most convincing measure to uncover close collaboration patterns because it fairly balances joint frequency against individual productivity without being biased by network sparseness.
