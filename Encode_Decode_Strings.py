class Solution:

    def encode(self, strs: List[str]) -> str:
        # lets use the length to signify the count for the string
        # lets use # as a separator and ensure we ignore it if it ends up in the string.
        # there were two issues handling empty strings 0# and ""
        encoded = ''
        for s in strs:
            length = len(s)
            encoded += str(length)
            encoded += '#'
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        cur_len = ''

        run_len = 0
        decode_str = False
        cur_str = ''
        decode_len = 0

        for a in s:
            if a == "#" and decode_str == False:
                decode_str = True
               
                if cur_len == '0' or cur_len == '':
                    decode_len = 0
                    decoded.append("")
                    decode_str = False
                else:   
                    decode_len = int(cur_len)
                continue

            if decode_str:
                cur_str += a
                run_len += 1
                if run_len == decode_len:
                    decode_str = False
                    decode_len = 0
                    run_len = 0
                    cur_len = ''
                    decoded.append(cur_str)
                    cur_str = ''
            else:
                cur_len += a

        return decoded