def find_anagrams(word, candidates):
    """
        find_angrams helps to find .
        
        Args : 
            - word (str) : a target word.
            - candidates (list) : a list of word that can be word's anagram
            
        Returns :
            anagrams (list)
    """
    
    return [candidate for candidate in candidates  if "".join(sorted(candidate.lower())) == "".join(sorted(word.lower())) and candidate.lower() != word.lower()]