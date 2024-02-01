def task_todo(string):
    if '#todo' in string.lower():
        return True
    elif string == '':
        raise Exception('Error empty string!')

    return False
