import sys,os 
from functools import cmp_to_key

def min_by_key(key, records):
    if not records:
        return None

    res = {}
    min_value = float('inf')
    for record in records:
        tmp = record.get(key, 0)
        if tmp < min_value:
            res = record
            min_value = tmp
    return res


def min_by_key_1(key, records):
    return first_by_key(key, "asc", records)

def min_by_key_2(key, records):
    cmp_function = RecordComparator(key, "asc").compare
    records = sorted(records, key=cmp_to_key(cmp_function))
    # # tmp = sorted(records, cmp=cmp_function)
    return records[0]

def first_by_key(key, direction, records):
    if not records:
        return None

    res = {}
    if direction == "asc":
        min_value = float('inf')
        for record in records:
            tmp = record.get(key, 0)
            if tmp < min_value:
                res = record
                min_value = tmp
    else:
        max_value = float('-inf')
        for record in records:
            tmp = record.get(key, 0)
            if tmp > max_value:
                res = record
                max_value = tmp
    return res

def first_by_key_1(key, direction, records):
    tmp = records
    cmp_function = RecordComparator(key, direction).compare
    tmp = sorted(tmp, key=cmp_to_key(cmp_function))
    # # tmp = sorted(records, cmp=cmp_function)
    return tmp[0]

class RecordComparator:
    def __init__(self, key, direction):
        self.key = key
        self.direction = direction
    def compare(self, a, b):
        k = self.key 
        v1 = a.get(k, 0)
        v2 = b.get(k, 0)
        if self.direction == "asc":
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            else:
                return 0
        elif self.direction == "desc":
            if v1 < v2:
                return 1
            elif v1 > v2:
                return -1
            else:
                return 0
        else:
            sys.exit("direction error!")

def first_by_sort_order(sort_orders, records):
    if not records:
        return None
    
    for sort_order in sort_orders:
        cmp_function = RecordComparator(sort_order[0], sort_order[1]).compare
        records = sorted(records, key=cmp_to_key(cmp_function))
        # # records = sorted(records, cmp=cmp_function)
        for i, d in enumerate(records):
            if i == 0:
                v = d.get(sort_order[0], 0)
            else:
                if d.get(sort_order[0], 0) != v:
                    records = records[:i]
                    break
    return records[0]


def test_min_by_key():
    example1 = [{"a": 1, "b": 2}, {"a": 2}]
    example2 = [example1[1], example1[0]]
    example3 = [{}]
    example4 = [{"a": -1}, {"b": -1}]
    assert min_by_key("a", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 1, "b": 2}
    assert min_by_key("a", [{"a": 2}, {"a": 1, "b": 2}]) == {"a": 1, "b": 2}
    assert min_by_key("b", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 2}
    assert min_by_key("a", [{}]) == {}
    assert min_by_key("b", [{"a": -1}, {"b": -1}]) == {"b": -1}

def test_min_by_key_1():
    example1 = [{"a": 1, "b": 2}, {"a": 2}]
    example2 = [example1[1], example1[0]]
    example3 = [{}]
    example4 = [{"a": -1}, {"b": -1}]
    assert min_by_key_1("a", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 1, "b": 2}
    assert min_by_key_1("a", [{"a": 2}, {"a": 1, "b": 2}]) == {"a": 1, "b": 2}
    assert min_by_key_1("b", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 2}
    assert min_by_key_1("a", [{}]) == {}
    assert min_by_key_1("b", [{"a": -1}, {"b": -1}]) == {"b": -1}

def test_min_by_key_2():
    example1 = [{"a": 1, "b": 2}, {"a": 2}]
    example2 = [example1[1], example1[0]]
    example3 = [{}]
    example4 = [{"a": -1}, {"b": -1}]
    assert min_by_key_2("a", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 1, "b": 2}
    assert min_by_key_2("a", [{"a": 2}, {"a": 1, "b": 2}]) == {"a": 1, "b": 2}
    assert min_by_key_2("b", [{"a": 1, "b": 2}, {"a": 2}]) == {"a": 2}
    assert min_by_key_2("a", [{}]) == {}
    assert min_by_key_2("b", [{"a": -1}, {"b": -1}]) == {"b": -1}

def test_first_by_key():
    example1 = [{"a": 1}]
    example2 = [{"b": 1}, {"b": -2}, {"a": 10}]
    example3 = [{}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]
    assert first_by_key("a", "asc", [{"a": 1}]) == {"a": 1}
    assert first_by_key("a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [{"b": 1}, {"b": -2}]
    assert first_by_key("a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
    assert first_by_key("b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
    assert first_by_key("b", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": 1}
    assert first_by_key("a", "desc", [{}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]) == {"a": 10, "b": -10}

def test_first_by_key_1():
    example1 = [{"a": 1}]
    example2 = [{"b": 1}, {"b": -2}, {"a": 10}]
    example3 = [{}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]
    assert first_by_key_1("a", "asc", [{"a": 1}]) == {"a": 1}
    assert first_by_key_1("a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [{"b": 1}, {"b": -2}]
    assert first_by_key_1("a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
    assert first_by_key_1("b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
    assert first_by_key_1("b", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": 1}
    assert first_by_key_1("a", "desc", [{}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]) == {"a": 10, "b": -10}

def test_record_comparator():
    cmp = RecordComparator("a", "asc")
    assert cmp.compare({"a": 1}, {"a": 2}) == -1
    assert cmp.compare({"a": 2}, {"a": 1}) == 1
    assert cmp.compare({"a": 1}, {"a": 1}) == 0

def test_first_by_sort_order():
    assert(first_by_sort_order([("a", "desc")], [{"a": 5}, {"a": 6}])) == {"a": 6}
    assert(first_by_sort_order([("b", "asc"), ("a", "desc")], [{"a": -5, "b": 10}, {"a": -4, "b": 10}])) == {"a": -4, "b": 10}
    assert(first_by_sort_order([("a", "asc"), ("b", "asc")], [{"a": -5, "b": 10}, {"a": -4, "b": 10}])) == {"a": -5, "b": 10}
    assert(first_by_sort_order([], [])) is None
    assert(first_by_sort_order([], [{"a": 5}, {"a": 6}])) == {"a": 5}

def main(argv):
    test_min_by_key()
    test_min_by_key_1()
    test_min_by_key_2()
    test_first_by_key()
    test_first_by_key_1()
    test_record_comparator()
    test_first_by_sort_order()
    return 0

if __name__ == '__main__':   
    main(sys.argv)
    







