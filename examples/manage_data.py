from pyscience.datam import Data, Condition as C
from pprint import pprint
data = Data('data.csv')

condition = C('Age') > 40

pprint(data.where(condition))
