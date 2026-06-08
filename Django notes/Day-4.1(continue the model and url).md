hey there today the project is running properly.. it's a good thing

&#x20;--today we will learn how to display your data into the field...

&#x09;-for that first you have to create a function in views.py in your created app after that you have to import your model in it

&#x09;- when you import your model you have to fetch data from db using method like create any variable then store the query in it write down your model name which you wrote like i wrote racket "racket.objects.all()" then you return the variable from return with any variable you want just like flask when you transfer the data by storing in one variable 

&#x09;-- make sure you create you varible name a bit different then the model name because the python will get consfused...

&#x09;

&#x20; \*\*now lets print data into the front page open the front page then run a for loop inside your contact block you have to write 

&#x09;			{%for racket in rackets%} racket is new variable and the rackets is which you retrieved from the views

so now you write the div or any tage inside your for loop

&#x09;	-inside that tage write the tag and for source you use {{}} which is used to print the variable as example you want to fetch image so you write "<img src="{{racket.image.url}}" >" racket is where you stored the data and image is varible name from the db where you stored your values url is only used in image cause Django saves the images as url and data both.....

\-- if you want name or somthing like that write {{racket.name}

\-- and you give the class of tailwind and make styles of your choices

\--just for the practice added two more fields like price and descriptions and showed them into the web page loved it to see that i my self can do something now.. 

\-- added button to the card and now i want it to **redirect** to buy page let's work on it

\--first you have to create view and import **"from django.shortcuts import get\_object\_or\_404"**

&#x09;	after you import write function like this 

**def buy\_racket(request, racket\_id):**

&#x20;   **racket = get\_object\_or\_404(rackets, pk= racket\_id)**

&#x20;   **return render(request, 'DBL/buy.html', {'racket': racket})**

*in this i made just typo which was very good cause i know where i make mistakes in simple words you are passing you id as parameter which id dajango give automaticly then you run a method of get object or error which passes the data and you are also pasing the id with it as a primary key means it's unique then you know the process... this works when you write in url but lets do it while clicking button..*

*--when you created view you have to give it a path  "path('<int:racket\_id>/', views.buy\_racket, name='buy'),"   why int racket cause it shows the id of the racket in the url..*

*--now when the path is done just add the link in anchor tag in the dbl page to redirect just write "<a href="{% url 'buy' racket.id %}">" url is simpley a name which we gave in url like above it makes it easy to redirect... done*



