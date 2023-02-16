class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_mails = set({})
        for curr in emails:
            local, domain = curr.split('@')
            local = local.split('+')[0]
            local = local.replace(".", "")
            unique_mails.add(local+'@'+domain)
        
        return len(unique_mails)