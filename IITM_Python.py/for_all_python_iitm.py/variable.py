ram_bank_balance=100000
#ram's bank balance,note that this is positive
ram_loan=500000
#ram's loan this is to be returned by him and hence will count 
#as negative 
lakshman_bank_balance=200000
#lakshman's bank balance ,this is positive 
lakshman_loan=100000
#lakshman's this is to be returend by him and hence will count 
#as positive 
net_income=ram_bank_balance+lakshman_bank_balance 
#net income is the total bank balance of the two brothers
net_liability=ram_loan+lakshman_loan
#net liability is the total loan of two brothers
final_values=net_income-net_liability
# final value of the family final money 
print("so,the family has",final_values)