
class CharacterCountNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text": ("STRING", {
                    "multiline": True,  # 允许多行文本输入
                    "default": ""
                }),
            },
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "count_characters"

    CATEGORY = "Text Processing"

    def count_characters(self, input_text):
        # 假设所有外部输入都会有一个额外的字符，并减去这个字符
        character_count = len(input_text) - 1 if input_text else 0
        return (str(character_count),)
