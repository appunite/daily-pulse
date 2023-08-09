import asyncio

from daily_pulse.utils.prompt import promptMultipleTexts, promptSingleText
from daily_pulse.utils.slack import getSlackMessageAsPlainText
from daily_pulse.utils.text.date import getFormattedTargetDate
from daily_pulse.utils.text.document import mapTextsToDocuments
from daily_pulse.utils.instances.llm import summarize_individual_long_chain, summarize_individual_short_chain, summarize_cta_day_chain, summarize_no_documents_chain

async def getSummarizedLong (documents):
  return await promptMultipleTexts(summarize_individual_long_chain, documents)

async def getSummarizedShortOfLong (documents):
  return await promptMultipleTexts(summarize_individual_short_chain, documents)

async def getSummarizeCTA ():
  return await promptSingleText(summarize_cta_day_chain, '')

async def getSummarizeNoDocumentsCTA ():
  return await promptSingleText(summarize_no_documents_chain, '')

async def getSummarizedAllDayMessage (pages):
  documents = [page['document'] for page in pages]
  day_summarize_cta, documents_summarized_long = await asyncio.gather(*[getSummarizeCTA(), getSummarizedLong(documents)])

  day_title_day = getFormattedTargetDate(format="%b %d", withSuffix=True)
  day_summarize_title = f'🤝 ADR Summary for {day_title_day}:'
  day_summarize_cta_escaped = day_summarize_cta.replace('"', '')

  documents_summarized_long_parsed = mapTextsToDocuments(documents_summarized_long)
  documents_summarized_short = await getSummarizedShortOfLong(documents_summarized_long_parsed)

  documents_summarized_list_stripped = [d.replace("\n", "") for d in documents_summarized_short]
  documents_summarized_list = [f"`[{i+1}]` {d} `<{pages[i]['url']}|*ADR»*>`" for i, d in enumerate(documents_summarized_list_stripped)]
  documents_summarized_combined = "\n\n".join(documents_summarized_list)

  return getSlackMessageAsPlainText(day_summarize_title, day_summarize_cta_escaped, documents_summarized_combined)