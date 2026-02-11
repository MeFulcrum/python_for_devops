class class1:
    def process(self):
        return "processed data"

class class2:
    pass


def process_data(obj):
    if hasattr(obj, 'process') and callable(getattr(obj, 'process')):
        return obj.process()
    return None



def process_data1(obj):
    try:
        return obj.process()
    except AttributeError:
        return None
    

    