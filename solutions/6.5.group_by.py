from typing import Callable, Iterable, Any, List, Dict


def group_by(func: Callable[[Any], Any], iterable: Iterable[Any]) -> Dict[Any, List[Any]]:
    """
        Groups elements in the `iterable` by the result of applying `func` to each element.

       Args:
           func: A function that takes an element from the `iterable` as input and returns a key to group by.
           iterable: An iterable containing the elements to group.

       Returns:
           A dictionary where the keys are the results of applying `func` to the elements in `iterable`
           and the values are lists of elements from `iterable` that correspond to each key.
    """
    grouped_by_func_dic = {}
    for element in iterable:
        key = func(element)
        if key in grouped_by_func_dic:
            grouped_by_func_dic[key] +=[element]
        else:
            grouped_by_func_dic[key] = [element]
    return grouped_by_func_dic


def main():
    # example to split group of numbers by even, not even, using group_by func.
    numbers = [i for i in range(200)]
    groups = group_by(lambda number: number % 2 == 0, numbers)
    print("grouped by function result:")
    for key, value in groups.items():
        print(value)


if __name__ == "__main__":
    main()
