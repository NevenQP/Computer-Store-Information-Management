import json

with open("staff.txt", "w") as f:
    f.truncate(0)
    f.write(json.dumps([['ID','Name','Dob','Contact Number','Email','Position']]))

with open("product.txt", "w") as f:
    f.truncate(0)
    f.write(json.dumps([['ID','Name','CPU','RAM','Hard Disk','OS','Color']]))

with open("customer.txt", "w") as f:
    f.truncate(0)
    f.write(json.dumps([['ID','Name','Dob','Contact Number','Email','Address']]))

with open("bill.txt", "w") as f:
    f.truncate(0)
    f.write(json.dumps([['Bill_id','Product_id','Cost','Staff_id','Time']]))

with open("account.txt", "w") as f:
    f.truncate(0)