import sys
import os

file_path = r"d:\Documents\Web Sites\Tales From Wall Street\talesfromwallstreet\excerpt.html"

from part1 import text1
from part2 import text2
from part3 import text3
from part4 import text4

new_content = text1 + "\n" + text2 + "\n" + text3 + "\n" + text4

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "<h2>The Wall Street Fast Lane</h2>"
end_marker = '<div style="text-align: center; margin-top: 2rem;">'

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)
    
    # ensure new_content paragraphs are properly indented
    new_lines = new_content.splitlines()
    indented_new_content = "\n".join(["            " + line if line.strip() else "" for line in new_lines]).strip()
    
    new_file_content = content[:start_idx] + "\n\n            " + indented_new_content + "\n\n            " + content[end_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_file_content)
    print("Replaced successfully")
else:
    print("Markers not found")
