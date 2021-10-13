import urllib.request
import csv
import json


def get_company_report_rows(companies, opportunities):
    rows = []
    for company_id in companies.keys():
        name = companies[company_id]['name']
        start_date = companies[company_id]['start_date']

        opportunity_amount = 0
        opportunity_sum = 0
        last_updated_opportunity = "1900-12-15T05:11:12Z"

        for opportunity_id in opportunities.keys():
            if opportunities[opportunity_id]['company_id'] == company_id:
                opportunity_amount += 1
                opportunity_sum += float(opportunities[opportunity_id]['amount'])
                if opportunities[opportunity_id]['updated_at'] > last_updated_opportunity:
                    last_updated_opportunity = opportunities[opportunity_id]['updated_at']

        rows.append([name, start_date, opportunity_amount, opportunity_sum/opportunity_amount, last_updated_opportunity])

    return rows

def process_csv_as_json(csv_url, file_name):
    csv_file, _ = urllib.request.urlretrieve(csv_url, "")
    
    with open(csv_file, 'r') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        with open(file_name, 'w') as json_file_handler:
            for row in csv_reader:
                json.dump(row, json_file_handler)
                json_file_handler.write('\n')


def main():
    # part 1
    process_csv_as_json("https://pbryan.github.io/exercise/companies.csv", "companies_json")
    process_csv_as_json("https://pbryan.github.io/exercise/opportunities.csv", "opportunities_json")

    # part 2
    companies = {}
    opportunities = {}

    with open("companies_json") as companies_file:
        for jsonStr in companies_file:
            jsonObj = json.loads(jsonStr)
            companies[jsonObj['id']] = {
                'name': jsonObj['name'],
                'start_date': jsonObj['start_date'],
                'logo_image_url': jsonObj['logo_image_url'],
                'employees': jsonObj['employees'],
                'target_account': jsonObj['target_account']
            }

    with open("opportunities_json") as opportunities_file:
        for jsonStr in opportunities_file:
            jsonObj = json.loads(jsonStr)
            opportunities[jsonObj['id']] = {
                'company_id': jsonObj['company_id'],
                'amount': jsonObj['amount'],
                'type': jsonObj['type'],
                'updated_at': jsonObj['updated_at'],
                'status': jsonObj['status']
            }

    # part 3
    # company report

    report_headers = ['company name', 'start date', 'opportunities', 'average opportunity amount', 'last update']
    report_rows = get_company_report_rows(companies, opportunities)
    with open('company_report.csv', 'w') as report:
        writer = csv.writer(report)
        writer.writerow(report_headers)
        for row in report_rows:
            writer.writerow(row)


if __name__ == "__main__":
    main()
