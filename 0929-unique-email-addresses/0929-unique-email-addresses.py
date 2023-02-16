class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_mails = set({})
        for curr in emails:
            local, domain = curr.split('@')
            builder = ''
            local_to_build = ''
            for ch in local.split('+')[0]:
                if ch != '.':
                    local_to_build += ch
            builder += local_to_build
            builder += '@'
            builder += domain
            unique_mails.add(builder)
        
        return len(unique_mails)