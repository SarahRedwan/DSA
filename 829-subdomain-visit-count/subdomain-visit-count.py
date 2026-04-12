class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq={}

        for item in cpdomains:
            #split domain and count
            count,domain=item.split()
            count=int(count)
            #split the domain into subdomain
            parts=domain.split('.')

            #build the subdomin and count theeri frequency
            for i in range(len(parts)):
                subdomain=".".join(parts[i:])

                if subdomain in freq:
                    freq[subdomain]+=count
                else:
                    freq[subdomain]=count
        #build the result 
        result=[]
        for domain in freq:
            result.append(str(freq[domain])+" "+domain)
        return result

        