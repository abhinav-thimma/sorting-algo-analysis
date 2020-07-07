import mongoengine as me 

'''
{
    "array": {
        "array_id": "1",
        "arrays": [
            [3,2,4],
            [1,2,3]
        ],
        "array_type": "sorted"
    }
}
'''
class Array(me.Document):
    array_list = me.ListField(required=True)
    array_type = me.StringField(required=True)

    meta = {
        'db_alias': 'sortdb',
        'collection': 'arrays'
    }

    def __str__(self):
        return f"array_type = {self.array_type} array_list = {self.array_list}"
    