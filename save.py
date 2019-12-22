import csv
# comma seperated value

def save_to_file(jobs):
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title, company, location, apply-link"])
  for job in jobs:
    writer.writerow(list(job.values()))