```
1. PascalCase
		* for classes
2. camelCase
		* never write in python
3. kebab-case
		* may be for project names
4. snake_case
		* recommended for variables, functions, methods
```

Collections in Python

Python provides different collection types to store multiple values in a single variable. The four commonly used collections are List, Set, Tuple, and Dictionary (Dict).

### List = [] ordered and changeable. Duplicates Allowed

### Set = {} unordered and immutable, but Add/Remove Possible. No duplicates

### Tuple = () ordered and unchangeable. Duplicates Possible. Faster than lists

### Dict = { "key": "value" }. Ordered and changable. keys must be unique and unchangeable

## List

A List is an ordered collection of items. It can be modified after creation, and duplicate values are allowed.

fruits = ["Apple", "Banana", "Apple"]

## Set

A Set is a collection of unique items. Duplicate values are automatically removed, and items cannot be accessed using an index.

fruits = {"Apple", "Banana", "Mango"}

## Tuple

A Tuple is an ordered collection similar to a List, but it cannot be modified after creation.

fruits = ("Apple", "Banana", "Mango")
Dictionary (Dict)

A Dictionary stores information as key-value pairs. Each key is unique and is used to access its corresponding value.

```
person = {
	"name": "John",
	"age": 25
}

```
