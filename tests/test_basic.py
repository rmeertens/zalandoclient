import unittest
from zalandoclient.zalandoQuery import *
from zalandoclient.zalandoClient import *

class allTests(unittest.TestCase):

    def getStandardQuery(self):
        query_builder = zalandoQuery()
        query_builder.setAgeGroup("adult")
        query_builder.setGender("male")
        query_builder.setLength(36)
        query_builder.setSize(32)
        query_builder.setPriceRange(0, 50)
        return query_builder

    def testReadsCorrect(self):
        query = self.getStandardQuery()
        json_data = get_articles(query)
        page_count = json_data['totalPages']
        self.assertGreater(page_count,0)
    def testInStock(self):
        query = self.getStandardQuery()
        print(query.build_query())
        for article in get_articles_all_pages(query):
            self.assertTrue('ADULT' in article['ageGroups'])
    def testCategories(self):
        query_builder = zalandoQuery()
        query_builder.setCategories(['casual-overhemden'])
        query_builder.setPriceRange(0,30)
        for article in get_articles_all_pages(query_builder ):
            self.assertTrue('casual-overhemden' in article['categoryKeys'])

    def testNonexistingCategory(self):
        query_builder = zalandoQuery()
        query_builder.setCategories(['not-existing-category-here'])
        self.assertRaises(ValueError)

    def testCategoryExists(self):
        allcategories = get_possible_category_keys()
        self.assertTrue('herenschoenen' in allcategories)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
