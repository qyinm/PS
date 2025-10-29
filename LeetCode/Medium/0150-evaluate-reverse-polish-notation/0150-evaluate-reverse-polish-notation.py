class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                st.append(int(token))
                continue

            top = st[-1]
            st.pop()
            match token:
                case '+':
                    st[-1] += top
                case '-':
                    st[-1] -= top
                case '*':
                    st[-1] *= top
                case '/':
                    st[-1] /= top
                    st[-1] = ceil(st[-1]) if st[-1] < 0 else floor(st[-1])
         
        return st[-1]