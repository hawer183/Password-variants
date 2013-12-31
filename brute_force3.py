'''
Created on 2013.12.30.

@author: zolka
'''
import itertools
import time
import sqlite3

def main():    
    try:
        print ("Still running, please wait...")
        start_time = time.time()

        con = sqlite3.connect("dictionary.sqlite")
        c = con.cursor()
        c.execute("CREATE TABLE test (word char(10))")
        
        #with open('dictionary.txt', 'w') as f:
        
        for word in itertools.imap(''.join, itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@&#!*', repeat=4)):
            #print(string)            
            #print >> f, string
            c.execute("INSERT INTO test (word) VALUES (?)", (word,))
        con.commit()
            
    finally:
        print ("Done! Check the txt file!\n")
        end_time = time.time()
        print "Processing time was: ", end_time - start_time
        
if __name__ == "__main__": main()