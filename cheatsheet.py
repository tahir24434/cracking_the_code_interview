#!/usr/bin/python

# *********************************************************************
# Ordered Sequence: fast index access, repeatable values. list, tuple
# *********************************************************************

# ========================== lists ==========================
empty_list = []                                       # Creation
my_list = ["x", 11, 8.9, 11]                          # Creation
print "%s, %d" % (my_list[0], my_list[1])             # Access
lowest_index = my_list.index(11)                      # returns the lowest index in list that obj appears.
print "lowest_index = %d" % lowest_index

# *** Returns new list
sliced_list = my_list[1:3]                            # Slicing (returns 11, 8.9)
print "sliced_list = %s" % sliced_list
sliced_list1 = my_list[0:-1]                          # Slicing (returns "x", 11, 8.9)
print "sliced_list1 = %s" % sliced_list1
concatenated_list = my_list + [5, 3, 9]               # Concatenation
print "concatenated_list = %s" % concatenated_list
repetitive_list = my_list * 2                         # Repetition
print "repetitive_list = %s" % repetitive_list
comprehend_list = [items*2 for items in my_list]      # List comprehension: Provides a compact way of mapping a list
                                                      # into another list by applying a function to each of the
                                                      # elements of the list
print "comprehend_list = %s" % comprehend_list

# *** Modify original list
my_list.append(4)                                     # Add object at end. list.append(obj)
print "my_list(appended) = %s" % my_list
my_list.append([6,5])
print "my_list(appended) = %s" % my_list
my_list.extend([1,2])                                 # appends contents of seq to list at end. list.extend(seq)
print "my_list(extended) = %s" % my_list
my_list.insert(1, "y")                                # Inserts object obj into list at offset index. list.insert(index, obj)
print "my_list(inserted) = %s" % my_list
my_list.remove(11)                                    # Remove first occurrence of object from list. list.remove(obj)
print "my_list(removed) = %s" % my_list
my_list.remove([6,5])
print "my_list(removed) = %s" % my_list
my_list.pop(0)                                        # remove & return item at index idx (default last)
my_list.pop(0)
print "my_list(popped) = %s" % my_list
my_list.reverse()                                     # Reverse list in place
print "my_list(reversed) = %s" % my_list
my_list.sort()                                        # Sort list in place
print "my_list(sorted) = %s" % my_list

# *** Generic Sequence operations. https://docs.python.org/2/library/functions.html
list_len = len(my_list)                               # Length of list
list_min = min(my_list)                               # Minimum value of list
list_max = max(my_list)                               # Maximum valued of list
list_sum = sum(my_list)                               # Sum of the values of list
exist = 8.9 in my_list                                # Membership
print "length=%d, min=%d, max=%d, sum=%d, exist=%s" % (list_len, list_min, list_max, list_sum, exist)

# *** Iterate over list
for items in my_list:
    print items

# *** APPLICATIONS
my_stack = []
my_stack.append(object)  # push
object = my_stack.pop()  # pop from end
my_queue = []
my_queue.append(object)   # push
object = my_queue.pop(0)  # pop from beginning

# *** Performance notes
# http://effbot.org/zone/python-list.htm#performance

# ========================== Tuples ==========================
print "******************************** Tuples *********************************"
empty_tup = ()                              # Create
tup = (50, )
print "tuppel = %s" % tup[0]                # Access

# *** Returns new tuple (Tuples are im-mutable)
tup1 = (20, )                                       # Adding new value using concatenation
my_tup = tup + tup1
print "my_tup = %s" % (my_tup, )

sliced_tup = my_tup[0:1]                            # Slicing (returns 11, 8.9)
print "sliced_tup = %s" % sliced_tup
sliced_tup1 = my_tup[0:-1]                          # Slicing (returns "x", 11, 8.9)
print "sliced_tup1 = %s" % sliced_tup1
concatenated_tup = my_tup + (5, 3, 9)               # Concatenation
print "concatenated_tup = %s" % (concatenated_tup, )
repetitive_tup = tup * 2                            # Repetition
print "repetitive_tup = %s " % (repetitive_tup, )

del my_tup                                          # Delete whole tuple.

# ========================== SETs ==========================
print "******************************** SETs *********************************"
engineers = {"Tahir", "Hassan"}
coders = {"Tahir", "Hassan", "John"}
set_len = len(engineers)
exists = 'Tahir' in engineers
is_subset = engineers <= coders
is_proper_subset = engineers <= coders                  # set <= other and set != other
print "set_len = %s, exists = %s, is_subset = %s, is_proper_subset = %s" % (set_len, exists, is_subset, is_proper_subset)
union_set = engineers.union(coders)
print "union_set = %s" % union_set
intersection_set = engineers.intersection(coders)
print "intersection_set = %s" % intersection_set
difference = coders - engineers
print "difference = %s" % difference
engineers.add("Bashir")
print "engineers = %s" % engineers
symmetric_difference = engineers ^ coders # Return a new set with elements in either the set or other but not both
print "symmetric_difference = %s" % symmetric_difference
engineers.remove("Bashir")
print "engineers = %s" % engineers




# ***********************************************************************
#  key containers, no a priori order, fast key acces, each key is unique
# ***********************************************************************

# ========================== Dictionaries ==========================
print "******************************** Dictionaries *********************************"
# Rules: No duplicate keys. Keys must be immutable. No Restriction on values.
empty_dict = {}                                         # Creation
my_dict = {'name':"Tahi", 'age':30}
print my_dict['name']                                   # Access
my_keys = my_dict.keys()                                # list of keys (iterable view)
print "my_keys = %s" % my_keys
my_values = my_dict.values()                            # list of values (iterable view)
print "my_values = %s" % my_values
my_associations = my_dict.items()                       # returns a list of dict's (key, value) tuple pairs
print "my_associations = %s" % my_associations
my_dict['name'] = "Tahir"                               # Update existing item
print "updated dictionary = %s" % my_dict
my_dict['extra'] = "fazool"                             # Add new item
print my_dict
del my_dict["extra"]                                    # Remove
print my_dict

dict2 = {'height': 5.6}
my_dict.update(dict2)                                   # adds dictionary dict2's key-values pairs in to dict
get_height = my_dict.get('height')                      # dict.get(key, default=None). Returns a value for the given key
                                                        # If key is not available then returns default value None
get_weight = my_dict.get('weight', 65)
print "get_height = %s, get_weight %s" % (get_height, get_weight)
pop_height = my_dict.pop('height')                       # If key is in the dictionary, remove it and return its value,
                                                        # else return default
print "pop_height %s" % pop_height
pop_weight = my_dict.pop('weight', 65)
print "pop_height = %s, pop_weight = %s" % (pop_height, pop_weight)

pop_tuple = my_dict.popitem()                                       # Remove and return an arbitrary (key, value) pair as 2-tuple.
print "pop_tuple = %s" % (pop_tuple,)


var = 100
if var > 50:
   print "1 - Got a true expression value"
   print var
elif var > 60:
   print "2 - Got a true expression value"
   print var






