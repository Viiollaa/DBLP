import re

print("Starting fast line-by-line streaming extraction...")

input_file = "dblp.xml"
output_file = "coauthors.txt"

count = 0
in_record = False
current_authors = []

# Regex to find author tags and clean any entities inside them
author_pattern = re.compile(r"<author[^>]*>(.*?)</author>", re.IGNORECASE)

try:
  with open(input_file, "r", encoding="utf-8", errors="ignore") as f_in, open(
      output_file, "w", encoding="utf-8"
  ) as f_out:

    for line in f_in:
      # Detect start of a paper record
      if "<article" in line or "<inproceedings" in line:
        in_record = True
        current_authors = []

      # If inside a record, extract authors
      if in_record:
        matches = author_pattern.findall(line)
        for author in matches:
          # Strip any lingering entity codes safely
          clean_author = re.sub(r"&[^;\s]+;", "", author).strip()
          if clean_author:
            current_authors.append(clean_author)

      # Detect end of a paper record
      if "</article>" in line or "</inproceedings>" in line:
        if in_record and len(current_authors) > 1:
          f_out.write(" ".join(current_authors) + "\n")
          count += 1

          if count % 50000 == 0:
            print(f"Successfully processed {count} coauthor transactions...")

        in_record = False
        current_authors = []

  print(
      f"Done! Successfully saved {count} coauthor transactions to {output_file}."
  )

except Exception as e:
  print(f"An error occurred: {e}")