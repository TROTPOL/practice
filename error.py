class ErrorBase(Exception):
       pass

class NameError(ErrorBase):
      
        text = 'Назва має містити лише англійські літери: a-z, A-Z.\nСпробуйте ще раз.'
        
        def __init__(self):
            super().__init__()
            self.msg = self.text

        def __str__(self):
              return self.msg
       
class CityNameError(ErrorBase):
        
        text = 'Не існує такої назви міста!!!'

        def __init__(self):
            super().__init__()
            self.msg = self.text

        def __str__(self):
              return self.msg
