
from .ABConditionNode import ABConditionNode
from .CharacterCountNode import CharacterCountNode

# 设置每个节点的CATEGORY属性确保它们在UI中被归类到"RUI"组
ABConditionNode.CATEGORY = "RUI"
CharacterCountNode.CATEGORY = "RUI"

NODE_CLASS_MAPPINGS = {
    "ABCondition": ABConditionNode,
    "CharacterCount": CharacterCountNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ABCondition": "A-B 条件节点",
    "CharacterCount": "字符计数节点",
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]
