import csv


def get_info(entities_list):
    list_result = []
    source_name = None
    date_entity = None
    month_entity = None
    hour_entity = None
    hour_entity_1 = None

    for entity in entities_list:
        for key, value in entity.items():
            if key == "entity" and value == "mã_chứng_khoán":
                source_name = entity["value"]
            if key == "entity" and value == "ngày":
                date_entity = int(entity['value'])
            if key == "entity" and value == "tháng":
                month_entity = int(entity['value'])
            if key == "entity" and value == "giờ":
                hour_entity = int(entity['value'])
            if key == "entity" and value == "giờ_1":
                hour_entity_1 = int(entity['value'])

    abc="mã chứng khoán/"+source_name+".csv"
    print(abc)

    with open(str(abc)) as csvfile:
        reader = csv.DictReader(csvfile)

        # date/month/hour-hour
        if source_name and date_entity and month_entity and hour_entity and hour_entity_1:
            print("hello")
            for row in reader:
                # split date data
                date_raw = row['Date']
                date_space = date_raw.split()
                date_nospace = date_space[0]
                date_split = date_nospace.split("/")
                date_check = list(map(int,date_split))
                # split time data
                time_full_form = date_space[1]
                time_split =time_full_form.split(":")
                hour_check = int(time_split[0])
                minute_check = int(time_split[1])
                if date_check[0] == date_entity and date_check[1] == month_entity and hour_check >= hour_entity and hour_check <= hour_entity_1 :
                    # print(row["Date"], row["Open"], row['High'], row['Low'], row['Close'], row['Volume'])
                    row_dict = dict(row)
                    row_dict["Hour"] = hour_check
                    row_dict["Minute"] = minute_check
                    list_result.append(row_dict)
                    # print(list_result)
            if list_result != []:
                return list_result
            else:
                list_result = None
                return list_result
        #date/month/hour
        elif source_name and date_entity and month_entity and hour_entity:
            for row in reader:
                # split date data
                date_raw = row['Date']
                date_space = date_raw.split()
                date_nospace = date_space[0]
                date_split = date_nospace.split("/")
                date_check = list(map(int,date_split))
                # split time data
                time_full_form = date_space[1]
                time_split =time_full_form.split(":")
                hour_check = int(time_split[0])
                minute_check = int(time_split[1])
                if date_check[0] == date_entity and date_check[1] == month_entity and hour_check == hour_entity :
                    # print(row["Date"], row["Open"], row['High'], row['Low'], row['Close'], row['Volume'])
                    row_dict = dict(row)
                    list_result.append(row_dict)
                    # print(list_result)
            if list_result != []:
                return list_result[len(list_result)-1]
            else:
                list_result = None
                return list_result
        #date/month
        elif source_name and date_entity and month_entity :
            for row in reader:
                # split date data
                date_raw = row['Date']
                date_space = date_raw.split()
                date_nospace = date_space[0]
                date_split = date_nospace.split("/")
                date_check = list(map(int,date_split))
                # split time data
                time_full_form = date_space[1]
                time_split =time_full_form.split(":")
                hour_check = int(time_split[0])
                minute_check = int(time_split[1])
                if date_check[0] == date_entity and date_check[1] == month_entity :
                    # print(row["Date"], row["Open"], row['High'], row['Low'], row['Close'], row['Volume'])
                    row_dict = dict(row)
                    list_result.append(row_dict)
                    # print(list_result)
            if list_result != []:
                return list_result[len(list_result)-1]
            else:
                list_result = None
                return list_result
