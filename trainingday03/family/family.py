def rel(f, i):
    res = []
    if i in f.keys():
        res.append(f[i])
    elif i in f.values():
        for k in f.keys():
            if f[k] == i:
                res.append(k)
    return res


def are_related(father_d, mother_d, first, second):
    families = [[first], [second]]


print(rel({'John': 'Jack', 'Jack': 'Jim', 'minh': 'Jack'}, 'Jack'))
print(are_related({'John': 'Jack', 'Jack': 'Jim', 'minh': 'Jack'}, {'Jim': 'El'}, 'John', 'El'))

    #
    # """Find out if `first` and `second` are related.
    #
    # `father_d` is a dict where for each key, the associated
    # value is the father of key.
    #
    # For example, if 'John' is the father of 'Nathalie', then
    # we would have father_d['Nathalie'] == 'John'
    #
    # `mother_d` is a dict where for each key, the associated
    # value is the mother of key.
    #
    # For example, if 'Martha' is the mother of 'Nathalie', then
    # we would have mother_d['Nathalie'] == 'Martha'
    #
    # >>> are_related({'John': 'Jack'}, {}, 'John', 'Jack')
    # True
    # >>> are_related({'John': 'Jack'}, {'Al': 'El'}, 'John', 'El')
    # False
    # >>> are_related({'John': 'Jack', 'Jack': 'Jim'}, {'Jim': 'El'}, 'John', 'El')
    # True
    # """
