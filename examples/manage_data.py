from pyscience.datam import Data, Condition as C
from pprint import pprint
data = Data('data.csv')

condition = (C('Age') >= 40) & (C('Age') < 50)
#condition = (C('Country') == 'Spain') & (C('Age') == 55)

pprint(data.where(condition))
