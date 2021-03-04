import csv

def save_to_file(arti): 
  file = open("arti.csv", mode = "w")
  writer = csv.writer(file)
  writer.writerow(["제목", "주소", "날짜"])
  for article in arti:
    writer.writerow(list(article.values()))
  return 