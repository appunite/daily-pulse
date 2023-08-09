import requests
from langchain.docstore.document import Document

from daily_pulse.config import config
from daily_pulse.utils.text.markdown import (
    convertBlocksToMarkdown,
    convertStandardPageInfoToMarkdown,
)


def getStandarizedPageInfo(pageObject):
    return {
        "id": pageObject["id"],
        "url": pageObject["url"],
        "name": pageObject["properties_value"]["Name"][0]["plain_text"],
        "type": pageObject["properties_value"]["Type"]["name"],
        "status": pageObject["properties_value"]["Status"]["name"],
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
    }

    return {
        "id": "06151dd6-4767-46eb-8282-7fdd02ffb328",
        "url": "https://www.notion.so/Jerry-joins-OPNR-FT-for-two-weeks-06151dd6476746eb82827fdd02ffb328",
        "document": Document(
            page_content="Title: Jerry joins OPNR FT for two weeks Type: Decision Status: Decided URL: https://www.notion.so/Jerry-joins-OPNR-FT-for-two-weeks-06151dd6476746eb82827fdd02ffb328 --- # Context Context is written in below document, this ADR is created for hygiene reasons. [https://www.notion.so/appunite/Increase-Jerry-engagement-in-OPNR-for-FT-600330c2a91f45ad892ad6e38653adca](https://www.notion.so/appunite/Increase-Jerry-engagement-in-OPNR-for-FT-600330c2a91f45ad892ad6e38653adca) # What problems do we aim to solve There is a lot of product design work right now which can be a bottleneck. # Hypothesis Having Jerry FT for 2 weeks boosts product and won’t affect client’s finances. # Implementation plan Jerry is working FT in OPNR from 07.08.2023 - 18.08.2023 # Changelog * / - * *List important moments for this card* Damian Dębicki / Aug 9, 2023 - card created"
        ),
    }
