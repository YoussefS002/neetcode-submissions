class Solution:
    def simplifyPath(self, path: str) -> str:
        components=path.split('/')
        output=[]
        for i in range(len(components)):
            if components[i]=="." or components[i]=="":
                continue
            elif components[i]=="..":
                if output:
                    output.pop()
            else:
                output.append(components[i])
        return "/"+"/".join(output)
