from notion2md.convertor.block import BlockConvertor

def convertBlocksToMarkdown(blocks):
    convertor = BlockConvertor(None, None)
    return convertor.convert(blocks)

def convertStandardPageInfoToMarkdown(pageInfo):
    return f"""
        Title: {pageInfo["name"]}
        Type: {pageInfo["type"]}
        Status: {pageInfo["status"]}
        URL: {pageInfo["url"]}
        ---
    """
