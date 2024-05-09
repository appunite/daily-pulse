import requests
from langchain.docstore.document import Document
from glom import glom

from daily_pulse.config import config
from daily_pulse.utils.text.markdown import (
    convertBlocksToMarkdown,
    convertStandardPageInfoToMarkdown,
)


def getNameElementText(nameElement):
    plain_text = nameElement["plain_text"]

    if plain_text == "Untitled":
        return "[no access]"

    return plain_text


def getStandarizedPageInfo(pageObject):
    name = pageObject["properties_value"]["Name"]
    name_texts = [getNameElementText(name_element) for name_element in name]

    return {
        "id": pageObject["id"],
        "url": pageObject["url"],
        "name": "".join(name_texts),
        "type": glom(pageObject, "properties_value.Type.name", default=""),
        "status": glom(pageObject, "properties_value.Status.name", default=""),
        "decision": glom(pageObject, "properties_value.Decision.name", default=""),
    }


def getPageChildrenBlocks(pageId):
    url = config["GET_PAGE_CONTENT_HOOK"]
    json = {"id": pageId, "Authorization": f"Bearer {config['AUTH_CODE']}"}

    resp = requests.post(url=url, json=json)
    return resp.json()


def getPageWithDocument(pageObject):
    standarized_page = getStandarizedPageInfo(pageObject)
    page_children = getPageChildrenBlocks(standarized_page["id"])
    page_children_markdown = convertBlocksToMarkdown(page_children)
    page_header_markdown = convertStandardPageInfoToMarkdown(standarized_page)
    page_document_content = "\n".join([page_header_markdown, page_children_markdown])
    page_document = Document(page_content=page_document_content)

    return {
        "id": standarized_page["id"],
        "url": standarized_page["url"],
        "document": page_document,
        "name": standarized_page["name"],
        "type": standarized_page["type"],
        "status": standarized_page["status"],
        "decision": standarized_page["decision"],
    }
