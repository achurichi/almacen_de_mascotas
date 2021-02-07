from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Q
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.forms import modelformset_factory

from .models import Product, ProductImg
from .forms import ProductForm, ProductImgForm


def products_list(request):
    query = ""
    if request.GET:
        query = request.GET['q']
    
    ImgFormset = modelformset_factory(ProductImg,
                                      form=ProductImgForm,
                                      extra=1,)

    if request.method == "POST":
        productForm = ProductForm(request.POST)
        imgFormset = ImgFormset(request.POST,
                                request.FILES,
                                queryset=ProductImg.objects.none())

        if productForm.is_valid():
            savedProduct = productForm.save()

            if request.FILES != {} and imgFormset.is_valid():
                for form in imgFormset.cleaned_data:
                    if form != {}:
                        photo = ProductImg(
                            product=savedProduct, image=form['image'])
                        photo.save()

        return HttpResponseRedirect(reverse('sales:products_list'))
    else:
        productForm = ProductForm()
        imgFormset = ImgFormset(queryset=ProductImg.objects.none())

    products = Product.objects.filter(
        Q(product_id__icontains=query) |
        Q(description__icontains=query)).distinct().order_by('-created_at')

    product_img_list = []
    noImgObject = ProductImg(image='images/no-image-found.jpg')
    for product in products:
        productImg = ProductImg.objects.filter(product=product).first()
        if productImg:
            product_img_list.append(productImg)
        else:
            product_img_list.append(noImgObject)
        
    print(product_img_list)

    paginator = Paginator(products, 15)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    productForm = ProductForm()
    context = {
        'query': str(query),
        'products': products,
        'productForm': productForm,
        'imgFormset': imgFormset,
        'productsWithImg': zip(products, product_img_list),
    }

    return render(request, 'sales/products_list.html', context)


def delete_product(request):
    product_db_id = request.POST.get('product_db_id', None)
    Product.objects.filter(id=product_db_id).delete()
    return JsonResponse({})


def show_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    productImg = ProductImg.objects.filter(
        product=product)
    context = {
        'product': product,
        'productImg': productImg,
    }
    return render(request, 'sales/show_product.html', context)


def edit_product(request, pk):
    ImgFormset = modelformset_factory(ProductImg,
                                      form=ProductImgForm,
                                      extra=1,
                                      can_delete=True,)

    if request.method == "POST":
        product = get_object_or_404(Product, id=pk)
        productForm = ProductForm(request.POST, instance=product)
        imgFormset = ImgFormset(request.POST,
                                request.FILES,
                                queryset=ProductImg.objects.filter(
                                    product_id=pk))
        if productForm.has_changed() and productForm.is_valid():
            productForm.save()

        if imgFormset.is_valid():
            for form in imgFormset.cleaned_data:
                if form == {} or form['id'] == None and form['DELETE'] == True:
                    continue
                else:
                    if form['id'] == None:
                        photo = ProductImg(
                            product=product, image=form['image'])
                        photo.save()
                    elif form['DELETE'] == True:
                        ProductImg.objects.filter(
                            id=form['id'].pk).delete()
                    else:
                        photo = ProductImg.objects.filter(
                            id=form['id'].pk)[0]
                        if photo.image != form['image']:
                            photo.image = form['image']
                            photo.save()

        url = reverse('sales:show_product', kwargs={'pk': pk})
        return HttpResponseRedirect(url)

    product = get_object_or_404(Product, id=pk)
    productForm = ProductForm(instance=product)
    imgFormset = ImgFormset(queryset=ProductImg.objects.filter(
        product_id=pk))

    context = {
        'product': product,
        'productForm': productForm,
        'imgFormset': imgFormset,
    }

    return render(request, 'sales/edit_product.html', context)
