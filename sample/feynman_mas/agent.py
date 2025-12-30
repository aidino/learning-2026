from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent, BaseAgent
from google.adk.events import Event, EventActions
from google.adk.tools import google_search # Công cụ tra cứu tích hợp [3]
from google.genai import types


# --- ĐỊNH NGHĨA CÁC TÁC NHÂN CHUYÊN BIỆT ---

# Bước 1: Chọn chủ đề và lập bản đồ kiến thức ban đầu [4]
concept_mapper = LlmAgent(
    model="gemini-2.5-flash",
    name="ConceptMapper",
    instruction="""Xác định cụ thể chủ đề cần học. Viết ra tất cả những gì bạn biết 
    về chủ đề này một cách có cấu trúc.""",
    output_key="initial_mapping" # Lưu vào session.state [5]
)

# Bước 2: Giải thích cho trẻ 12 tuổi (Teach) [6]
explainer = LlmAgent(
    model="gemini-2.5-flash",
    name="TheExplainer",
    instruction="""Dựa trên {initial_mapping}, hãy giải thích khái niệm này như đang dạy một đứa trẻ 12 tuổi. 
    Không dùng thuật ngữ chuyên môn (jargon), sử dụng ngôn ngữ đơn giản nhất có thể.""",
    output_key="current_explanation"
)

# Bước 3: Phản biện tìm lỗ hổng kiến thức (Identify Gaps) [7]
child_critic = LlmAgent(
    model="gemini-2.5-flash",
    name="ChildCritic",
    instruction="""Đóng vai một đứa trẻ tò mò, phân tích {current_explanation} và liên tục hỏi 'Tại sao?'. 
    Chỉ ra những điểm giải thích còn mơ hồ hoặc các bước nhảy logic không rõ ràng.""",
    output_key="knowledge_gaps"
)

# Bước 3 (Bổ sung): Nghiên cứu mục tiêu để lấp đầy lỗ hổng [7]
targeted_researcher = LlmAgent(
    model="gemini-2.5-flash",
    name="TargetedResearcher",
    instruction="""Sử dụng công cụ tìm kiếm để nghiên cứu sâu các vấn đề được nêu trong {knowledge_gaps}. 
    Cung cấp thông tin chính xác để bổ sung vào kiến thức còn thiếu.""",
    tools=[google_search], # Trang bị công cụ tìm kiếm [8]
    output_key="remediation_data"
)

# Bước 4: Tinh luyện và đơn giản hóa bằng ẩn dụ (Simplify) [9]
narrative_refiner = LlmAgent(
    model="gemini-2.5-flash",
    name="NarrativeRefiner",
    instruction="""Tổng hợp {current_explanation} và {remediation_data}. 
    Viết lại một bản giải thích cuối cùng hoàn hảo, sử dụng các phép ẩn dụ (analogies) sinh động.""",
    output_key="final_explanation"
)

# Tác nhân kiểm tra điều kiện thoát vòng lặp [10]
class ExitChecker(BaseAgent):
    async def _run_async_impl(self, ctx):
        # Nếu ChildCritic không còn tìm thấy lỗ hổng đáng kể, thoát vòng lặp
        gaps = ctx.session.state.get("knowledge_gaps", "")
        is_clear = "không có lỗ hổng" in gaps.lower() or len(gaps) < 20
        
        # Gửi tín hiệu escalate=True để dừng LoopAgent [10]
        yield Event(author=self.name, actions=EventActions(escalate=is_clear))

# --- THIẾT LẬP LUỒNG CÔNG VIỆC (ORCHESTRATION) ---

# Vòng lặp tinh luyện kiến thức (Lặp lại Bước 2, 3, 4) [11]
refinement_loop = LoopAgent(
    name="RefinementLoop",
    sub_agents=[explainer, child_critic, targeted_researcher, narrative_refiner, ExitChecker(name="ConditionChecker")],
    max_iterations=3 # Giới hạn để tránh tiêu tốn token vô hạn [12]
)

# Tổng thể quy trình Feynman [1]
feynman_system = SequentialAgent(
    name="FeynmanCognitiveWorkflow",
    sub_agents=[concept_mapper, refinement_loop]
)

root_agent = feynman_system


