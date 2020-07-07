import mongoengine as me 
import datetime
from .array import Array 

'''
{
    "sort" : {
        "sort_id": "12",
        "array": "Array reference",
        "time_to_sort": "2.34",
        "array_access_count": "1234"
        "date_ran": "12/2/2020 12:54PM"
    }
}
'''
class Sort(me.Document):
    array = me.ReferenceField(Array)
    time_to_sort = me.FloatField(default=0)
    array_access_count = me.IntField(default=0)
    date_ran = me.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'sortdb',
        'collection': 'sorts'
    }

    def __str__(self):
        return f"array_id = {self.array} time_to_sort = {self.time_to_sort} array_access_count = {self.array_access_count}"
