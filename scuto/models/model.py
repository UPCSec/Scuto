class Model():

    @classmethod
    def get_or_none(cls, *args, **kwargs):
        """
        Returns None if MultipleObjectsReturned or DoesNotExist is raised
            :param cls: 
            :param *args: 
            :param **kwargs: 
        """   
        try:
            return cls.objects.get(*args, **kwargs)
        except:
            return None
    
    def update_with_json(self, data):
        """
        Update a document object with json data
            :param data: asd
        """
        pass