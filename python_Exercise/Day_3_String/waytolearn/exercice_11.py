def insertStr(string, elt_to_add):
    """insert a string in another string
        Args : 
            string (str) : Where to insert
            elt_to_add(str) : string to insert 
        
        Returns :
            str : new string 
    """
    try:
        middle = len(string) // 2
        return string[:middle] + elt_to_add + string[middle:]
    except TypeError:
        return TypeError("Argumment should be 'str'")

print(insertStr("{{}}","Python"))
print(insertStr("{{}}",10))
print(insertStr(0,-1))