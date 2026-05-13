import openpyxl

def save_excel(data):
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(["Company", "Info"])

    for item in data:
        ws.append([
            item.get("company", ""),
            item.get("info", "")
        ])

    file_name = "results.xlsx"
    wb.save(file_name)

    return file_name
