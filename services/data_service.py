from data.array import Array
from data.sort import Sort
from data.sort_time import SortTime

'''
Creates an Array entity and stores in DB
'''
def create_array(array_list, array_type):
    array = Array()
    array.array_list = array_list
    array.array_type = array_type
    array.save()

    return array

'''
Creates a Sort entity and stores in DB
''' 
def create_sort(array: Array, time_to_sort, array_access_count):
    sort = Sort()
    sort.time_to_sort = time_to_sort
    sort.array_access_count = array_access_count
    sort.array_id = array.id

    sort.save()
    return sort

'''
Creates an SortTime entity and stores in DB
'''
def create_sort_time(name, sorts):
    sorttime = SortTime()
    sorttime.name = name
    sorttime.sorts = [sort.id for sort in sorts]

    sorttime.save()
    return sorttime

'''
Fetch Arrays using array_type
'''
def fetch_arrays_using_type(array_type):
    return Array.objects(array_type = array_type)

'''
Fetch SortTime using name
'''
def fetch_sorttime_using_name(name):
    return SortTime.objects(name = name)

'''
Fetch Sort using id
'''
def fetch_sort(id):
    return Sort.objects(id = id)