import mongoengine

def global_init():
    mongoengine.register_connection(alias = 'sortdb', name= 'sort_analysis')