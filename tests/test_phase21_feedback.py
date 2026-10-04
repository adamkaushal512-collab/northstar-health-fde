from app.feedback.loop import FeedbackItem,route_feedback
def test_safety_feedback_blocks_release():
 assert route_feedback(FeedbackItem("pilot","safety","high","unsafe output"))=="red_team_and_block_release"
def test_ai_quality_enters_evaluation():
 assert route_feedback(FeedbackItem("specialist","ai_quality","medium","missed evidence"))=="evaluation_backlog"
def test_workflow_feedback_enters_product_backlog():
 assert route_feedback(FeedbackItem("specialist","workflow","low","extra click"))=="product_backlog"
