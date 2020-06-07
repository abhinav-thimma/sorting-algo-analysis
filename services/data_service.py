from data.array import Array
from data.sort import Sort
from data.sort_time import SortTime

def create_array(array_list, array_type):
    array = Array()
    array.array_list = array_list
    array.array_type = array_type
    array.save()

    return array
    
def create_sort(array: Array, time_to_sort, array_access_count):
    sort = Sort()
    sort.time_to_sort = time_to_sort
    sort.array_access_count = array_access_count
    sort.array_id = array.id

    sort.save()
    return sort

def create_sort_time(name, sorts):
    sorttime = SortTime()
    sorttime.name = name
    sorttime.sorts = [sort.id for sort in sorts]

    sorttime.save()
    return sorttime