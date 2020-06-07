import mongoengine as me 
import datetime

'''
{
    "sort" : {
        "sort_id": "12",
        "array_id": "1",
        "time_to_sort": "2.34",
        "array_access_count": "1234"
        "date_ran": "12/2/2020 12:54PM"
    }
}
'''
class Sort(me.Document):
    array_id = me.ObjectIdField(required=True)
    time_to_sort = me.FloatField(default=0)
    array_access_count = me.IntField(default=0)
    date_ran = me.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'sortdb',
        'collection': 'sorts'
    }
