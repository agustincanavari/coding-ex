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
        last_updated_opportunity = None

        for opportunity_id in opportunities.keys():
            if opportunities[opportunity_id]['company_id'] == company_id:
                opportunity_amount += 1
                opportunity_sum += opportunities[opportunity_id]['amount']
                if opportunities[opportunity_id]['updated_at'] > last_updated_opportunity:
                    last_updated_opportunity = opportunities[opportunity_id]['updated_at']

        rows.append([name, start_date, opportunity_amount, opportunity_sum/opportunity_amount, last_updated_opportunity])

    return rows


def main():
    # part 1
    local_companies, _ = urllib.request.urlretrieve("https://pbryan.github.io/exercise/companies.csv", "")
    local_opportunities, _ = urllib.request.urlretrieve("https://pbryan.github.io/exercise/opportunities.csv", "")

    companies = open(local_companies, 'r')
    opportunities = open(local_opportunities, 'r')

    json_companies = open('companies_json', 'w')
    json_opportunities = open('opportunities_json', 'w')

    companies_reader = csv.DictReader(companies, ['id', 'name', 'start_date', 'logo_image_url', 'employees', 'target_account', '_row_'])
    opportunities_reader = csv.DictReader(opportunities, ['id', 'company_id', 'amount', 'type', 'updated_at', 'status', '_row_'])

    for row in companies_reader:
        json.dump(row, json_companies)
        json_companies.write('\n')

    for row in opportunities_reader:
        json.dump(row, json_opportunities)
        json_opportunities.write('\n')

    companies.close()
    opportunities.close()
    json_companies.close()
    json_opportunities.close()

    # part 2
    companies = {}
    opportunities = {}

    with open(json_companies) as companies_file:
        for jsonObj in companies_file:
            companies[jsonObj['id']] = {
                'name': jsonObj['name'],
                'start_date': jsonObj['start_date'],
                'logo_image_url': jsonObj['logo_image_url'],
                'employees': jsonObj['employees'],
                'target_account': jsonObj['target_account']
            }

    with open(json_opportunities) as opportunities_file:
        for jsonObj in opportunities_file:
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
    report = open('company_report.csv')
    writer = csv.writer(report)
    writer.writerow(report_headers)
    for row in report_rows:
        writer.writerow(row)


if __name__ == "__main__":
    main()
