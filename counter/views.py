from django.shortcuts import render
# G1lpGkcs/uXRmxaRh3EgYA==5lVtfrGAlPj7ymIL
# Create your views here.
def home(request):
    import json
    import requests
    if request.method=='POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = request.get (api_url + query, headers = {'X-Api-Key':'G1lpGkcs/uXRmxaRh3EgYA==5lVtfrGAlPj7ymIL' })
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api="oops! There was an error"
            print(e)
        return render(request, 'home.html',{'api':api})
    else:
        return render(request, 'home.html')
    
