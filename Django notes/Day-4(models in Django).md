hey there

&#x09;--you can also change your password from terminal if you forgot just type "python manage.py changepassword username"

Knew for the day:-

&#x09;-for making model go to your app and open models.py

&#x09;   -now you have to create class and in that class call models.model as parameter then you have to add field of data

&#x09;\*\*\* main thing always us extenstions without that there will be so many small errors like one latter capital and small mistake...

&#x09;-- now you add fields you want in your basic model if you want to add images so you have to install one package which is pillow run command "python -m pip install Pillow" (P capital needed)

&#x09;\*\*To use media file you have to add path in settings.py but in your main app just write:-

&#x09;			#for media files

&#x09;				"MEDIA\_URL = '/media/'

&#x09;				MEDIA\_ROOT = os.path.join(BASE\_DIR, 'media')"

&#x09;--now you have done the setting part but have to give url also in urls.py also

&#x09;for fetching you image url needs some import so import static setting and configrastion write in your urls.py page this

&#x09;  			"from django.conf import settings

&#x09;			from django.conf.urls.static import static"

&#x09;as a url write this at the last "+ static(settings.MEDIA\_URL, document\_root=settings.MEDIA\_ROOT)"

\-- now we have done the main thing but have to tell Django that i have creted a model so please look into it so we have to make migrasions

##### wow ran into an error and it was just that i added the + static url in new lin but it had to go just after your url box end like this

##### &#x09;] + static.....

&#x09;**\*\*big thing when we write our modul and makemigrations the Django writes sql queerys by it self which shows in migration folder wow**

\- after that you run migrate command to save everything

\-- when you do all that if you want to look your created table in the admin page you just have to connect your model to admin.py just write  					"from .models import rackets

&#x09;				admin.site.register(rackets)"

end for the day sorry couldn't complete - 15/05/2026 - 7:00 pm





