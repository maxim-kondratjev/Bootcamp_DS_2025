from agents import function_tool, RunContextWrapper

@function_tool
async def get_interview_context(ctx: RunContextWrapper[None]) -> str:
    """
    Вспоминает историю диалога в рамках интервью

    Arguments:
        messages: Список сообщений для обработки.
    
    Return:
        history: История диалога.
    """
    print('get_interview')
    history = ctx.context.get("messages", [])
    print(history)
    return history