class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hset = set()

        for e in emails:
            separated = e.split('@')

            local_post_plus = separated[0].split('+')[0]
            local_post_period = local_post_plus.replace('.', '')

            hset.add(local_post_period + '@' + separated[1])

        return len(hset)