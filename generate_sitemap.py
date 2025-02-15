import os
import time
import xml.etree.ElementTree as ET
from datetime import datetime

def get_lastmod_time(filepath):
    timestamp = os.path.getmtime(filepath)
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S+00:00')

def format_blog_url(filename, base_url):
    parts = filename.split("-")
    if len(parts) < 5:
        return None
    year, month, day = parts[:3]
    post_name = "-".join(parts[3:])
    post_name = os.path.splitext(post_name)[0]  # Remove .md extension
    return f"{base_url}/assets/blog/posts/{year}/{month}/{day}/{post_name}.html"

def generate_sitemap(wiki_directory, posts_directory, base_url, output_file="sitemap.xml"):
    urlset = ET.Element("urlset", {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xsi:schemaLocation": "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    })
    
    # Add home URL
    home_url = ET.SubElement(urlset, "url")
    ET.SubElement(home_url, "loc").text = f"{base_url}/home"
    ET.SubElement(home_url, "lastmod").text = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S+00:00')
    ET.SubElement(home_url, "priority").text = "0.80"
    
    # Scan wiki directory for .md files
    for filename in os.listdir(wiki_directory):
        if filename.endswith(".md"):
            filepath = os.path.join(wiki_directory, filename)
            file_base_name = os.path.splitext(filename)[0]
            file_url = f"{base_url}/{file_base_name}"
            
            url_element = ET.SubElement(urlset, "url")
            ET.SubElement(url_element, "loc").text = file_url
            ET.SubElement(url_element, "lastmod").text = get_lastmod_time(filepath)
            ET.SubElement(url_element, "priority").text = "0.64"
    
    # Scan _posts directory for .md files
    for filename in os.listdir(posts_directory):
        if filename.endswith(".md"):
            filepath = os.path.join(posts_directory, filename)
            post_url = format_blog_url(filename, base_url)
            if post_url:
                url_element = ET.SubElement(urlset, "url")
                ET.SubElement(url_element, "loc").text = post_url
                ET.SubElement(url_element, "lastmod").text = get_lastmod_time(filepath)
                ET.SubElement(url_element, "priority").text = "0.64"
    
    # Write XML to file
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"Sitemap successfully generated: {output_file}")

if __name__ == "__main__":
    wiki_directory = "./wiki"  # 현재 디렉토리에서 wiki 폴더
    posts_directory = "./_posts"  # 현재 디렉토리에서 _posts 폴더
    base_url = "https://www.vlsi.kr"
    generate_sitemap(wiki_directory, posts_directory, base_url)
