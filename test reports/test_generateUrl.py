import generate_url
import unittest

tld = ['.com', '.org', '.net', '.int', '.edu', '.gov', '.mil']
rating_sites = ['mapquest', 'yelp', 'bbb', 'podium', 'porch', 'chamberofcommerce', 'angi']

class test_generateUrl(unittest.TestCase):

    def test_appends(self):

        companyName1 = "The File Depot"
        companyName2 = "Lewk"

        url1 = generate_url.appends(companyName1,tld)
        url2 = generate_url.appends(companyName2,tld)

        self.assertEqual(url1, ["https://www.thefiledepot.com"])
        self.assertEqual(url2, ["https://www.lewk.com"])

    def test_cleanData(self):
        companyName1 = "The File Depot"
        companyName2 = "Aspen Dental"
        companyName3 = "Creative Ape Studios, LLC"

        name1 = generate_url.clean_data(companyName1)
        name2 = generate_url.clean_data(companyName2)
        name3 = generate_url.clean_data(companyName3)

        self.assertEqual(name1, "thefiledepot")
        self.assertEqual(name2, "aspendental")
        self.assertEqual(name3, "creativeapestudios")

    def test_valid(self):
        url1 = "https://www.thefiledepot.com"
        url2 = "https://www.badlandsdoitbesthardware.com"
        url3 = "https://www.thefiledepot.org"

        validUrl1 = generate_url.validURl(url1)
        validUrl2 = generate_url.validURl(url2)
        invalidUrl3 = generate_url.validURl(url3)

        self.assertTrue(validUrl1, "Failed")
        self.assertTrue(validUrl2, "Failed")
        self.assertFalse(invalidUrl3, "Failed")

    def test_getUrl(self):
        name1 = "Carmex"
        name2 = "Sky Visions"

        url1 = generate_url.getURL(name1, [], rating_sites)
        url2 = generate_url.getURL(name2, [], rating_sites)

        self.assertEqual(len(url1), 10)
        self.assertEqual(len(url2), 10)

    def test_filter(self):
        url1 = "https://vetterhomes.com/"
        url2 = "https://www.bbb.org/us/nd/bismarck/profile/general-contractor/vetter-homes-inc-0704-1000000003"

        valid_url = generate_url.filter(url1, rating_sites)
        rating_url = generate_url.filter(url2, rating_sites)

        self.assertTrue(url1, "failed")
        self.assertFalse(rating_url, "failed")

    def test_statusCode(self):
        url1 = "https://vetterhomes.com/"
        url2 = "http://www.mnintegrity.com"
        url3 = "https://www.ablemovingcorp.com/"

        statusCode1 = generate_url.status_code(url1)
        statusCode2 = generate_url.status_code(url2)
        statusCode3 = generate_url.status_code(url3)

        self.assertEqual(statusCode1, 200)
        self.assertEqual(statusCode2, 404)
        self.assertEqual(statusCode3, -1)

    def test_scrap(self):
        infor1 = ['Tree Trust Landscape Services' '1419 Energy Park Dr' 'Saint Paul' 'MN',  9527673880, 'jareds@treetrust.org']
        infor2 = ['Blackduck Auto Parts Inc' '25730 Highway 71 Ne'	'Blackduck'	'MN', 2188354278, '']


        content1 = generate_url.scrap("https://treetrust.org/landscape-services/", 'Tree Trust Landscape Services', infor1)
        content2 = generate_url.scrap("https://www.dnb.com/business-directory/company-profiles.blackduck_auto_parts_inc.6e26f4796a28746e7af0cf435484863b.html", 'Blackduck Auto Parts Inc', infor2)

        self.assertEqual(content1, 3)
        self.assertEqual(content2, 3)

    def test_correctUrl(self):
        name1 = "Carmex"
        potentialUrl1 = ['https://www.mycarmex.com/',
                         'https://en.wikipedia.org/wiki/Carmex',
                         'https://carmex.com/',
                         'https://carmex.com/distributors/',
                         'https://carmex.com/products/milling-tools/thread-milling/',
                         'https://carmex.com/catalogs/',
                         'https://carmex.com/products/',
                         'https://www.amazon.com/Carmex-Classic-Balm-0-35-Blister/dp/B001KYTQ8W',
                         'https://en.wikipedia.org/wiki/Carmex#History',
                         'https://en.wikipedia.org/wiki/Carmex#Ingredients']
        infor1 = ['Carmex' '12800 Whitewater Dr # 110'	'Hopkins' 'MN' ,9529433900,'']

        url1 = generate_url.correctUrl(potentialUrl1, name1, infor1)

        self.assertEqual(url1, 'https://www.mycarmex.com/')

if __name__ == '__main__':
    unittest.main()