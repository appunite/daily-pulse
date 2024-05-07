# plain content message omits process of AI summarization
from daily_pulse.utils.slack import getSlackMessageAsPlainText
from daily_pulse.utils.text.date import getFormattedTargetDate


def getSummarizedPageLink(page, index):
    name = page["name"]
    url = page["url"]
    decision = f" *[{page['decision']}]*" if page["decision"] else ""

    return f"`[{index}]` {name}{decision} `<{url}|*ADR»*>`"


def getSummarizedAllDayMessageWithPlainContent(pages):
    day_title_day = getFormattedTargetDate(format="%b %-d", withSuffix=True)
    day_summarize_title = f"🤝 ADR Summary for {day_title_day}:"

    documents_summarized_list = [
        getSummarizedPageLink(page, i + 1) for i, page in enumerate(pages)
    ]

    documents_summarized_combined = "\n\n".join(documents_summarized_list)

    return getSlackMessageAsPlainText(
        day_summarize_title, "", documents_summarized_combined
    )
