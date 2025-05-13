from backend.src.models import SummarizedData
from database import get_entry, add_entry
import json


send = SummarizedData(
    region_code='test2',
    summ=['test1', 'test2', 'test3', 'test4', 'test5']
)



on_db = get_entry('US')
print(on_db)
if on_db is not None:
    for i in range(5):
        # sent in string literal '{"id": id, "content": content}/n'
        print(json.dumps({"id": i, "content": on_db['summaries'][i]}) + "\n")

