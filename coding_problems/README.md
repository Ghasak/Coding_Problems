# Collecting Several programming puzzles
Here i have collected several coding puzzles and ideas that I found them interesting.

## C1- Find the smallest integer not in a list.
If the data structure can be mutated in place and supports random access then you can do it in O(N) time and O(1) additional space. Just go through the array sequentially and for every index write the value at the index to the index specified by value, recursively placing any value at that location to its place and throwing away values > N. Then go again through the array looking for the spot where value doesn't match the index - that's the smallest value not in the array. This results in at most 3N comparisons and only uses a few values worth of temporary space.

```py
def smallest_missing_uint64(source_list):
    the_answer = None

    target = 0L
    while target < 2L**64:

        target_found = False
        for item in source_list:
            if item == target:
                target_found = True

        if not target_found and the_answer is None:
            the_answer = target

        target += 1L

    return the_answer
```
