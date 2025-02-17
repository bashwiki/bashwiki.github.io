import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

def get_lastmod_time(filepath):
    timestamp = os.path.getmtime(filepath)
    return datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-%dT%H:%M:%S+00:00')

def format_blog_url(filename, base_url):
    parts = filename.split("-")
    if len(parts) < 5:
        return None
    year, month, day = parts[:3]
    post_name = "-".join(parts[3:])
    post_name = os.path.splitext(post_name)[0]  # .md 확장자 제거
    return f"{base_url}/assets/blog/posts/{year}/{month}/{day}/{post_name}.html"

def generate_sitemap(wiki_directory, posts_directory, base_url, output_file="sitemap.xml"):
    urlset = ET.Element("urlset", {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xsi:schemaLocation": "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    })
    
    # 홈 URL 추가
    home_url = ET.SubElement(urlset, "url")
    ET.SubElement(home_url, "loc").text = f"{base_url}/home"
    ET.SubElement(home_url, "lastmod").text = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S+00:00')
    ET.SubElement(home_url, "priority").text = "0.80"
    
    # wiki 디렉토리 처리
    if os.path.isdir(wiki_directory):
        wiki_files = [f for f in os.listdir(wiki_directory) if f.endswith(".md")]
        if wiki_files:
            for filename in wiki_files:
                filepath = os.path.join(wiki_directory, filename)
                file_base_name = os.path.splitext(filename)[0]
                file_url = f"{base_url}/{file_base_name}"
                
                url_element = ET.SubElement(urlset, "url")
                ET.SubElement(url_element, "loc").text = file_url
                ET.SubElement(url_element, "lastmod").text = get_lastmod_time(filepath)
                ET.SubElement(url_element, "priority").text = "0.64"
        else:
            print(f"경고: '{wiki_directory}' 디렉토리에 .md 파일이 없습니다.")
    else:
        print(f"경고: '{wiki_directory}' 디렉토리가 존재하지 않습니다.")
    
    # posts 디렉토리 처리
    if os.path.isdir(posts_directory):
        posts_files = [f for f in os.listdir(posts_directory) if f.endswith(".md")]
        if posts_files:
            for filename in posts_files:
                filepath = os.path.join(posts_directory, filename)
                post_url = format_blog_url(filename, base_url)
                if post_url:
                    url_element = ET.SubElement(urlset, "url")
                    ET.SubElement(url_element, "loc").text = post_url
                    ET.SubElement(url_element, "lastmod").text = get_lastmod_time(filepath)
                    ET.SubElement(url_element, "priority").text = "0.64"
        else:
            print(f"경고: '{posts_directory}' 디렉토리에 .md 파일이 없습니다.")
    else:
        print(f"경고: '{posts_directory}' 디렉토리가 존재하지 않습니다.")
    
    # 출력 파일 경로를 절대경로로 변환
    output_path = os.path.abspath(output_file)
    
    # 혹시 출력 대상이 이미 디렉토리인 경우 체크
    if os.path.isdir(output_path):
        print(f"오류: '{output_path}'는 디렉토리입니다. 파일 이름을 변경해 주세요.")
        return

    # XML 파일로 저장 (파일 객체를 이용)
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)
    try:
        with open(output_path, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)
        print(f"Sitemap successfully generated: {output_path}")
    except OSError as e:
        print(f"파일 작성 중 오류 발생: {e}")

if __name__ == "__main__":
    wiki_directory = "./wiki"    # 현재 디렉토리의 wiki 폴더
    posts_directory = "./_posts"  # 현재 디렉토리의 _posts 폴더
    base_url = "https://bashwiki.github.io"
    generate_sitemap(wiki_directory, posts_directory, base_url)
