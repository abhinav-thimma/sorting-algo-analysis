import mongoengine

'''
This function initliases the mongo DB connection
'''
def global_init():
    mongoengine.register_connection(alias = 'sortdb', name= 'sort_analysis')