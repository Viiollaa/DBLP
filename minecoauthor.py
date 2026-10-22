from collections import defaultdict
from itertools import combinations
import pandas as pd


def mine_close_collaborators(txt_path, min_support=5):
  print("Reading co-author transaction file...")

  author_counts = defaultdict(int)
  pair_counts = defaultdict(int)
  total_papers = 0

  # Read coauthors.txt line by line
  with open(txt_path, "r", encoding="utf-8") as f:
    for line in f:
      authors = line.strip().split()
      # Remove duplicates within the same paper if any
      unique_authors = sorted(list(set(authors)))

      if len(unique_authors) < 2:
        continue

      total_papers += 1

      # Count individual author publications
      for author in unique_authors:
        author_counts[author] += 1

      # Count co-author pairs (combinations of 2)
      for a1, a2 in combinations(unique_authors, 2):
        pair_counts[(a1, a2)] += 1

  print("Calculating co-author correlation metrics...")
  results = []
  for (a1, a2), count_ab in pair_counts.items():
    if count_ab < min_support:
      continue

    count_a = author_counts[a1]
    count_b = author_counts[a2]

    # Kulczynski measure
    kulc = 0.5 * ((count_ab / count_a) + (count_ab / count_b))

    # Cosine measure
    cosine = count_ab / (count_a * count_b) ** 0.5

    results.append({
        "Author_A": a1,
        "Author_B": a2,
        "Co_authored_papers": count_ab,
        "Kulczynski": round(kulc, 4),
        "Cosine": round(cosine, 4),
    })

  res_df = pd.DataFrame(results)
  if not res_df.empty:
    res_df.sort_values(by="Kulczynski", ascending=False, inplace=True)
    res_df.to_csv("coauthor_patterns.csv", index=False)
    print("Done! Mining results successfully saved to coauthor_patterns.csv")
  else:
    print("No co-author pairs met the minimum support threshold.")


if __name__ == "__main__":
  mine_close_collaborators("coauthors.txt", min_support=5)