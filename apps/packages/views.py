from django.shortcuts import render, redirect
from .models import Category, Classification, Product
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# definimos el inicio
def home(request):
    return render(request, 'home.html')

# definimos el quien soy.
def about (request):
    return render(request, 'about.html')

# listamos todos las categorias
@login_required
def category_list (request):
    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }
    return render(request, 'packages/category_list.html', context)

# creamos todos las categorias
@login_required
def category_create(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
                return redirect('category_list')
            except:
                messages(request, 'Hay un error en los datos suministrados')
    else:
        form = CreateCategoryForm()    
    return render(request, 'packages/category_create.html', {"form":form})

# modificamos las categorias se requiere id
@login_required
def category_update(request, id):
    categories = Category.objects.get(pk = id)
    form = UpdateCategoryForm(instance = categories)
    if request.method == "POST":
        form = UpdateCategoryForm(request.POST, request.FILES, instance = categories)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria Editada Correctamente")
            return redirect('category_list')
    context = {'form':form}
    return render(request, 'packages/category_update.html', context)

# Eliminamos una categoria con el id seleccionado, solo informare que se elimino
@login_required
def category_delete(request, id):
    categories = Category.objects.get(pk = id)
    categories.delete()
    return render(request, 'packages/category_delete.html')


# listamos todos las clasificaciones
@login_required
def classification_list (request):
    classifications = Classification.objects.order_by('name')
    context = {
        'classifications': classifications,
    }
    return render(request, 'packages/classification_list.html', context)

# creamos las categorias
@login_required
def classification_create(request):
    if request.method == 'POST':
        form = CreateClassificationForm(request.POST, request.FILES )
        if form.is_valid:
            try:
                form.save()
                return redirect('classification_list')
            except:
                messages(request, 'Hay un error en los datos suministrados')
    else:
        form = CreateClassificationForm()    
    return render(request, 'packages/classification_create.html', {"form":form})

# modificamos las clasificaciones
@login_required
def classification_update(request, id):
    classifications = Classification.objects.get(pk = id)
    form = UpdateClassificationForm(instance = classifications)
    if request.method == "POST":
        form = UpdateClassificationForm(request.POST, request.FILES, instance = classifications)
        if form.is_valid():
            form.save()
            messages.success(request, "Classificacion Editada Correctamente")
            return redirect('classification_list')
    context = {'form':form}
    return render(request, 'packages/classification_update.html', context)

# Eliminamos una clase con el id seleccionado, solo informare que se elimino
@login_required
def classification_delete(request, id):
    classifications = Classification.objects.get(pk = id)
    classifications.delete()
    return render(request, 'packages/classification_delete.html')


# Listamos todos los productos sin filtro de FK, asociado al crud de producto
@login_required
def product_list(request):
    products = Product.objects.order_by('-title')
    page_num = request.GET.get("page")
    paginator = Paginator(products, 2)
    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)        
    context = {
        'products': products,
    }
    return render(request, 'packages/product_list.html', context)

# Buscamos un producto segun su id.
@login_required
def product_read(request, id):
    products = Product.objects.get(pk = id)
    context = {'products': products}
    return render(request, 'packages/product_read.html', context)

# Creamos un producto con el modelo creado en forms.py
@login_required
def product_create(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES )
        if form.is_valid:
            try:
                form.save()
                messages.success(request, "Producto Cargado Correctamente")
                return redirect('product_list')
            except:
                messages(request, 'Hay un error en los datos suministrados')
    else:
        form = CreateProductForm()    
    return render(request, 'packages/product_create.html', {"form":form})

# Editamos producto se requiere el id (al igual que en la urls)
@login_required
def product_update(request, id):
    products = Product.objects.get(pk = id)
    form = UpdateProductForm(instance = products)
    if request.method == "POST":
        form = UpdateProductForm(request.POST, request.FILES, instance = products)
        if form.is_valid():
            img_last = Product.objects.filter(image=products)
            if len(img_last) > 0:
                img_last[0].delete()
            form.save()
            messages.success(request, "Producto Editado Correctamente")
            return redirect('product_list')
    context = {'form':form}
    return render(request, 'packages/product_update.html', context)

# Eliminamos producto se requiere el id (al igual que en la urls)
@login_required
def product_delete(request, id):
    products = Product.objects.get(pk = id)
    if request.method == 'POST':
        products.delete()
        return redirect('product_list')
    context = {'products': products}
    return render(request, 'packages/product_delete.html', context)

# Busqueda de producto atravez de un requerimiento
@login_required
def product_search(request):
    if request.method == 'POST':
        searching = request.POST['searching']
        products = Product.objects.filter(title__icontains=searching) 
        return render(request, 'packages\product_search.html', {'query':searching, 'products':products})
    else:
        print("Lo sentimos, no hay resultados para su búsqueda")
        return render(request, 'packages\product_search.html',{})

# Busqueda de producto por categoria (Destino)    
@login_required
def product_category(request):
    category = request.GET.get('category')
    if category == None:
        products = Product.objects.order_by('-title')
        page_num = request.GET.get("page")
        paginator = Paginator(products, 2)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)             
    else:
        products = Product.objects.filter(category__name=category)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'packages\product_show.html', context)    

# Busqueda de producto por clasificacion (Tipo de vacacion)  
@login_required
def product_classification(request):
    classification = request.GET.get('classification')
    if classification == None:
        products = Product.objects.order_by('-title')
        page_num = request.GET.get("page")
        paginator = Paginator(products, 2)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)             
    else:
        products = Product.objects.filter(classification__name=classification)
    classifications = Classification.objects.all()
    context = {
        'products': products,
        'classifications': classifications
    }
    return render(request, 'packages\product_show.html', context)  