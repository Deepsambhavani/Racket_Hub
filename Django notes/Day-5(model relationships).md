\*\*we already know what are the relationships in db like #one to one

&#x09;						#one to many

&#x09;						#many to many

we won't talk about all the theory part here we will just get into the coding session so let's do that

###### &#x09;**\*the one to many relationship** 

###### &#x09;	example:- reviews of our rackets let's create the model for that

&#x09;-if we want reviews from user we will need login and logout authentication which Django provides us inbuild method which we have to import in models.py so write "from django.contrib.auth.models import User" in top..

&#x09;-create a model class with name and add some fields like one is necessary where the reviews will be stored and it will require foreinkey because it's not our we will receive it from the user so that's why..

&#x09;---with foreign-key we will use method " racket = models.ForeignKey(rackets,on\_delete=models.CASCADE,related\_name="reviews")" on delete is used to delete the reviews if the rackets are delted. casecade helps to do that it's delete method that automatically tells model to delete that and at the and we use it for linking the page and pass the values as simple as we used in url remember....

\--now i want user to only give rating from 1-5 star so i will use the choice function which is already in-build okay so how will we write it?

&#x09;**syntax:-**

RATING\_CHOICES = \[

&#x20;       (1, '⭐'),

&#x20;       (2, '⭐⭐'),

&#x20;       (3, '⭐⭐⭐'),

&#x20;       (4, '⭐⭐⭐⭐'),

&#x20;       (5, '⭐⭐⭐⭐⭐'),

&#x20;   ]

&#x20;   rating = models.PositiveSmallIntegerField(choices=RATING\_CHOICES, default=5)

\--let's breack code rating choice is just a set of tuples and the choice is in build feild we can use is anywhere, but the positivessmallintegerfield is used for very nice purpose cause it uses less memory and runs fast also it is best for small positive values..



##### **\*many to many relasionship** 



###### &#x09;**\*syntax**



**class racket\_type(models.Model):**

&#x20;   **name = models.CharField(max\_length=50)**

&#x20;   **description = models.TextField(max\_length=200, default="")**

&#x20;   **rackets = models.ManyToManyField(rackets, related\_name='types')**

&#x20;   **def \_\_str\_\_(self):**

&#x20;       **return self.name**   





**--this is many to many where we will take the example of multipal types of rackets can be from diffrent brand like heavy\_head,light weight etc...**

**--models.manytomany is used to tell the django that it has relation with the rackets model.... this one is simple**



##### **\*one to one** 

&#x09;**\*syntax**

&#x09;	**class LaserSerial(models.Model):**

&#x20;   **racket = models.OneToOneField(rackets, on\_delete=models.CASCADE, related\_name='serial')**

&#x20;   **serial\_code = models.CharField(max\_length=30, unique=True)**

&#x20;   **warranty\_months = models.PositiveSmallIntegerField(default=12)**



&#x20;   **def \_\_str\_\_(self):**

&#x20;       **return f"Serial: {self.serial\_code} ({self.racket.name})"**

**-- this is special beacuse it has only one relasion with one model or any type**

**-- so as a example we took the serial number of rackets because they are always unique so we store that in racket variable telling them it's one to one relation and other thing is you know delete**

**-- in code unique is used to check if the numnber already exist or not** 

**--simple i know you understand this......**



**@@@@@ now when we have added models so we have to of-course  make-migrations and migrate all this to tell the django..**

**--after making migration let's let's add models to the admin page.**

**\*\*admin page we added class to the admin pages and imported models into it we know how to import models so let's talk about class-**

&#x09;**-by building classes in admin page we have modified the admin panel with this codes see the codes first-**

&#x09;**\*\*syntax**

**class racket\_reviewsInLine(admin.TabularInline):**

&#x20;   **model = racket\_reviews**

&#x20;   **extra = 1**





**class racketsAdmin(admin.ModelAdmin):**

&#x20;   **list\_display = ('name', 'type', 'pricing', 'date\_added')**

&#x20;   **inlines = \[racket\_reviewsInLine]**

&#x20;   

**class racket\_typeAdmin(admin.ModelAdmin):**

&#x20;   **list\_display = ('name', 'description',)**

&#x20;   **filter\_horizontal = ('rackets',)**



**class LaserSerialAdmin(admin.ModelAdmin):**

&#x20;   **list\_display = ('serial\_code', 'racket', 'warranty\_months')**

&#x20;   **search\_fields = ('serial\_code', 'racket\_\_name')**





**admin.site.register(rackets, racketsAdmin)**

**admin.site.register(racket\_type, racket\_typeAdmin)**

**admin.site.register(LaserSerial, LaserSerialAdmin)**



**\_\_\_**

**-first the racket\_reviwes we use this to get the two tables in a single panle like the rackets it's types and it's reviews so we can simply see the both of them together TabularInline is a fucntion for it.. model tales which model to use and extra 1 means to add box to write reviews**

**-secound one is used to do changes in admin panle of racket model where the record is displatyed list\_displayes shows you the record outside without opning the model it-self and the inlines is used to show output of the class**

###### &#x09;**"in simple term tabularline connects both models and inlines make changes into admin and shows us"**

**-the third class is used to do changes in racket type model which first shows name descripon etc and seccond command is filter\_horizonrl is used to display two boxes to help you understand which of the rackets have you choose and which are all rackets..**

**-the last is serriol number field which is used to show warranty of rackets,name and code of it and the search\_fields creates a serach bar at the top of you laserserial page..**

**--then at last you register your model and tell them which model you upgraded at the admin page simple**

**im out sorry if you understand today cause mind is bit off today and tired** 





















&#x20;



