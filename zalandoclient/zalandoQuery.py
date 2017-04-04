class zalandoQuery:
    def __init__(self):
        self.ageGroup = None
        self.gender = None
        self.length = None
        self.size = None
        self.minprice = None
        self.maxprice = None
        self.page = None
        self.pageSize = None
        self.categories = []
        self.BASE_URL = "https://api.zalando.com/articles"

    def setPriceRange(self, minprice, maxprice):
        self.minprice = minprice
        self.maxprice = maxprice

    def setPage(self, page):
        self.page = page

    def setPageSize(self, pageSize):
        self.pageSize = pageSize

    def setSize(self, size):
        self.size = size

    def setCategories(self, categories):
        self.categories = categories

    def setLength(self, length):
        self.length = length

    def setAgeGroup(self, ageGroup):
        """ageGroup can be one of: babies, kids, teen, adult"""
        self.ageGroup = ageGroup

    def setGender(self, gender):
        """gender can be one of: male, female"""
        self.gender = gender

    def build_query(self):
        tobuild = []

        if self.ageGroup:
            tobuild.append("ageGroup=" + self.ageGroup)
        if self.gender:
            tobuild.append("gender=" + self.gender)
        if self.length:
            tobuild.append("length=" + str(self.length))
        if self.size:
            tobuild.append("size=" + str(self.size))
        if self.minprice or self.maxprice:
            if not self.minprice:
                self.minprice = 0
            if not self.maxprice:
                self.maxprice = 99999
            tobuild.append("price=" + str(self.minprice) + "-" + str(self.maxprice))
        if self.page:
            tobuild.append("page=" + str(self.page))
        if self.pageSize:
            tobuild.append("pageSize=" + str(self.pageSize))
        if len(self.categories) > 0:
            for category in self.categories:
                tobuild.append("category=%s" % category)
        arguments = "&".join(tobuild)
        url = self.BASE_URL + "?"
        if len(tobuild) > 0:
            url += arguments
        return url

