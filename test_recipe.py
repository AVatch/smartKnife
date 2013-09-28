import urllib2 as recipeUrl
import urllib
import sys
import webbrowser
import random as rand

urlAddr = 'http://allrecipes.com/'
veggie = sys.argv[1]

print(veggie)

req = recipeUrl.Request('http://allrecipes.com/search/default.aspx?qt=k&wt=' + veggie + '&rt=r&origin=Home%20Page')
f = recipeUrl.urlopen(req)
    
search =  f.read()
href = []

for word in search.split(" "):
    if word.startswith('href="/Recipe/'):
        href.append(word)

for i in range(len(href)):
    href[i] = 'http://allrecipes.com'+href[i][6:]

randNumber = rand.randint(1, len(href))

webbrowser.open_new(href[randNumber])


