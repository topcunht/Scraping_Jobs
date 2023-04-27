from bs4 import BeautifulSoup
import requests
import time

print("Give some tags for searcing job")
key_info = input(">")
print(f" Searching for {key_info}")
print(" ")
def SearchJob():
    html_text = requests.get("https://www.kariyer.net/is-ilanlari?kw=python").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("div", class_ = "list-items")
    for index, job in enumerate(jobs):
        company_name = job.find("div", class_ = "subtitle").text.replace(" ", "")
        job_names = job.find("span", class_ = "k-ad-card-title multiline").text.replace(" ", "")
        published_time = job.find("span", class_ = "date date-other")
        more_info = job.find("a", href = True)["href"]
        published_time_new = ''
        if published_time is not None:
            published_time_new = published_time.text
        if key_info in job_names:
            with open(f'Posts/{index}.txt', 'w') as f:
                f.write(f" Company Name : {company_name.strip()}")
                f.write(f" Job Name : {job_names.strip()}")
                f.write("kariyer.net" + more_info)
            print(f' File Saved : {index}')
if __name__ == "__main__":
    while True:
        SearchJob()
        print("Give a time wait")
        time_wait = 600
        time.sleep(time_wait)   
    


    
