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
    trueTime = 0
    prevLine = ""
                                        # [1724786135, 1, 0, 0,...] is the array, and the first value is the seconds and
                                            #second value is the hall effect. so array[0] = 1724786135 and array[1] = 1

    content = file.readline()                 #reads the first line of the txt file and reads it as a continuous string
    count += 1                           #this is the line number
    print("count: ", count)
    prevLine = content
    elements = content.split(',')        #splits the line of text by commas just read and puts it into an array
                                            # "[1724786135, 1, 0, 0,...]
    r_time = elements[0]                 #this is the first second of the file we are ignoring for calcuations.
    for line in file:                   #this is loops through every line in the file



        while skip_loop:                        #this whole loop checks to see if the next second is equal to the one we should skip.
            prevLine = content
            elements = content.split(',')             # iF it is, we keep reading until its not the second we are skipping.

            curr_time = elements[0]
            print("curr time: ", curr_time)
            content = file.readline()
            count += 1
            print("count: ", count)
            prevLine = content
            elements = content.split(',')
            curr_time = elements[0]
            if r_time == curr_time:
                content = file.readline()
                count += 1
                print("count: ", count)
                prevLine = content
                elements = content.split(',')
                curr_time = elements[0]
            else:
                skip_loop = 0

        for j in range(0, 500):                 #The data is formatted so that it gives is in milliseconds,
                                                # so this is our way of checking to see
                                                # what millisecond we are on.
            prevLine = content
            elements = content.split(',')

            print(elements[0])
            if len(elements[0]) == 0:
                print("End of Data")
                break                       #this checks to see if we ran through all lines of data.
            timestamp = elements[0]
            hall_data = elements[1]
            print("Time Recorded: ", timestamp)
            #print("Halleffect Recorded: ", hall_data)
            timestamp_value = float(timestamp)
            #print("J value: ", j)
            trueTime = j / 500 + timestamp_value
            print("Time: ", trueTime)
            hall_data = int(hall_data)
            if hall_data:
                if prev_time != 0 and trueTime != 0:                        #this calculates our rpm.
                    rpm = 60 / (trueTime - prev_time) * (1 / teeth_num)
                    print("RPM: ", rpm)
                prev_time = trueTime
            if j < 500:
                content = file.readline()
                count += 1
                print("count: ", count)
            else:
                break
        prevLine = elements
        # if prev_time != 0:
        #     elements = content.split(',')
        #     print(elements[0])
        #     if len(elements[0]) == 0:
        #         print("End of Data")
        #         break  # this checks to see if we ran through all lines of data.
        #     timestamp = elements[0]
        #     hall_data = elements[1]
        #     print("Time Recorded: ", timestamp)
        #     # print("Halleffect Recorded: ", hall_data)
        #     timestamp_value = float(timestamp)
        #     # print("J value: ", j)
        #     trueTime = timestamp_value + 0.999
        #     print("Time: ", trueTime)
        #     hall_data = int(hall_data)
        #     if hall_data:
        #         if prev_time != 0 and trueTime != 0 and prev_time != trueTime:  # this calculates our rpm.
        #             rpm = 60 / (trueTime - prev_time) * (1 / teeth_num)
        #             print("RPM: ", rpm)
        #         prev_time = trueTime

        count += 1