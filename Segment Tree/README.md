# Segment Tree Implementation in C++

 C++ implementation of a Segment Tree, a data structure commonly used for handling range queries and updates efficiently.

## Overview

A Segment Tree is a versatile data structure used primarily for handling range queries and updates on arrays or lists. It allows for fast queries such as finding the minimum, maximum, sum, etc., of elements within a given range, as well as efficient updates of individual elements.

This implementation provides a basic structure for a Segment Tree along with methods for building the tree, updating values, and querying ranges.

## Features

- **Efficient Range Queries**: Supports fast queries for the minimum value within a given range.
- **Update Operations**: Allows updating individual elements efficiently.
- **Flexibility**: Can be extended to support other range query operations like maximum, sum, etc.

## Functions

### `build(std::vector<long long>& v)`

This function builds the segment tree from the given array `v`. It takes the array `v`, its size, and recursively constructs the tree by dividing the array into segments and merging them.

### `set(int idx, long long value)`

This function updates the value of the element at index `idx` to the specified `value`. It recursively updates the affected segments of the tree to maintain its integrity.

### `getRange(int l, int r)`

This function queries the segment tree to find the minimum value within the range `[l, r)`. It traverses the tree to locate the relevant segments and returns the minimum value found within the specified range.

## Example

Consider an array `[1, 3, 2, 7, 9, 11]`. We can build a segment tree from this array and perform various operations:

1. Build the segment tree from the array.
2. Query the minimum value in the range `[1, 4]`.
3. Update the value at index 2 to 5.
4. Query the minimum value again in the updated range `[1, 4]`.

The example code demonstrates these operations and showcases the functionality of the segment tree implementation.
