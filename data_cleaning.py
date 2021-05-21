def parse_i2b2(annotations, documents, base_string = 'clinical-'):
    a_ids = []
    e_ids = []

    # Use regex to create doc id

    for con in a_corpus:
        f_id = re.findall(r'\d+', con)[0]
        a_ids.append(f_id)
    for doc in e_corpus:
        f_id = re.findall(r'\d+', doc)[0]
        e_ids.append(f_id)

    a_ids = tuple(sorted(a_ids))
    e_ids = tuple(sorted(e_ids))

    intersection = list(set(a_ids) & set(e_ids))
    if len(intersection) == len(a_ids):
        print("Count of concept files with corresponding doc:", len(intersection))
    else:
        print("Count of concept files does not correspond to count of docs")

