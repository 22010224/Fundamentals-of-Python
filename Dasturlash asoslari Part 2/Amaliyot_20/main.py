class Meta:
    """Meta nomli klass yaratamiz!"""
    def __init__(self, ism, familiya, yosh):
        """ Userning ma'lumotlari"""
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

 #   ***
        def get_age(self, yil):
            """ Userning yoshini qaytaradi """
            return yil - self.yosh

