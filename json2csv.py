import json, csv

def json2csv(json_file, csv_file):
    with open(json_file, "r") as file1:
        data = json.load(file1)
        with open(csv_file, "w") as file2:
            csv_writer = csv.writer(file2)
            count = 0
            for item in data:
                if count == 0:
                    header = item.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(item.values())
            print(f"Converted {json_file} to {csv_file}")

if __name__ == "__main__":
    json_file = "data/starred_users_kataras_iris.json"
    csv_file = "data/starred_users_kataras_iris.csv"
    json2csv(json_file, csv_file)