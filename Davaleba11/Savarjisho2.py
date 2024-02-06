

first_tuple = (1,1,2,3,4,4,5,6)

second_tuple = (4,5,5,6,6,7)





def add_tuples(tuple1, tuple2):

    combined_tuple =()
    dublicate_tuple =()

    for i in range(len(tuple1)):
        if tuple1[i] in tuple2:
            if tuple1[i] not in combined_tuple:
                combined_tuple = combined_tuple + (tuple1[i],)
                dublicate_tuple = dublicate_tuple + (tuple1[i],)
        elif tuple1[i] not in combined_tuple:
            combined_tuple = combined_tuple + (tuple1[i],)
    
    for i in range(len(tuple2)):
        if tuple2[i] not in combined_tuple:
            combined_tuple = combined_tuple + (tuple2[i],)

    print(combined_tuple)
    print(dublicate_tuple)



add_tuples(first_tuple, second_tuple)


    