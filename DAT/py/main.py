from model import *

admin = Answers('1','dhuio', 'sfjh', 'djij', 'dfndjs', 'jdfjh', 'iuhiuhiu',
                               '123', 'isjdf', 'dsfjoij', 'fdhjha', 'shuhfd', 'sfdhu',
                               'sdhu', 'dsakhu', 'dfjjhwuh', '2134', 'dfhuh')
db.session.add(admin)
db.session.commit()