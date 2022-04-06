from django.shortcuts import render

def example_view(request):
    return render(request, 'my_app/example.html')

def variable_view(request):
    my_var = {
        'first_name':'Rosalind',
        'last_name':'Frankland',
        'some_list': [1,2,3],
        'some_dict': {
            'inside_key_1':'inside_value_1',
            'inside_key_2':'inside_value_2',
            'inside_key_3':'inside_value_3',
            },
        'user_logged_in':True,
    }
    return render(request, 'my_app/variable.html', context=my_var)