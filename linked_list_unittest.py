import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def set_list_up(self, length: int = 10):
        self.linked_list.clear()
        self.create_list(length)

    def create_list(self, length):
        for i in range(1, length + 1):
            self.linked_list.add(value=i)

    def test_add(self):
        self.set_list_up()

        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10")
    
    def test_pop(self):
        self.set_list_up()

        self.linked_list.pop()
        self.linked_list.pop()
        self.linked_list.pop()

        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7")
        
    def test_delete_by_first_appeared_value(self):
        self.set_list_up()

        self.linked_list.delete_by_first_appeared_value(1)
        self.linked_list.delete_by_first_appeared_value(10)
        self.linked_list.delete_by_first_appeared_value(5)

        self.assertEqual(str(self.linked_list), "2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9")

    def test_len(self):
        self.set_list_up()

        self.assertEqual(len(self.linked_list), 10)

    def test_search_by_index(self):
        self.set_list_up()

        self.assertEqual(self.linked_list.search_by_index(0), 1)
        self.assertEqual(self.linked_list.search_by_index(5), 6)
        self.assertEqual(self.linked_list.search_by_index(9), 10)
    
    def test_insert_at_index(self):
        self.set_list_up()

        self.linked_list.insert_at_index(index=0, value=41)
        self.linked_list.insert_at_index(index=len(self.linked_list), value=42)
        self.linked_list.insert_at_index(index=5, value=43)

        self.assertEqual(str(self.linked_list), "41 -> 1 -> 2 -> 3 -> 4 -> 43 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 42")
        with self.assertRaises(IndexError):
            self.linked_list.insert_at_index(index=42, value=42)

    def test_to_list(self):
        self.set_list_up()
        self.assertEqual(self.linked_list.to_list(), [1,2,3,4,5,6,7,8,9,10])

    def test_reverse(self):
        self.set_list_up()
        self.linked_list.reverse()

        self.assertEqual(str(self.linked_list), "10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1")

    def test_reverse_in_place(self):
        self.set_list_up()

        self.linked_list.reverse_in_place()

        self.assertEqual(str(self.linked_list), "10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1")
    
    def test_contains(self):
        self.set_list_up()

        self.assertFalse(self.linked_list.contains(42))
        self.assertFalse(self.linked_list.contains(0))
        self.assertTrue(self.linked_list.contains(10))
        self.assertTrue(self.linked_list.contains(1))
        self.assertTrue(self.linked_list.contains(7))

    def test_index_of(self):
        self.set_list_up()

        self.assertEqual(self.linked_list.index_of(1), 0)
        self.assertEqual(self.linked_list.index_of(10), 9)
        self.assertEqual(self.linked_list.index_of(5), 4)
        self.assertIsNone(self.linked_list.index_of(42))

    def test_is_empty(self):
        self.set_list_up(length=0)

        self.assertTrue(self.linked_list.is_empty())

    def test_merge(self):
        self.set_list_up()

        new_ll = LinkedList()
        new_ll.add(1)
        new_ll.add(2)
        new_ll.add(3)

        self.linked_list.merge(list=new_ll)

        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 1 -> 2 -> 3")
    
    def test_extend(self):
        self.set_list_up()

        array = [1,2,3]
        self.linked_list.extend(values=array)

        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 1 -> 2 -> 3")
    
    def test_copy(self):
        self.set_list_up()

        ll_copy = self.linked_list.copy()

        self.assertEqual(str(ll_copy), str(self.linked_list))
    
    def test_delete_all_occurances_by_value(self):
        self.set_list_up()

        self.linked_list.add(5)
        self.linked_list.add(5)
        self.linked_list.add(5)

        self.linked_list.delete_all_occurances_by_value(5)

        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 10")

    

if __name__=="__main__":
    unittest.main()