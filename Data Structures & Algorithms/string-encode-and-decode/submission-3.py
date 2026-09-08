class Solution:
    def encode(self, strs: list[str]) -> str:
        # strs = ["Hello","World"]
        encoded_str = ""
        for text in strs:
            encoded_str += f"{len(text)}#{text}"
        return encoded_str

    def decode(self, encoded_str: str) -> list[str]:
        count = ""
        decoded_lst = []
        i = 0
        while i < len(encoded_str):
            char = encoded_str[i]
            if char == "#":
                length = int(count)
                dest = i + 1 + length
                decoded_lst.append(encoded_str[i + 1: dest])
                i = dest
                count = ""
            else:
                count += char
                i += 1
        return decoded_lst