class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique_emails = set()

        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique_email = local+"@"+domain
            if unique_email not in unique_emails:
                unique_emails.add(unique_email)
        return len(unique_emails)