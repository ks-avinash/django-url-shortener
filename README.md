# django-url-shortener
A URL shortener is a Web Application that will create a short Uniform Resource Locator (URL) or Web page address from a long one so that the short version, which is easier to remember and enter, can be used instead.

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

Support uploading '.csv' file containing urls and show the shortened urls for each
