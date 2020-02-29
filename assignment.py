
# GLOBAL VARIABLES
elements = ["1", "s", "t", "t^2", "st", "ts", "st^2", "t^2s", "tst", "sts", "tst^2", "t^2st"]
cayley = {
    "1": {"1": "1", "s":"s", "t":"t", "t^2":"t^2", "st":"st", "ts":"ts", "st^2":"st^2", "t^2s":"t^2s", "tst":"tst", "sts":"sts", "tst^2":"tst^2", "t^2st":"t^st"}, 
    "s": {"1":"s", "s":"1", "t":"st", "t^2":"st^2", "st":"t", "ts":"t^2", "st^2":"t^2", "t^2s":"tst", "tst":"t^2s", "sts":"ts", "tst^2":"t^2st", "t^2st":"tst^2"}, 
    "t": {"1":"t", "s":"ts", "t":"t^2", "t^2":"1", "st":"tst", "ts":"t^2s", "st^2":"tst^2", "t^2s":"s", "tst":"t^2st", "sts":"st^2", "tst^2":"sts", "t^2st":"st"}, 
    "t^2": {"1":"t^2", "s":"t^2s", "t":"1", "t^2":"t", "st":"t^2st", "ts":"s", "st^2":"sts", "t^2s":"ts", "tst":"st", "sts":"tst^2", "tst^2":"st^2", "t^2st":"tst"},
    "st": {"1":"st", "s":"sts", "t":"st^2", "t^2":"s", "st":"t^2s", "ts":"tst", "st^2":"t^2st", "t^2s":"1", "tst":"tst^2", "sts":"t^2", "tst^2":"ts", "t^2st":"t"},
    "ts": {"1":"ts", "s":"t", "t":"tst", "t^2":"tst^2", "st":"t^2", "ts":"st^2", "st^2":"1", "t^2s":"t^2st", "tst":"s", "sts":"t^2s", "tst^2":"st", "t^2st":"sts"},
    "st^2": {"1":"st^2", "s":"tst", "t":"s", "t^2":"st", "st":"tst^2", "ts":"1", "st^2":"ts", "t^2s":"sts", "tst":"t", "sts":"t^2st", "tst^2":"t^2", "t^2st":"t^2s"},
    "t^2s": {"1":"t^2s", "s":"t^2", "t":"t^2st", "t^2":"sts", "st":"1", "ts":"tst^2", "st^2":"t", "t^2s":"st", "tst":"ts", "sts":"s", "tst^2":"tst", "t^2st":"st^2"},
    "tst": {"1":"tst", "s":"st^2", "t":"tst^2", "t^2":"ts", "st":"s", "ts":"t^2st", "st^2":"st", "t^2s":"t", "tst":"sts", "sts":"1", "tst^2":"t^2s", "t^2st":"t^2"},
    "sts": {"1":"sts", "s":"st", "t":"t^2s", "t^2":"t^2st", "st":"st^2", "ts":"t^2", "st^2":"s", "t^2s":"tst^2", "tst":"1", "sts":"tst", "tst^2":"t", "t^2st":"ts"},
    "tst^2": {"1":"tst^2", "s":"t^2st", "t":"ts", "t^2":"tst", "st":"sts", "ts":"t", "st^2":"t^2s", "t^2s":"st^2", "tst":"t^2", "sts":"st", "tst^2":"1", "t^2st":"s"},
    "t^2st": {"1":"t^2st", "s":"tst^2", "t":"sts", "t^2":"t^2s", "st":"ts", "ts":"st", "st^2":"tst", "t^2s":"t^2", "tst":"st^2", "sts":"t", "tst^2":"s", "t^2st":"1"}
}

# COMPUTATIONS
def return_product(elem1, elem2):
    return cayley[elem1][elem2]

def left_coset(element, set1):
    new_set = []
    for elem in set1:
        new_set.append(cayley[element][elem])
    return new_set

def right_coset(element, set1):
    new_set = []
    for elem in set1:
        new_set.append(cayley[elem][element])
    return new_set