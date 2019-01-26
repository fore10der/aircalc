from django.shortcuts import render
 
def index(request):
    block1_title= "title"
   
    # block2_table = [ { 'Customer' :  1, 'F/H' : 11, 'NURn' :  111, 'NFn' : 1111, 'NR' : 11111},{ 'Customer' :  2, 'F/H' : 22, 'NURn' :  222, 'NFn' : 2222, 'NR' : 22222}, { 'Customer' :  3, 'F/H' : 33, 'NURn' :  333, 'NFn' : 3333, 'NR' : 33333},{ 'Customer' :  4, 'F/H' : 44, 'NURn' :  444, 'NFn' : 4444, 'NR' : 44444}]
    # ???   a list of dictionaries => error
    
    block2_table = { 'Customer' :  1, 'F/H' : 11, 'NURn' :  111, 'NFn' : 1111, 'NR' : 11111}

    block3_image = "image"

   # data = YourModel.objects.all()

    data = {
        "block1_title": block1_title,
        "block2_table": block2_table,
        "block3_image": block3_image
    }

    return render(request, "report.html", context=data)

    