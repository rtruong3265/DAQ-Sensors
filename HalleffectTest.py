text_file = '27-8-2024 19_15_33.txt'
with open(text_file, 'r') as file:
    k = 0
    skip_loop = 1
    prev_time = 0
    rpm = 0
    teeth_num = 20
    curr_time = 0
    r_time = 0
    hall_data = 0
    count = 0
    end_waffle = 1

    content = file.readline()
    count += 1
    print("count: ", count)

    elements = content.split(',')
    r_time = elements[0]
    if len(elements[0]) == 0:
        print("No more data")

    else:
        while skip_loop:
            elements = content.split(',')
            curr_time = elements[0]
            print("curr time: ", curr_time)
            content = file.readline()
            count += 1
            print("count: ", count)

            elements = content.split(',')
            curr_time = elements[0]
            if r_time == curr_time:
                content = file.readline()
                count += 1
                print("count: ", count)

                elements = content.split(',')
                curr_time = elements[0]
            else:
                skip_loop = 0

        for j in range(0, 1000):


            elements = content.split(',')

            print(elements[0])
            if len(elements[0]) == 0:
                print("End of Data")
                end_waffle = 0
                break
            timestamp = elements[0]
            hall_data = elements[1]
            print("Time Recorded: ", timestamp)
            #print("Halleffect Recorded: ", hall_data)
            timestamp_value = float(timestamp)
            #print("J value: ", j)
            trueTime = j / 1000 + timestamp_value
            print("Time: ", trueTime)
            hall_data = int(hall_data)
            if hall_data:
                if prev_time != 0 and trueTime != 0:
                    rpm = 60 / (trueTime - prev_time) * (1 / teeth_num)
                    print("RPM: ", rpm)
                prev_time = trueTime
            if j < 1000:
                content = file.readline()
                count += 1
                print("count: ", count)
        count += 1