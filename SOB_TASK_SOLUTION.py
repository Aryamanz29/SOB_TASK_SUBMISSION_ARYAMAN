"""
    NAME - ARYAMAN [CSE SOPHOMORE] 
    OPEN SOURCE ENTHUSIAST
    https://github.com/Aryamanz29
   
    ------ Summer of Bitcoin Code Challenge ------
    
    UNDERSTANDING OF PROBLEM:
        Each transaction has three major things:
            - Fee
            - Weight (Size)
            - Parent transaction
       
        There is an list of transactions with the following conditons:
            1) It should be an ordered list, i.e no transaction should come before Parent transaction
            2) Weight should be <= 4,000,000
            3) A transaction may only appear in a block if all of its parents appear
             earlier in the block.
            4)Should Maximize Fee

    APPROACH(Greedy):
        - Append the transactions to check_trans[]
        - Check if the selected transaction is valid if not set valid_trans_status = False, i.e. is all its parents are already included in the block.
        - Sorting & arranging on the basis of value of fee
        - Now iterate over sorted dict and check whether that transaction is valid or not and append valid transaction to block.txt
    
    Time Complexity: O(N^2), N = Number of Transaction in CSV file.
    
    NOTE : DUE TO MY PERSONAL ISSUES I CAN'T REFACTOR & OPTIMISED THIS SOLUTION , HOPE YOU UNDERSTAND.

"""

def make_block_transaction():
     max_weight = 4000000
     init_weight = 0
     parents_trans = []
     trans_fee = {}
     check_trans = [] 
     with open('mempool.csv') as f:
         
         trans_id = 1
         for line in f.readlines()[1:]:
            valid_trans_status = False # Intialize transaction as invalid 
            txid, fee, weight, parents = line.strip().split(',') # Extract values from CSV
            check_trans.append(txid) # Append transaction ID's to check_trans[]
            if parents == "":
                valid_trans_status = True
                parents_trans.append([parents, trans_id, valid_trans_status])
            else:
                if parents.find(';'): # Extract multiple parent trans
                    parents = parents.split(';')
                    for parent in parents:
                        if parent in check_trans: # Check if the selected transaction is valid, i.e. is all its parents are already included in the block.
                            valid_trans_status = True
                            parents_trans.append([parents, trans_id, valid_trans_status])
                        else:
                            valid_trans_status = False
                            parents_trans.append([parents, trans_id, valid_trans_status])
                else:
                       if parent in check_trans:
                            valid_trans_status = False
                            parents_trans.append([parents, trans_id, valid_trans_status])
                       else:
                            valid_trans_status = True
                            parents_trans.append([parents, trans_id, valid_trans_status])

            trans_fee.update({txid:[int(fee),int(weight),trans_id]}) # Create Dict for { 'txid ': [fee, weight, trans_id] }
            trans_id+= 1 
         

         trans_fee = sorted(trans_fee.items(), key=lambda x: x[1][0], reverse=True) # Sorting & arranging on the basis of value of fee
        #  max_fees = 0
         for trans , fees_weight_id in trans_fee:
            #    max_fees+= fees_weight_id[0] 
               if init_weight <= max_weight: # Weight should be less than 4,000,000
                  
                   for parent in parents_trans:
                        if fees_weight_id[2] == parent[1]: # Check trans_id
                            #  print(parent)
                             if parent[2]: # Check valid transaction
                                with open('block.txt', 'a') as file:
                                    file.write(trans + '\n')
                                    init_weight+= fees_weight_id[1] # NOTE : Don't run this script twice , 
                                                                    # because text file is opened in append mode. 
                                                                    # If you really want to run first clear content of file or delete exisitng one. 
                        else:
                            continue 
               else:
                    break;
        #  print(max_fees) #2988465 satoshis

make_block_transaction()
