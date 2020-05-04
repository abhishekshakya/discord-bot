from phlib import PornHub
import random
import requests
ph = PornHub()
# a=ph.categories()
a = ph.categories
st = '''here are all the commands
    **example**           **description**
    **.help**          -> *to open this message*
    **.link**          -> *gives random porn link*
    **.link keyword**  -> *keyword should be separated by '-'(dash) not ' '(space)*
    **.degi**          -> *some random reply from audrey bitoni*
    **.clear a**       -> *'a' is an integer it deletes last 'a' messages from chat*      
    **.info username** -> *shows rating and rank of username in codeforces*
    **.contest**       -> *to know codeforces upcoming contest timing*
    **.register**      -> *to get registration page link of the codeforces*
    **.poblem**        -> *gives random problem (from level A,B,C)*
    **.poblem  B**     -> *gives problem from level B*
    **.poblem dp**     -> *gives problem from tag dp (level A,B,C)*
    **.poblem dp E**   -> *gives level E problem from tag dp*
    **.tags**          -> *gives tag that has to used in .poblem*
    **.me_ghissu**     -> *github code*
    **DESCLAIMER - gaali mt dena agr bezti ni krani to**
    '''
print(len(st))