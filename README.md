# SOB_TASK_SUBMISSION_ARYAMAN

# Summer Of Bitcoin Code Challenge
A global program that matches students with open source, free software and technology-related organizations working on bitcoin to write code and become part of these communities while making some BTC along the way!

The organizations provide mentors who act as guides through the entire process, from learning about the community to contributing code.

Students get involved in and become familiar with the bitcoin open source community and put their summer break to good use. The program requires 10-12 weeks of time commitment with a minimum of expectation of 30 hours a week.


## What is a BitCoin?
BitCoin can be considered as a type of cryptocurrency. It was invented in 2009.. There are no physical bitcoins, only balances kept on a public ledger that everyone has transparent access to. All bitcoin transactions are verified by a massive amount of computing power. Bitcoin is very popular and has triggered the launch of hundreds of other cryptocurrencies, collectively referred to as altcoins.  Bitcoin is commonly abbreviated as "BTC." BitCoin can be considered as a leisure, for eg : you pay money to fruit seller that is considered as a trade.


## UNDERSTANDING OF PROBLEM:

    NAME - ARYAMAN [CSE SOPHOMORE] 
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

    
    Time Complexity: O(N^2), N = Number of Transaction in CSV file.
    
    NOTE : DUE TO MY PERSONAL ISSUES I CAN'T REFACTOR & OPTIMISED THIS SOLUTION , HOPE YOU UNDERSTAND.


## Tools and Technologies used for the task
   - Python
   - Linux 
   - Blockchain 
   - Data Mining
<br>

## MY APPROACH (Greedy):

- Append the transactions to check_trans [ ]
- Check if the selected transaction is valid if not set valid_trans_status = False, i.e. is all its parents are already included in the block.
- Sorting & arranging on the basis of value of fee
- Now iterate over sorted dict and check whether that transaction is valid or not and append valid transaction to **block.txt**

##### Time Complexity: O(N^2), N = Number of transactions in CSV file.