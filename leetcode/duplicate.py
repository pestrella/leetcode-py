def find_dups(coll):
    uniques = set()
    dups = set()
    for i in coll:
        if i in uniques:
            dups.add(i)

        uniques.add(i)

    return list(dups)
