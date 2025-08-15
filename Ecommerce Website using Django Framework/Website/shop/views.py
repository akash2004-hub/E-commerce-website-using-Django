from django.shortcuts import render
from django.http import HttpResponse
from .product import Product
from .category import Category
from django.contrib.auth.views import LoginView

def home(request):
    category_id = request.GET.get('category')

    if category_id:
        try:
            products = Product.get_products_by_category(category_id)
        except:
            products = Product.objects.all()  # fallback if invalid ID
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    data = {
        'products': products,
        'categories': categories
    }
    return render(request, 'index.html', data)


def cart_view(request):
    
    return render(request, 'cart.html')


def signup_view(request):
    return render(request, 'signup.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'


def signup_view(request):
    if request.method == 'GET':
        
        return render(request, 'signup.html')

    elif request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        userdata=[first_name,last_name,phone,email,password]
        print(userdata)

         # Validation
        error_message = None
        if not first_name:
            error_message = "First name is required"
        elif not last_name:
            error_message = "Last name is required"
        elif not phone:
            error_message = "Phone number is required"
        elif not email:
            error_message = "Email is required"
        elif not password or len(password) < 6:
            error_message = "Password must be at least 6 characters"
        elif Customer.objects.filter(email=email).exists():
            error_message = "Email already registered"

        return HttpResponse("text message: we are reciving the data")


def custom_login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:  # POST request
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Try to find user with matching email
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email is not registered. Please sign up first.")
            return render(request, 'login.html')

        # Now authenticate using the username linked to that email
        user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # or wherever you want to redirect after login
        else:
            messages.error(request, "Invalid password. Please try again.")
            return render(request, 'login.html')
