"""
721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""

"""
Create a Node, with name, email and use
- Every email should point to the Node
- while inserting an account... if there are nodes conflicting.. resolve the conflicts.
- return the sorted emails with the Nodes in an Answer
"""
class MyNode(object):
    def __init__ (self, name, emails):
        self.name = name
        self.email =set ()
        self.use = True
        for email in emails:
            self.email.add(email)
    def add (self,emails):
        for email in emails:
            self.email.add(email)
    def setUse (self):
        self.use = True
    def setNoUse (self):
        self.use = False

class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # If there are multiple nodes.. pick the first Node and set it to True.
        # copy the other nodes email to the first Node.
        # set the other nodes as false.
        def resolveConflicts (Conflicts,nameAccountDict):
            prevNode = None
            for Node in Conflicts:
                if (prevNode == None):
                    prevNode = Node
                    prevNode.setUse()
                    continue;
                Node.setNoUse()
                prevNode.add(Node.email)
                for email in Node.email:
                    nameAccountDict[email] = prevNode
            return prevNode

        Ans = []
        nameAccountDict = dict()

        for account in accounts:
            Node = None
            Conflicts = []
            # for emails check if there are conflicts
            for item in account[1:]:
                if (item in nameAccountDict):
                    Conflicts.append(nameAccountDict[item])
            # Resolve the Conflicts.. At the end have only one Node
            Node = resolveConflicts(set(Conflicts),nameAccountDict)
            # Assign all emails to the Node
            for item in account[1:]:
                nameAccountDict[item]  = Node
            # If Node is none. create the Node and set the pointers.
            if (Node == None):
                Node = MyNode(account[0],account[1:])
                for item in account[1:]:
                    nameAccountDict[item] = Node
                Ans.append(Node)
            Node.add(account[1:])

        # For all the answer add it to Answer
        AList = []
        for Node in Ans:
            if (Node.use):
                AList.append([Node.name ]+ sorted(Node.email))
        return AList

                        
