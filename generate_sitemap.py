#!/usr/bin/env python

import json
import urllib2

space_id = ""
access_token = ""
content_type ="pages"
select_items = "fields.slug"

sitemap_url = "https://cdn.contentful.com/spaces/" + space_id + "/entries?access_token=" + access_token + "&content_type=" + content_type + "&select=" + select_items

sitemap_xml_file_location = "/data/httpd/site/www.assembly.org/html/sitemap.xml"

sitemap_json = json.load(urllib2.urlopen(sitemap_url))

sitemap_xml_file = open(sitemap_xml_file_location, 'w')

sitemap_xml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
sitemap_xml_file.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

for item in sitemap_json['items']:
  if item['fields']['slug'] == "frontpage":
    sitemap_xml_file.write('<url><loc>https://www.assembly.org/summer18</loc><priority>0.5</priority></url>\n')
  else:
    sitemap_xml_file.write('<url><loc>https://www.assembly.org/summer18/'+ item['fields']['slug'] +'</loc><priority>0.5</priority></url>\n')

sitemap_xml_file.write('</urlset>\n')
sitemap_xml_file.close()
