# Django-REST-3
Mixin Concept


Mixins
=====

The mixin classes provide the "actions" methods that are used to provide
the basic view behavior.

Note that the mixin classes proide action methods rather than defining the 
handler methods, such as .list(), .retrieve(), .destroy()....
 
This allows for more flexible composition of behavior.

The mixin classes can be imported    ---- >>> from rest_framework.mixins.


Here we use both handler methods and action methods in class based views to handel corresponding requests like get, post, put and delete.

Example:
=======
            def get(self,request):
                return self.list(request)



   
Mixins_class          purpose         action methods   handler methods
---------          -----------        --------------    --------------

ListModelMixin	   ----	getting all	.list()		        get()	
CreateModelMixin   ----	create one	.create()		post()

RetrieveModelMixin ----	getting one	.retrieve()		get()
UpdateModelMixin   ----	update one	.update()	        put()
DestroyModelMixin  ----	delete one	.destroy()		delete()



1. ListModelMixin:   
==============      

It provides .list(request)  action method,  that list out all available model instances.



2. CreateModelMixin:                
==================   
It provides .create() action method, that allows us to post a new model instance and also it will save the new  model instance.



3. RetrieveModelMixin:            
====================
It provides .retrieve() method, that returns an existing model instance as a response.



4.UpdateModelMixin:           
================== 
It provides .update() method, that allows us to modify the existing model instance, after modifying it also save the model instance.



5. DestroyModelMixin:          
===================          
It provides .destroy() method, that allow us to delete the existing model instance.


different handler methods are,

1. get()
2. post()
3. put()
4. delete()

action & handler methods               Mixin Classes    
===================                   ===================== 
1.   .list()		               ListModelMixin                                              get()

2.  .create()		               CreateModelMixin                                          post()

3.  .retrieve()	                       RetrieveModelMixin                                        get()

4.  .update()	                       UpdateModelMixin                                          put()

5.  .destroy()	                       DestroyModelMixin                                        delete()



Program :-  Create  project with Mixins concept
========     ======  ==========  ==============

folder name:	mixinsfolder

project name:	mixins_pro

app name:	mixins_app

open mixinsfolder in pycharm

crete models.py file code

create  serializers.py file in side application name  with code.

create views.py file code

create project  urls.py code

create application urls.py code


python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

user name:	'your username'
pwd:		'your password'

python manage.py runserver


login to the admin site and enter some product details

open new tab and enter ipaddress along with /api/product

127.0.0.1:8000/api/product

