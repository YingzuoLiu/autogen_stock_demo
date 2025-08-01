from autogen import UserProxyAgent, AssistantAgent, GroupChat, GroupChatManager

# 用户代理
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINAL",
    max_consecutive_auto_reply=0,
)

# 单个助手代理：同时支持语言模型和代码执行
assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "model": "gpt-3.5-turbo",  # 可替换为本地模型
        "temperature": 0.7,
    },
    code_execution_config={"use_docker": False},
    description="理解自然语言请求并生成执行Python代码"
)

# 建立对话组和控制器
groupchat = GroupChat(
    agents=[user_proxy, assistant],
    messages=[],
    max_round=5
)

manager = GroupChatManager(groupchat=groupchat, name="manager")

# 启动对话
user_proxy.initiate_chat(manager, message="获取今天微软的股票数据并画图")
