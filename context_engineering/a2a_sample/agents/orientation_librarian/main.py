import uvicorn
import json
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers.default_request_handler import DefaultRequestHandler
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import TaskState, Part, TextPart, Task, TaskStatus, AgentCard
from a2a.utils import completed_task, new_artifact
from agent import librarian_llm

class LibrarianExecutor(AgentExecutor):
    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        query = context.get_user_input()
        
        # Gọi logic xử lý từ ADK agent
        # Lưu ý: Trong thực tế, bạn có thể kiểm tra trạng thái Task để quyết định 
        # trả về 'input-required' (nếu cần hỏi thêm) hoặc 'completed'.
        response = await librarian_llm.invoke_async(query, session_id=context.context_id)
        
        # Đóng gói kết quả vào Artifact
        parts = [Part(root=TextPart(text=str(response)))]
        artifact = new_artifact(parts, name=f"orientation_goal_{context.task_id}")
        
        # Gửi sự kiện hoàn thành Task về Event Queue
        await event_queue.enqueue_event(
            completed_task(
                task_id=context.task_id,
                context_id=context.context_id,
                artifacts=[artifact]
            )
        )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        await event_queue.enqueue_event(
            Task(
                id=context.task_id,
                context_id=context.context_id,
                status=TaskStatus(state=TaskState.canceled)
            )
        )

# Tải cấu hình Agent Card
with open("agent.json", "r") as f:
    agent_card_data = json.load(f)
agent_card = AgentCard.model_validate(agent_card_data)

# Thiết lập máy chủ A2A
handler = DefaultRequestHandler(
    agent_executor=LibrarianExecutor(),
    task_store=InMemoryTaskStore()
)

app = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=handler
)

if __name__ == "__main__":
    uvicorn.run(app.build(), host="0.0.0.0", port=10001)