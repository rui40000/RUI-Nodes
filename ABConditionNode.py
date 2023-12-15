
class ABConditionNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "A": ("FLOAT", {  # 使用FLOAT以支持小数输入
                    "default": 0.0,  # 默认值为0.0
                }),
            },
        }

    RETURN_TYPES = ("INT",)

    FUNCTION = "calculate_B"

    CATEGORY = "Math Operations"

    def calculate_B(self, A):
        if A == 0:  # 使用==比较，确保只有当A严格等于0时才返回1
            B = 1
        else:
            B = 2
        return (B,)
