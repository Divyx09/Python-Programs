import pandas as pd
from datetime import date
import holidays
from workalendar.europe import Germany

for holiday in holidays.Germany(years=[2020, 2021]).items():
    print(holiday)
