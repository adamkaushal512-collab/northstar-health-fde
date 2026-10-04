from dataclasses import dataclass
@dataclass(frozen=True)
class FeedbackItem:
 source:str; category:str; severity:str; description:str
def route_feedback(item:FeedbackItem)->str:
 if item.category in {"safety","privacy"} or item.severity=="critical": return "red_team_and_block_release"
 if item.category in {"ai_quality","retrieval"}: return "evaluation_backlog"
 if item.category in {"workflow","usability"}: return "product_backlog"
 return "engineering_backlog"
