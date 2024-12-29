from pyrogram import types
from typing import AsyncGenerator, List, Optional, Union

class YourClient:
    # ... (rest of your client implementation)

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
        filters: List[str] = None  # List of message types to filter
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return

            messages = await self.get_messages(chat_id, list(range(current, current + new_diff + 1)))
            for message in messages:
                # Check if filters are provided and if the message type matches any of the filters
                if filters is None or message.media and any(filter_type in message.media for filter_type in filters):
                    yield message
                else:
                    yield 'filtered'
                current += 1
