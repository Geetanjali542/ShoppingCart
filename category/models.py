from django.db import models

# Create your models here.
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)  #these are the category
    slug = models.SlugField(max_length=100, unique=True)     #The slug field, represented as models.SlugField in Django models, is used to store a URL-friendly version of a text-based field, such as a title. a slug only stores char, number, hyphen and underscores.
    description = models.CharField(max_length=250, blank=True)
    cat_image = models.ImageField(upload_to="photos/categories")


# verbose_name_plural doesn't got change even after migrating
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'catgories' # this is done so that the name mentioned as table name is visible to us according to us otherwise it just adds s to the name we have given but with this help it does not do accordingly to built in feature.
    
    def get_url(self):
        return reverse('products_by_category', args = [self.slug])   
    # prodcuts_by_category is the name of the url "category/<slug:category_slug>/" and views fun name is store we are using the url by name for redirecting purpose and for the saving the path of the url travelled 
    

    def __str__(self):
        return self.category_name
# it is used to give name to the objects created on the categorys table instead of categorys object(1), categorys object(2)


# This overrides the default name of the objects of this class, it's something like Categorys :object which isn't very helpful.

# overriding it gives a more human friendly name of the object like the Categorys
# .name


