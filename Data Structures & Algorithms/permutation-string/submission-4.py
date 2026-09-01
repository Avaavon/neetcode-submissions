class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 in s2? order does not matter
        # but must be consecutive
        
        # step 1: check s1 NOT > s2

        if len(s1) > len(s2):
            return False
        
        # step 2: make dict with s1
        s1_dict = {}
        for c in s1:
            s1_dict[c] = 1 + s1_dict.get(c,0)
        
        # step 3: create first window
        s2_dict = {}
        for i in range(len(s1)):
            c = s2[i]
            s2_dict[c] = 1 + s2_dict.get(c,0)
        
        # step 4: check matches from first window
        matches = 0
        for key, value in s1_dict.items():
            if s2_dict.get(key,0) == value:
                matches += 1
        if matches == len(s1_dict):
            return True

        # step 5: check remaining windows if not found
        l = 0
        # adding right char
        for r in range(len(s1), len(s2)):
            # store prev count of new right char
            prev = s2_dict.get(s2[r], 0)
            # increment s2_dict count
            s2_dict[s2[r]] = 1 + s2_dict.get(s2[r],0)

            # if the char is needed then update 'matches'
            if s2[r] in s1_dict:
                # previously was 1 less than needed -> matches +1
                if prev == s1_dict[s2[r]] - 1:
                    matches +=1
                # previously was equal to what was needed -> matches -1
                elif prev == s1_dict[s2[r]]:
                    matches-=1
                
            # removing left char
            # store prev count of old char
            prev = s2_dict.get(s2[l],0)
            # decrement s2_dict count
            s2_dict[s2[l]] = prev - 1

            if s2[l] in s1_dict:
                # previously was equal to needed
                if prev == s1_dict[s2[l]]:
                    matches -= 1
                # previously was 1 less than needed
                elif prev == s1_dict[s2[l]] + 1:
                    matches += 1
            l+=1

            if matches == len(s1_dict):
                return True

        return False



                    



            
