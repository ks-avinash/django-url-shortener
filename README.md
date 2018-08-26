# django-url-shortener

**A URL shortener is a Web Application(RESTfull API endpoints) that will create a short Uniform Resource Locator (URL) or Web page address from a long one so that the short version, which is easier to remember and enter, can be used instead.**

creating a shortened url

fetching list of shortened urls

fetching original url from a shortened url

deleting shortened-urls

Constraints for the shortener service

Shortened urls should be unique for different urls.

Shortener service should generate the same url for all of below cases

google.com

www.google.com

http://google.com

http://www.google.com

https://google.com

https://www.google.com

Its support uploading '.csv' file containing urls and show the shortened urls for each

Postman Collection for Above Operations(REST API endpoints)

https://www.getpostman.com/collections/f6efcf11b5689b75121e

# Instructions

- `git clone https://github.com/avinashkunuje/django-url-shortener.git`

- `python3 -m venv yourenvname`

- `source activate yourenvname`

- `pip install -r requirements.txt`

- `cd django-url-shortener`

- `python manage.py runserver`
