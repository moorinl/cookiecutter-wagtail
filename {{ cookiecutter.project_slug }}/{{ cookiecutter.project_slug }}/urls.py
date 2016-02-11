from django.conf.urls import include, url
from django.contrib import admin

{%- if cookiecutter.generate_sitemap == 'yes' -%}from wagtail.contrib.wagtailsitemaps.views import sitemap{%- endif -%}
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),
    {%- if cookiecutter.generate_sitemap == 'yes' -%}url('^sitemap\.xml$', sitemap),{%- endif -%}
    url(r'', include(wagtail_urls)),
]
