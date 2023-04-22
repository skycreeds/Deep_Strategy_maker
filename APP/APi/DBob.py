from deta import Deta

class DBcon:
    def __init__(self) -> None:
        self.DeTa=Deta('a0vpxq7szms_My9Z8jKAMrMgUqKjnZjmfBK34WrYsA1k')


    def DB_query(self,DB,Query={}):
        db=self.DeTa.Base(DB)
    


    def insert_info(self,DB,item={}):
        #returns error if not inserted
        db=self.DeTa.Base(DB)
        try:
            db.insert(item)
        except:
            return False
        finally:
            return True
        
    
    def 