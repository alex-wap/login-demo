from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  print "GET index"
  # check if error messages
    # put in context
    # clear them out of session
  # else, context messages are empty
  context={'messages':[]}
  return render(request,'login/index.html',context)

def register(request):
  print "POST register"
  # if check request.method
    # make call to model method register
    # store in messages variable
    # if messages empty
      # print "no messages, success"
      # assign session id and first
      # return redirect('/success')
    # else, assign session messages
  return redirect('/')

def login(request):
  print "POST register"
  # if check request.method
    # make call to model method login
    # if messages empty
      # print "no messages, success"
      # fetch user id and first via email
      # assign session id and first
      # return redirect('/success')
    # else, assign session messages
  return redirect('/')

def success(request):
  print "GET success"
  return render(request,'login/success.html')

def logout(request):
  print "POST logout"
  # delete session keys
  return redirect('/')