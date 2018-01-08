class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        1) Use a stack
        2) Push the number into stack
        3) If a operator is seen, pop the two numbers out of stack and perform the operation and push it again.
        4) Finally pop the last number.
        """
        st  = []
        def is_operator (item):
            if ((item == "+") or (item == "-") or (item == "*") or (item == "/")):
                return True;
            return False

        for token in tokens:
            if (is_operator(token)):
                b = int(st.pop())
                a = int(st.pop())
                if (token == "+"):   
                    st.append(a+b)
                elif (token == "-"):
                    st.append(a-b)
                elif (token == "*"):
                    st.append(a*b)
                elif (token == "/"):
                    st.append(a/b)
            else:
                st.append(token)
        return  (int(st.pop()))

