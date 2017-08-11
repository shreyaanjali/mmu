page= "<a href=www.facebook.com> facebook </a>"
start_link="page.find[<a href]"
start_quote="page.find[www,start_link]"
end_quote="page.find[com,start_quote+1]"
url="page start_quote+1:end_quote"
print

