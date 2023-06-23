class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set({})

        for email in emails:
            local, domain = email.split("@")
            local = local.split('+')[0]
            local = local.replace('.', '')
            unique_emails.add(local + '@' + domain)
        
        print(unique_emails)
        return len(unique_emails)