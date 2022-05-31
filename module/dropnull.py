class ClearNull:
    """Clear null values if null it will drop the rows out"""
    
    def __init__(self, dataframe, columns):
        self.dataframe = dataframe
        self.columns = columns
        
    def get_data(self):
        return self.dataframe[self.columns]
        
    def isnullchecking(self):
        """Check if the text is null or not if null turn into True"""
        df = self.get_data()
        self.dataframe['check'] = df.isnull()
        return self.dataframe[self.dataframe['check'] == True]
    
    def dropnull(self):
        """Drop the null row"""
        null = self.isnullchecking()
        df = self.dataframe
        index_name = null[null['check'] == True].index
        df.drop(index_name, inplace=True)
        return self.dataframe
    
    def reset_index(self):
        """Reset the index of the row"""
        df = self.dropnull()
        df.reset_index(drop=True, inplace=True)
        return df
    
    def drop_check(self):
        df = self.reset_index()
        df = df.drop(columns='check')
        return df
        
    def output(self):
        return self.drop_check()


