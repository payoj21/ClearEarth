from collections import defaultdict
import codecs
def confusion_matrix(evaluate_script, entity_list):
    """
    Given a matrix of test examples and labels, compute the confusion
    matrixfor the current classifier.  Should return a dictionary of
    dictionaries where d[ii][jj] is the number of times an example
    with true label ii was labeled as jj.

    :param test_x: Test data representation
    :param test_y: Test data answers
    """

    # Finish this function to build a dictionary with the
    # mislabeled examples.  You'll need to call the classify
    # function for each example.



    d = defaultdict(dict)
    data_index = 0

    # for xx, yy in zip(test_x, test_y):
    #     data_index += 1
    #     output_y = self.classify(xx)
    #     if output_y in d[yy]:
    #         d[yy][output_y] += 1
    #     else:
    #         d[yy][output_y] = 1
    #     if debug and data_index % 100 == 0:
    #         print("%i/%i for confusion matrix" % (data_index, len(test_x)))
    # return d

    f = codecs.open(evaluate_script, 'r', encoding= 'utf-8')
    for ent1 in entity_list:
        for ent2 in entity_list:
            d[ent1][ent2] = 0
    for line in f:
        if line != '\n':

            line = line.strip('\n')
            content = line.split('\t')
            # print(content)
            gold = content[1].lower()
            prediction = content[2].lower()
            print gold , prediction
            # print(gold +'\t\t'+ prediction)

            # if gold in d:
            #     if prediction in d[gold]:
            #         d[gold][prediction] += 1
            #     else:
            #         d[gold][prediction] = 1
            # else:
            #     d[gold] = {prediction: 1}

            if prediction in d[gold]:
                d[gold][prediction] += 1
            else:
                d[gold][prediction] = 1

    # confusion = knn.confusion_matrix(data.test_x, data.test_y)


    print("\t" + "\t".join(x[:3] for x in entity_list))
    print("".join(["-"] * 90))
    for ii in entity_list:
        print("%s:\t" % ii[:3] + "\t".join(str(d[ii].get(x, 0))
                                       for x in entity_list))



# entity_files = ["data/geo/entity_types.txt","data/bio/entity_types.txt","data/sea_ice/entity_types.txt"]
# evaluate_script_files = ["data/geo/evaluate_script.txt","data/bio/evaluate_script.txt","data/sea_ice/evaluate_script.txt"]

entity_files = ["data/bio/entity_types.txt"]
evaluate_script_files = ["data/bio/evaluate_script.txt"]
for i, filename in enumerate(entity_files):
    f = codecs.open(filename, 'r', encoding = 'utf-8')
    print(filename[filename.find('/'):filename.find('/entity')].upper())
    entity = []
    for line in f:
        entity.append(line.strip('\n').lower())

    evaluate_script = evaluate_script_files[i]
    confusion_matrix(evaluate_script,entity)





