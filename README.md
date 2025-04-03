# Python Linked List Class

This structure covers the main aspects of linked list implementation

**## Short methods description**
1. **`__str__`**
	- Returns a string representation of the list in the format: `value1 -> value2 -> value3`. If the list is empty, returns `"Empty List"`.

2. **`__iter__(return_node: bool = False)`**
	- Returns an iterator to traverse the list. If `return_node=True`, returns **Node** objects, otherwise returns the node values.

3. **`__len__`**
	- Returns the length of the list.

4. **`clear()`**
	- Clears the list by removing all elements.

5. **`add(value) -> bool`**
	- Adds an element to the end of the list. Returns `True` upon successful addition.

6. **`pop() -> Optional[Any]`**
	- Removes and returns the last element of the list. If the list is empty, returns `None`.

7. **`delete_by_first_appeared_value(value) -> bool`**
	- Removes the first element found with the specified value. Returns `True` if the element is found and removed, otherwise `False`.

8. **`search_by_index(index, return_node=False) -> Node | Any`**
	- Returns the element by index. If `return_node=True`, returns the **Node** object, otherwise returns the node value.

9. **`insert_at_index(index: int, value) -> bool`**
	- Inserts an element with the specified value at the given index. Returns `True` upon successful insertion.

10. **`delete_by_index(index) -> bool`**
	- Removes the element by index. Returns `True` if the element is successfully removed, otherwise raises an **IndexError**.

11. **`to_list() -> List[Any]`**
	- Converts the list to a Python **List** and returns it.

12. **`reverse()`**
	- Reverses the list, creating a new list with elements in reverse order.

13. **`contains(value) -> bool`**
	- Checks if the list contains an element with the specified value. Returns `True` or `False`.

14. **`index_of(value) -> int`**
	- Returns the index of the first element found with the specified value. If the element is not found, returns `None`.

15. **`is_empty() -> bool`**
	- Checks if the list is empty. Returns `True` if the list is empty, otherwise `False`.

16. **`extend(values: List[Any]) -> None`**
	- Adds elements from the given **List** to the end of the current list.

17. **`count(value) -> int`**
	- Returns the number of occurrences of an element with the specified value in the list.

18. **`reverse_in_place()`**
	- Reverses the list in place, changing the order of elements without creating a new list.

19. **`copy() -> LinkedList`**
	- Creates and returns a copy of the current list.

20. **`merge(list: LinkedList) -> None`**
	- Merges the current list with another **LinkedList** object. Raises a **TypeError** if the passed object is not an instance of **LinkedList**.

21. **`delete_all_occurances_by_value(value) -> None`**
	- Removes all elements with the specified value from the list.

## **Usage**

```Python
from linked_list import LinkedList

# Create a new linked list
ll = LinkedList()

# Add elements
ll.add(10)
ll.add(20)
ll.add(30)

# Print the list
print(ll)

# Get the length of the list
print(len(ll))

# Check if the list contains a value
print(ll.contains(20))

# Remove an element by value
ll.delete_by_first_appeared_value(20)

# Convert to a Python list
print(ll.to_list())

# Reverse the list
ll.reverse()

# Print the reversed list
print(ll)
```

## **To run the tests, execute from the folowing command**
```
python -m unittest discover tests
```
