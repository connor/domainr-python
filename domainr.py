import urllib2, json

class Domainr:

		def search(self, domain):
		    base_url = "https://domai.nr/api/json/search?q=" + domain
		    request = urllib2.Request(base_url)
		    request.add_header('User-Agent', 'domainr.py/0.1')
		    opener = urllib2.build_opener()
		    data = opener.open(request).read()
		    response = json.loads(data)
		    return response

		def info(self, domain):
		    base_url = "https://domai.nr/api/json/info?q=" + domain
		    request = urllib2.Request(base_url)
		    request.add_header('User-Agent', 'domainr.py/0.1')
		    opener = urllib2.build_opener()
		    data = opener.open(request).read()
		    response = json.loads(data)
		    return response


import unittest


class TestDomainr(unittest.TestCase):
    def testSearch(self):
        results = {u'query': u'connor', u'results': [{u'domain': u'connor.com', u'register_url': u'http://domai.nr/connor.com/register', u'host': '', u'path': '', u'subdomain': u'connor.com', u'availability': u'taken'}, {u'domain': u'connor.net', u'register_url': u'http://domai.nr/connor.net/register', u'host': '', u'path': '', u'subdomain': u'connor.net', u'availability': u'maybe'}, {u'domain': u'connor.org', u'register_url': u'http://domai.nr/connor.org/register', u'host': '', u'path': '', u'subdomain': u'connor.org', u'availability': u'taken'}, {u'domain': u'con.no', u'register_url': u'http://domai.nr/con.no/register', u'host': '', u'path': u'/r', u'subdomain': u'con.no', u'availability': u'taken'}, {u'domain': u'con.nr', u'register_url': u'http://domai.nr/con.nr/register', u'host': '', u'path': '', u'subdomain': u'con.nr', u'availability': u'available'}, {u'domain': u'cn.nr', u'register_url': u'http://domai.nr/cn.nr/register', u'host': '', u'path': '', u'subdomain': u'cn.nr', u'availability': u'unavailable'}, {u'domain': u'co', u'register_url': u'http://domai.nr/co/register', u'host': '', u'path': u'/nnor', u'subdomain': u'co', u'availability': u'tld'}, {u'domain': u'cn', u'register_url': u'http://domai.nr/cn/register', u'host': '', u'path': u'/nr', u'subdomain': u'cn', u'availability': u'tld'}]}

        d = Domainr()
        expected = d.search('connor')

        self.assertEqual( expected , results, "searching for 'connor' returns the correct hash")

    def testInfo(self):
    		results = {u'domain': u'connormontgomery.com', u'whois_url': u'http://domai.nr/connormontgomery.com/whois', u'subregistration_permitted': True, u'register_url': u'http://domai.nr/connormontgomery.com/register', u'tld': {u'domain': u'com', u'wikipedia_url': u'http://domai.nr/com/wikipedia', u'iana_url': u'http://domai.nr/com/iana'}, u'registrars': [{u'registrar': u'iwantmyname.com', u'name': u'iWantMyName', u'register_url': u'http://domai.nr/connormontgomery.com/register/iwantmyname.com'}, {u'registrar': u'101domain.com', u'name': u'101domain.com', u'register_url': u'http://domai.nr/connormontgomery.com/register/101domain.com'}, {u'registrar': u'dotster.com', u'name': u'Dotster', u'register_url': u'http://domai.nr/connormontgomery.com/register/dotster.com'}, {u'registrar': u'name.com', u'name': u'Name.com', u'register_url': u'http://domai.nr/connormontgomery.com/register/name.com'}, {u'registrar': u'godaddy.com', u'name': u'Go Daddy', u'register_url': u'http://domai.nr/connormontgomery.com/register/godaddy.com'}, {u'registrar': u'dreamhost.com', u'name': u'Dreamhost', u'register_url': u'http://domai.nr/connormontgomery.com/register/dreamhost.com'}, {u'registrar': u'marcaria.com', u'name': u'Marcaria', u'register_url': u'http://domai.nr/connormontgomery.com/register/marcaria.com'}, {u'registrar': u'namecheap.com', u'name': u'Namecheap', u'register_url': u'http://domai.nr/connormontgomery.com/register/namecheap.com'}, {u'registrar': u'networksolutions.com', u'name': u'Network Solutions', u'register_url': u'http://domai.nr/connormontgomery.com/register/networksolutions.com'}, {u'registrar': u'instra.com', u'name': u'Instra', u'register_url': u'http://domai.nr/connormontgomery.com/register/instra.com'}, {u'registrar': u'xdnet.co.uk', u'name': u'XDnet', u'register_url': u'http://domai.nr/connormontgomery.com/register/xdnet.co.uk'}, {u'registrar': u'123-reg.co.uk', u'name': u'123-reg', u'register_url': u'http://domai.nr/connormontgomery.com/register/123-reg.co.uk'}, {u'registrar': u'moniker.com', u'name': u'Moniker', u'register_url': u'http://domai.nr/connormontgomery.com/register/moniker.com'}, {u'registrar': u'netfirms.com', u'name': u'Netfirms', u'register_url': u'http://domai.nr/connormontgomery.com/register/netfirms.com'}, {u'registrar': u'bottledomains.com.au', u'name': u'Bottle Domains', u'register_url': u'http://domai.nr/connormontgomery.com/register/bottledomains.com.au'}, {u'registrar': u'domaindiscount24.net', u'name': u'Key-Systems', u'register_url': u'http://domai.nr/connormontgomery.com/register/domaindiscount24.net'}, {u'registrar': u'1and1.com', u'name': u'1and1.com', u'register_url': u'http://domai.nr/connormontgomery.com/register/1and1.com'}, {u'registrar': u'1and1.co.uk', u'name': u'1and1 UK', u'register_url': u'http://domai.nr/connormontgomery.com/register/1and1.co.uk'}, {u'registrar': u'idotz.net', u'name': u'iDotz.Net', u'register_url': u'http://domai.nr/connormontgomery.com/register/idotz.net'}, {u'registrar': u'eurodns.com', u'name': u'EuroDNS', u'register_url': u'http://domai.nr/connormontgomery.com/register/eurodns.com'}, {u'registrar': u'register.com', u'name': u'register.com', u'register_url': u'http://domai.nr/connormontgomery.com/register/register.com'}, {u'registrar': u'cctld.uz', u'name': u'ccTLD.uz', u'register_url': u'http://domai.nr/connormontgomery.com/register/cctld.uz'}, {u'registrar': u'enom.com', u'name': u'eNom', u'register_url': u'http://domai.nr/connormontgomery.com/register/enom.com'}, {u'registrar': u'gandi.net', u'name': u'Gandi', u'register_url': u'http://domai.nr/connormontgomery.com/register/gandi.net'}], u'subdomains': [], u'host': '', u'path': '', u'www_url': u'http://domai.nr/connormontgomery.com/www', u'query': u'connormontgomery.com', u'subdomain': u'connormontgomery.com', u'domain_idna': u'connormontgomery.com', u'availability': u'taken'}

    		d = Domainr()
    		expected = d.info('connormontgomery.com')
    		self.assertEqual( expected , results, "searching for 'connor' returns the correct hash")


if __name__ == '__main__':
    unittest.main()