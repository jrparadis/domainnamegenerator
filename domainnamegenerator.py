from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import random
import sqlite3
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import RegexpTokenizer
import re
stopwordss = set(stopwords.words('english'))
xb = ''
'''
randompick = ['.com','.org','.net ','.me ','.mobi ','.us ','.biz ','.tv ','.mx ','.at ','.bz ','.com.co ','.net.co ','.nom.co ','.in ','.xxx ','.ag ','.uno ','.menu ','.luxury ',
'.build ','.bike ','.clothing ','.guru ','.holdings ','.plumbing ','.singles ','.ventures ','.estate ','.photography ','.gallery ','.camera ','.lighting ','.equipment ','.graphics ',
'.kitchen ','.construction ','.contractors ','.directory ','.today ','.technology ','.land ','.tips ','.diamonds ','.enterprises ','.voyage ','.careers ','.recipes ','.photos ',
'.shoes ','.company ','.cab ','.domains ','.limo ','.management ','.systems ','.center ','.computer ','.support ','.academy ','.solutions ','.repair ','.house ','.builders ','.camp',
'.education ','.glass ','.international ','.solar ','.training ','.email ','.institute ','.florist ','.coffee ','.club ','.codes ','.farm ','.holiday ','.marketing ','.agency ','.cheap ',
'.zone ','.bargains ','.boutique ','.cool ','.watch ','.viajes ','.expert ','.works ','.reviews ','.dance ','.democrat ','.futbol ','.foundation ','.cruises ','.rentals ','.villas ','.exposed ','.flights ','.vacations ','.social ','.immobilien ','.ninja ','.consulting ','.rocks ','.republican ','.buzz ','.maison ','.properties ','.tienda ','.condos ','.dating ','.events ','.productions ','.partners ','.london ','.cards ','.cleaning ','.catering ','.community ','.wiki ','.parts ','.supply ','.industries ','.supplies ','.tools ','.xyz ','.ink ','.bid ','.report ','.vision ','.moda ','.pub ','.trade ','.webcam ','.fish ','.actor ','.kaufen ','.services ','.rest ','.bar ','.engineering ','.gripe ','.capital ','.exchange ','.lease ','.pictures ','.media ','.associates ','.reisen ','.university ','.toys ','.town ','.haus ','.financial ','.wtf ','.fail ','.limited ','.care ','.clinic ','.surgery ','.dental ','.nyc ','.cash ','.tax ','.fund ','.investments ','.vegas ','.furniture ','.discount ','.fitness ','.schule ','.nagoya ','.world ','.shopping ','.college ','.studio ','.movie ','.kiwi ','.ltda ','.degree ','.vote ','.voting ','.army ','.church ','.digital ','.legal ','.berlin ','.blue ','.place ','.gives ','.vip ','.porn ','.fit ','.archi ','.loans ','.fun ','.desi ','.healthcare ','.vin ','.bayern ','.blackfriday ','.tech ','.site ','.review ','.style ','.money ','.country ','.guide ','.horse ','.blog ','.ist ','.accountant ','.family ','.website ','.hiv ','.apartments ','.sex ','.red ','.cooking ','.ski ','.surf ','.tattoo ','.work ','.sarl ','.green ','.school ','.tennis ','.voto ','.racing ','.rich ','.golf ','.promo ','.rehab ','.lawyer ','.gratis ','.vodka ','.poker ','.pics ','.business ','.sydney ','.cricket ','.theatre ','.flowers ','.vet ','.energy ','.win ','.attorney ','.lol ','.yoga ','.loan ','.xn--6frz82g ','.fans ','.hockey ','.space ','.science ','.gold ','.global ','.onl ','.news ','.wine ','.fishing ','.earth ','.bingo ','.ceo ','.miami ','.store ','.amsterdam ','.paris ','.qpon ','.beer ','.faith ','.doctor ','.engineer ','.barcelona ','.team ','.theater ','.film ','.taxi ','.hiphop ','.lgbt ','.irish ','.fyi ','.juegos ','.protection ','.shiksha ','.gifts ','.restaurant ','.date ','.tube ','.rodeo ','.cafe ','.stream ','.rip ','.adult ','.chat ','.men ','.link ','.wales ','.garden ','.istanbul ','.casino ','.delivery ','.guitars ','.download ','.gift ','.network ','.group ','.moe ','.design ','.online ','.navy ','.salon ','.click ','.one ','.auto ','.party ','.casa ','.okinawa ','.city ','.wedding ','.hospital ','.car ','.cars ','.software ','.sale ','.dog ','.black ','.video ','.nrw ','.ryukyu ','.bet ','.memorial ','.property ','.jewelry ','.credit ','.courses ','.band ','.games ','.airforce ','.art ','.yokohama ','.diet ','.help ','.sexy ','.quebec ','.finance ','.show ','.pink ','.football ','.direct ','.mom ','.coach ','.jetzt ','.love ','.immo ','.audio ','.game ','.cloud ','.ltd ','.security ','.mba ','.insure ','.life ','.market ','.accountants ','.tires ','.live ','.tours ','.dentist ','.bio ','.reise ','.deals ','.auction ','.pet ','.cymru ','.christmas ','.host ','.fashion ',
'.coupons ','.creditcard ','.mortgage ','.express ','.shop ','.kim ','.forsale ','.plus ','.photo ','.hosting ','.soccer ','.study ',
'.melbourne ','.pizza ','.claims ','.gmbh ',
'.best ','.rent ','.press ','.run']
'''
randompick = ['.com','.net']
finallist = []
def abclist():
    for a in range(10,36):
        for b in range(10,36):
            for c in range(10,36):
                return string.printable[a] + string.printable[b] + string.printable[c] + '.com'

def makelistofwords(startword, numofwords, double, delone):

    for each in range(numofwords):
        try:
            try:
                x = wordnet.synset((str(newlist[random.randrange(0,len(newlist))]))+'.n.02').definition()
            except:
                try:
                    x = wordnet.synset((str(newlist[random.randrange(0,len(newlist))]))+'.v.02').definition()
                except:
                    try:
                        x = wordnet.synset((str(newlist[random.randrange(0,len(newlist))]))+'.a.02').definition()
                    except:
                        x = wordnet.synset(str(startword) + '.n.01').definition()

            tokenizer = RegexpTokenizer(r'\w+')
            b = tokenizer.tokenize(x)
            newb =''
            for each in b:
                newb += each + ' '

            newlist = filter(lambda w: not w in stopwordss,newb.split())
            if delone == True:
                b = list(newlist[random.randrange(0,len(newlist))])
                del b[random.randrange(0,len(b))]
                newword = ''.join(b)
            else:
                newword = newlist[random.randrange(0,len(newlist))]

            global finallist
            tld = randompick[random.randrange(0,len(randompick))]
            if double == True:
                finallist.append(str((newword) + newlist[random.randrange(0,len(newlist))]) + str(tld))
            else:
                finallist.append(str((newword) + str(tld)))
        except ValueError:
            print (ValueError)
def randomdomainname(tld, lengthofdomain):
    x = ''
    for each in range(lengthofdomain):
        lengt = random.randrange(10,36)
        x += string.printable[lengt]
    x += tld
    return x

def makedomainlist(listname, numberofdomains):
    for each in range(numberofdomains):
        listname.append(randomdomainname('.net',4))
while(1):
    finallist = []
    #use this function to get one word domain names. first value is word to check (it walks thru a dictionary to generate the words to pick),
    #second is amount of domains to check, first t/f just uses the name twice (eg googlegoogle.com), second t/f removes random letters from the domain name (like tumblr or flickr)
    
    #makelistofwords('motorcycle',500, False, False)
    makedomainlist(finallist, 100)
    liststring = ''
    for each in finallist:
        liststring += each + '\n'
    driver = webdriver.Chrome()
    driver.get("https://www.godaddy.com/domains/bulk-domain-search.aspx")
    searchArea = driver.find_element_by_xpath("//textarea[@id='bulkSearchArea']")
    searchArea.send_keys(liststring)
    clicky = driver.find_element_by_xpath("//a[@id='bulkSearchBtn']")
    clicky.click()
    sql = sqlite3.connect('gooddomainnames.db')  
    cur = sql.cursor()
    clicky2 = driver.find_element_by_xpath("//div[@id='bulkProceedtoCheckout']")
    clicky2.click()
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source)


    cur.execute('CREATE TABLE IF NOT EXISTS tabley(domain TEXT, price TEXT)')
    cur.execute('SELECT * FROM tabley')
    sql.commit()
    
    for each in soup.find_all('div', class_='name'):
        for each1 in soup.find_all('span', class_='amount'):
            if each.get_text() == 'domain':
                pass
            elif str(each.get_text()) in str(randompick) + ' Bulk Domain Registration':
                pass
            else:
                namesdb = cur.execute("SELECT domain FROM tabley").fetchall()
                if str(each.get_text()) in str(namesdb):
                    pass
                else:
                    
                    cur.execute('INSERT INTO tabley VALUES(?, ?)', [str(each.get_text()), each1.get_text()])
                    sql.commit()
                    print (str(each.get_text()) + ' added to database')
    for each in soup.find_all('th', class_='domain'):
        for each1 in soup.find_all('span', class_='amount'):
            if each.get_text() == 'domain':
                pass
            elif re.search(r'Add*',each.get_text()):
                pass
            elif str(each.get_text()) in str(randompick) + ' Bulk Domain Registration':
                pass
            else:
                namesdb = cur.execute("SELECT domain FROM tabley").fetchall()
                if str(each.get_text()) in str(namesdb):
                    pass
                    
                else:
                    cur.execute('INSERT INTO tabley VALUES(?, ?)', [str(each.get_text()), each1.get_text()])
                    sql.commit()
                    print (str(each.get_text()) +  ' added to database')
    sql.commit()
    driver.quit()
            
    time.sleep(10)
