import asyncio

async def promptSingleText (chain, text):
  return await chain.arun({"input_documents": [text], "text": text})

async def promptMultipleTexts (chain, texts):
  texts_prompt_promise = [promptSingleText(chain, t) for t in texts]
  texts_prompt = await asyncio.gather(*texts_prompt_promise)
  return texts_prompt