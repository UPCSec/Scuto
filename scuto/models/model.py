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