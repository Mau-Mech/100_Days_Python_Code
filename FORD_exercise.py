def process_data(obj):
    if hasattr(obj, 'process'):
        if callable(getattr(obj,'process')):
            return obj.process()
    else:
        return None
        
class MyClass :
    pass

def function_int():
    raise Exception("This will be handled in get_result not in process_data")

def function_str():
    return "function_str"

def get_result(queries):
    res = [] 
    obj = MyClass()
    for x in queries:
        print(x)
        if x == 1 :
            setattr(obj, "process", 1)
        if x == 2 :
            setattr(obj, "process", function_str)
        if x == 3 :
            setattr(obj, "process", function_int)
        if x == 4 and process_data(obj) != None:
            delattr(obj, "process")
        if x == 3:
            try:
                process_data(obj)
            except:
                res.append("1")
            delattr(obj, "process")
        else:
            res.append(str(process_data(obj)))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = get_result(queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()