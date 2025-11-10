from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.models import User

from .forms import LoginForm,RegisterForm,CommentForm,EditAccountForm,EditProfileUserForm
from django.shortcuts import render, redirect
from .models import Category, Dish, Comment,ProfileUser


# Create your views here.

def main_page(request):
    category = Category.objects.all()
    dishes = Dish.objects.all().order_by('-created_at')
    context={
        'title':'Food-Journey — готовь, вдохновляйся, наслаждайся!',
        'categories':category,
        'dishes':dishes
    }
    return render(request,'food_journey/index.html',context)

def food_by_category(request,pk):
    dishes = Dish.objects.filter(cuisine=pk)
    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    context={
        'title':f'Food-Journey {category.title}',
        'dishes':dishes,
        'categories': categories,
    }
    return render(request,'food_journey/index.html',context)


def food_detail(request,pk):
    food = Dish.objects.get(pk=pk)
    category = Category.objects.all()
    same_foods = Dish.objects.filter(cuisine=food.cuisine)
    context = {
        'food': food,
        'form':CommentForm(),
        'title':f'FoodProject {food.name_of_the_dish}',
        'categories': category,
        'comments':Comment.objects.filter(food=food),
        'same_dishes':same_foods.exclude(pk=food.pk).distinct().order_by('-created_at')
    }
    return render(request,'food_journey/food_detail.html',context)

def login_user_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method =='POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if user:
                    login(request, user)
                    return redirect('main')
        else:
            form = LoginForm()
        context = {
            'title': 'Авторизация',
            'form':form
        }
        return render(request,'food_journey/login.html',context)
def logout_user_view(request):
    logout(request)
    return redirect('main')

def register_user_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            form = RegisterForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                profile = ProfileUser.objects.create(user=user)
                profile.save()
                return redirect('login')
        else:
            form = RegisterForm()
    context = {
        'title':'Регистрация',
        'form':form
    }
    return render(request,'food_journey/register.html',context)

def search_game(request):
    category = Category.objects.all()
    word = request.GET.get('q')
    if word:
        dishes = Dish.objects.filter(name_of_the_dish__icontains=word).order_by('-created_at')
    else:
        dishes = Dish.objects.all().order_by('-created_at')

    context = {
        'categories': category,
        'dishes': dishes,
        'search_word': word,
    }
    return render(request, 'food_journey/index.html', context)

def about_site(request):
    return render(request, 'food_journey/about.html')

def save_comment(request,pk):
    if request.user.is_authenticated:
        try:
            food = Dish.objects.get(pk=pk)
            if request.method=='POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.author=request.user
                    comment.food = food
                    comment.save()
                return redirect('detail',food.pk)
        except:
            return redirect('main')
    else:
        return redirect('login')
def profile_user(request,pk):
    if request.user.is_authenticated:
        try:
            profile = ProfileUser.objects.get(user=pk)
            context = {
                'title':f'Профиль {profile.user.username}',
                'profile':profile,
                'account_form':EditAccountForm(instance=request.user),
                'profile_form':EditProfileUserForm(instance=request.user.profileuser)
            }
            return render(request,'food_journey/profile.html',context)
        except:
            return redirect('main')
    else:
        return redirect('main')

def edit_account_profile(request):
    if request.user.is_authenticated and request.method == 'POST':
        account_form = EditAccountForm(request.POST,instance=request.user)
        profile_form = EditProfileUserForm(request.POST,request.FILES,instance=request.user.profileuser)
        if account_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            account_form.save()
            data = account_form.cleaned_data
            user = User.objects.get(pk=request.user.pk)
            if user.check_password(data['old_password']):
                if data['old_password'] != data['new_password'] and data['new_password'] == data['new_password2']:
                    user.set_password(data['new_password'])
                    user.save()
                    update_session_auth_hash(request,user)
            return redirect('profile',user.pk)
    else:
        return redirect('login')



